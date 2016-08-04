#!/usr/bin/env python
#coding: utf-8
from datawiz_auth import Auth, APIGetError, APIUploadError
import pandas
import os
import logging
import math
#Потрібно перезавантажити модуль, щоб лог працював в ipython notebook
#Це звязано з тим, що logging.basicConfig звертається до того ж
# StreamHandler, що і notebook
reload(logging)
import json
from functools import wraps

RECEIPTS_API_URI = 'receipts'
CATEGORIES_API_URL = 'categories'
PRODUCTS_API_URL = 'products'
UNITS_API_URL = 'units'
CASHIERS_API_URL = 'cashiers'
TERMINALS_API_URL = 'terminals'
LOYALTY_API_URL = 'loyalty'
SHOPS_API_URL = 'shops'
# STOCKS_API_URL = 'stock'
PRICE_API_URL = 'date-prices'
STOCK_API_URL = 'product-inventory'
PURCHASE_DOCUMENT_URL = 'purchase_documents'
RECEIVE_DOCUMENT_URL = 'receive_documents'
RELOCATE_DOCUMENT_URL = 'relocate_documents'
SUPPLIER_URL = 'suppliers'
RECEIPTS_CHUNK_SIZE = 1000
DEFAULT_CHUNK_SIZE = 1000
SEPARATOR = ';'

logging.basicConfig(
    format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level = logging.DEBUG, file = 'log.txt')

class Up_DW(Auth):

    def _create_request_object(self, df, columns = []):

        """
        Функція формує правильний json-об’єкт для відправки на сервер

        """

        def _group_cartitems(receipt):

            cartitem_columns = ['product_id', 'base_price', 'qty', 'total_price']
            cartitems = receipt[cartitem_columns]
            cartitems['order_no'] = range(1, len(cartitems)+1)
            cartitems['price'] = cartitems['base_price']
            cartitems = cartitems.to_dict('records')
            total_price = (receipt.base_price*receipt.qty).sum()
            return pandas.Series({'cartitems': cartitems, 'total_price': total_price})

        df = df.groupby(['date', 'order_id', 'shop_id', 'terminal_id', 'cashier_id', 'loyalty_id'])\
            .apply(_group_cartitems)
        df = df.reset_index()
        return df.to_dict('records')

    def _split_list_to_chunks(self, lst, chunk_size=DEFAULT_CHUNK_SIZE):

        """
        Функція-генератор: розбиває список на чанки відповідно
        до розміру chunk_size
        """

        chunk_size = max(1, chunk_size)
        for i in xrange(0 , len(lst), chunk_size):
            yield lst[i:i+chunk_size]

    def _check_columns(columns):
        """
        Функція-декоратор, дозволяє виділяти колонки, потрібні для
        відправки на сервіс
        """

        def decorator(func):
            @wraps(func)
            def wrapper(self,*args, **kwargs):
                if isinstance(args[0], str) and kwargs.get('columns', None) is not None:
                    subcolumns = list(set(columns) & set(kwargs['columns']))
                    if len(subcolumns) != len(columns):
                        raise ValueError("Invalid columns: subcolumns [%s] is required "%','.join(columns))
                kwargs['subcolumns'] = columns
                return func(self, *args, **kwargs)
            return wrapper
        return decorator

    def _send_chunk_data(self,
                         resource_url,
                         data,
                         columns=None,
                         subcolumns=None,
                         skip_rows=1,
                         splitter=SEPARATOR,
                         columns_to_identify = None,
                         chunk_size=DEFAULT_CHUNK_SIZE
                         ):

        """
        Функція відправляє дані на сервер, попередньо розбивши на чанки
        columns: list ['column1', 'column2', ..., 'columnN']
            Імена колонок об’єкта DataFrame
        subcolumns: list ['column1', 'column2', ..., 'columnN']
            Імена колонок, які ми відправляємо серверу
        skiprows: int, default: 1
            Кількість рядків файлу, які необхідно пропустити
        columns_to_identify: list ['column1', 'column2', ..., 'columnN']
            Список колонок, по яких ідентифікуємо дублікати

        """

        chunk_num = 1
        if isinstance(data, list):
            # Якщо переданий список об’єктів, розбиваємо його на чанки
            for chunk in self._split_list_to_chunks(data):
                try:
                    # Відправляємо на сервер
                    invalid_elements = self._post(resource_url , data = chunk, chunk= True)
                    logging.info('Data chunk uploaded, %s elements failed'%len(invalid_elements))
                except APIUploadError, error:
                    # self._upload_data_recursively(resource_url, data)
                    logging.error('Data chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1
        # Якщо ж переданий файл *.csv
        elif isinstance(data, str) and os.path.isfile(data):
            # Читаємо файл чанками розміром DEFAULT_CHUNK_SIZE
            reader = pandas.read_csv(data,
                                     header = None,
                                     chunksize = chunk_size,
                                     names = columns,
                                     sep = splitter,
                                     skiprows = skip_rows,
                                     encoding = 'utf8')
            logging.info('Data upload started')
            for chunk in reader:
                if subcolumns:
                    chunk = chunk[subcolumns]
                # Замінює всі значення NaN в таблиці на None
                # Потрібно для того, щоб передавати в словнику json значення null замість nan
                chunk = chunk.where((pandas.notnull(chunk)), None)
                # Колонки, по яких будемо ідентифікувати дублікати
                # За замовчуванням - всі, крім першої
                if columns_to_identify is None:
                    columns_to_identify = list(chunk.columns)[1:]
                # chunk = chunk.drop_duplicates(columns_to_identify)
                try:
                    # Відправляємо на сервер
                    invalid_elements = self._post(resource_url, data = chunk.to_dict('records'), chunk=True)
                    logging.info('Data chunk #%s uploaded, %s elements failed'%(chunk_num, len(invalid_elements)))
                except APIUploadError, error:
                    logging.error('Data chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1
        else:
            raise TypeError('Invalid arguments')

    # Якщо відправка провалюється,розбиває чанк на ще менші частини
    def _upload_data_recursively(self, resource_url, data, delimeter = 10):
        if len(data) <= delimeter:
            for obj in data:
                try:
                    self._post(resource_url, data = data)
                    logging.info('Subchunk uploaded')
                except APIUploadError:
                    logging.error('Subchunk upload failed')
            return True
        chunk_size = int(math.ceil(float(len(data))/delimeter))
        for chunk in self._split_list_to_chunks(data, chunk_size=chunk_size):
            try:
                self._post(resource_url, data = chunk)
                logging.info('Subchunk <length %s> uploaded'%len(chunk))
            except APIUploadError:
                self._upload_data_recursively(resource_url, chunk)
                logging.error('Subchunk <length %s> upload failed. Trying with peaces'%len(chunk))

    @_check_columns(['shop_id',
                     'terminal_id',
                     'cashier_id',
                     'loyalty_id',
                     'order_id',
                     'date',
                     'product_id',
                     'base_price',
                     'qty',
                     'total_price'])
    def upload_receipts(self, receipts, columns = None, subcolumns = None, splitter = SEPARATOR, skip_rows = 1):
        """

        Функція відправляє на сервер дані по чеках
        Приймає список об’єктів чека в форматі

        [{
                   'order_id': <order_id>,
                   'date': <date>,
                   'terminal_id': <terminal_id>,
                   'cartitems': [
                            {
                            "order_no": <order_no>,
                            "product_id": <product_id>,
                            "base_price": <base_price>,
                            "price": <price>,
                            "qty": <qty>,
                            "total_price": <total_price>
                            }
                            ...
                   ]
                   'loyalty_id': <loyalty_id>,
                   'cashier_id': <cashier_id>,
                   'shop_id': <shop_id>
        }
        ...
            ]

        або шлях до файлу *.csv
        columns: list,
                 default: ['category_id', 'name', 'parent_id']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = [
                        'shop_id',
                        'terminal_id',
                        'cashier_id',
                        'loyalty_id',
                        'order_id',
                        'date',
                        'product_id',
                        'base_price',
                        'qty',
                        'total_price']

        # Якщо переданий список об’єктів чека
        chunk_num = 1
        if isinstance(receipts, list):
            # Розбиваємо список на частини і відправляємо на сервер
            for chunk in self._split_list_to_chunks(receipts,
                                                    chunk_size=RECEIPTS_CHUNK_SIZE):
                try:

                    invalid_elements = self._post(RECEIPTS_API_URI, data=chunk, chunk=True)
                    logging.info('Receipts chunk uploaded, %s elements failed'%len(invalid_elements))
                except APIUploadError, error:
                    #self._upload_data_recursively
                    logging.error('Receipts chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1
            return True
        # Якщо ж переданий шлях до файлу
        elif isinstance(receipts, str) and os.path.isfile(receipts):
            # Читаємо файл чанками розміром RECEIPTS_CHUNK_SIZE
            reader = pandas.read_csv(receipts,
                                     header = None,
                                     chunksize = RECEIPTS_CHUNK_SIZE,
                                     names = columns,
                                     sep = splitter,
                                     skiprows = skip_rows)
            last_chunk = None
            logging.info('Receipts upload started')
            for chunk in reader:
                # Замінює всі значення NaN в таблиці на None
                # Потрібно для того, щоб передавати в словнику json значення null замість nan
                chunk = chunk.where((pandas.notnull(chunk)), None)
                if last_chunk is not None:
                    last_order = list(last_chunk.tail(1)['order_id'])[0]
                    receipt_chunk = chunk[chunk['order_id'] == last_order]
                    # Чанк, в якому немає останнього чека з попереднього чанка
                    chunk = chunk[chunk['order_id'] != last_order]
                    # Додаємо в попередній чанк частини чека, розбиті пандою (якщо вони є)
                    last_chunk = last_chunk.append(receipt_chunk)
                    # Створюємо об’єкт запиту для передачі на сервер
                    data = self._create_request_object(last_chunk)
                    # Якщо чанк пустий (всі записи чанка відносяться
                    # до попередньго чека)
                    if chunk.empty:
                        continue
                    try:
                        self._post(RECEIPTS_API_URI, data = data, chunk=True)
                        logging.info('Receipts chunk #%s uploaded'%chunk_num)
                    except APIUploadError:
                        #self._upload_data_recursively
                        logging.error('Receipts chunk #%s upload failed'%chunk_num)
                    chunk_num += 1
                last_chunk = chunk
            try:
                data = self._create_request_object(last_chunk)
                self._post(RECEIPTS_API_URI, data = data, chunk=True)
                logging.info('Receipts chunk #%s uploaded'%chunk_num)
            except APIUploadError, error:
                #self._upload_data_recursively
                logging.error('Receipts chunk #%s upload failed\n%s'%(chunk_num, error))
        else:
            raise TypeError("Invalid params")
        return True

    @_check_columns(['category_id', 'name', 'parent_id'])
    def upload_categories(self, categories,
                          columns = None, subcolumns = None,
                          splitter=SEPARATOR):
        """
        Функція відправляє на сервер дані категорій
        Приймає список об’єктів категорії в форматі

        [
            {
                   'category_id': <category_id>,
                   'name': <name>,
                   'parent_id': <parent_id>,
            }
            ...
        ]

        або шлях до файлу *.csv

        columns: list,
                 default: ['category_id', 'name', 'parent_id']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = ['category_id',
                       'name',
                       'parent_id'
                      ]
        self._send_chunk_data(CATEGORIES_API_URL,
                              categories,
                              columns = columns,
                              subcolumns = subcolumns,
                              splitter = splitter)
        return True

    @_check_columns(['product_id', 'article','barcode', 'name', 'category_id', 'unit_id'])
    def upload_products(self, products, columns = None, subcolumns = None, splitter = SEPARATOR):

        """
        Функція відправляє серверу дані товарів
        Приймає список об’єктів товарів в форматі

        [
            {
                   'product_id': <category_id>,
                   'barcode': <code>,
                   'article': <article>,
                   'name': <name>,
                   'category_id': <category_id>,
                   'unit_id': <unit_id>

            }
            ...
        ]

        або шлях до файлу *.csv

        columns: list,
                 default: [
                        'product_id',
                        'barcode',
                        'article',
                        'name',
                        'category_id',
                        'unit_id',
                        'length',
                        'width',
                        'height',
                        'review',
                        'photo'
                        ]
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = [
                        'product_id',
                        'barcode',
                        'article',
                        'name',
                        'category_id',
                        'unit_id',
                        'length',
                        'width',
                        'height',
                        'review',
                        'photo'
                        ]

        return self._send_chunk_data(PRODUCTS_API_URL,
                                     products,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter
                                     )

    @_check_columns(['unit_id', 'name'])
    def upload_units(self, units, columns = None, subcolumns = None, splitter = SEPARATOR):

        """
        Функція відправляє серверу дані по одиницях виміру товарів
        Приймає список об’єктів одиниці виміру в форматі

        [
            {
                   'unit_id': <unit_id>,
                   'name': <name>,
            }
            ...
        ]
        або шлях до файлу *.csv

        columns: list,
                 default: ['unit_id', 'name']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = ['unit_id', 'name']
        return self._send_chunk_data(UNITS_API_URL,
                                     units,
                                     columns=columns,
                                     subcolumns=subcolumns,
                                     splitter = splitter)

    @_check_columns(['loyalty_id', 'cardno', 'client_birthday'])
    def upload_loyalty_client_info(self, clients, columns = None, subcolumns = None, splitter = SEPARATOR):

        """
        Функція відправляє серверу дані по клієнтах
        Приймає список об’єктів клієнта в форматі

        [
            {
                   'loyalty_id': <loyalty_id>,
                   'cardno': <cardno>,
                   'client_name': <client_name>,
                   'client_birthday': <client_birthday>

            }
            ...
        ]

        або шлях до файлу *.csv

        columns: list,
                 default: ['loyalty_id',
                           'cardno',
                           'shop_id',
                           'registration_date',
                           'first_name',
                           'last_name',
                           'sex',
                           'client_birthday',
                           'address',
                           'email'
                           ]
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        def _get_client_name(obj):
            #Створюємо ім’я клієнта, орієнтуючись на obj.first_name, obj.last_name
            name = obj.first_name
            last_name = obj.last_name
            # Перевірка на NaN значення
            if name!=name and last_name!=last_name:
                return ''
            elif name!=name and last_name == last_name:
                return last_name
            elif name == name and last_name != last_name:
                return name
            else:
                return '%s %s'%(name, last_name)

        chunk_num = 1
        # Якщо переданий список об’єктів клієнта
        if isinstance(clients, list):
            # Розбиваємо список на частини і відправляємо на сервер
            for chunk in self._split_list_to_chunks(clients,
                                                    chunk_size=DEFAULT_CHUNK_SIZE):
                try:
                    invalid_elements = self._post(LOYALTY_API_URL, data = chunk, chunk=True)
                    logging.info('Clients chunk #%s uploaded, %s elements failed'%(chunk_num, len(invalid_elements)))
                except APIUploadError, error:
                    logging.error('Clients chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1

        # Якщо ж переданий шлях до файлу
        elif isinstance(clients, str) and os.path.isfile(clients):
            if columns is None:
                columns = ['loyalty_id',
                           'cardno',
                           'shop_id',
                           'registration_date',
                           'first_name',
                           'last_name',
                           'sex',
                           'client_birthday',
                           'address',
                           'email'
                           ]
            # client_name створюємо динамічно, тому додаємо його тут
            # subcolums.append('client_name')
            chunk_num = 1
            # Читаємо файл чанками розміром DEFAULT_CHUNK_SIZE
            reader = pandas.read_csv(clients,
                                     header = None,
                                     chunksize = DEFAULT_CHUNK_SIZE,
                                     names = columns,
                                     sep = SEPARATOR,
                                     skiprows = 1)
            for chunk in reader:
                # chunk['client_name'] = chunk[['first_name', 'last_name']].apply(_get_client_name, axis = 1)
                chunk = chunk[subcolumns]
                # Замінює всі значення NaN в таблиці на None
                # Потрібно, щоб передавати в словнику json значення null замість nan
                chunk = chunk.where((pandas.notnull(chunk)), None)
                logging.info('Data upload started')
                try:
                    invalid_elements = self._post(LOYALTY_API_URL, data = chunk.to_dict('records'), chunk=True)
                    logging.info('Clients chunk #%s uploaded, %s elements failed'%(chunk_num, len(invalid_elements)))
                except APIUploadError, error:
                    logging.error('Clients chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1
        else:
            raise TypeError('Invalid arguments')
        return True

    @_check_columns(['cashier_id', 'name'])
    def upload_cashiers(self, cashiers, columns = None, subcolumns = None, splitter = SEPARATOR):
        """
        Функція відправляє серверу дані по касирах
        Приймає список об’єктів касира в форматі

        [
            {
                'cashier_id': <cashier_id>,
                'name': <name>

            }
            ...
        ]

        або шлях до файлу *.csv
        columns: list,
                 default: ['cashier_id', 'name']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """
        if columns is None:
            columns = ['cashier_id', 'name']
        return self._send_chunk_data(CASHIERS_API_URL,
                                     cashiers,
                                     columns=columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)

    @_check_columns(['terminal_id', 'shop_id', 'name'])
    def upload_terminals(self, terminals, columns = None, subcolumns = None, splitter = SEPARATOR):
        """
        Функція відправляє серверу дані по терміналах
        Приймає список об’єктів термінала в форматі

        [
            {
                'terminal_id': <terminal_id>,
                'shop_id': <shop_id>,
                'name': <name>

            }
            ...
        ]
        або шлях до файлу *.csv

        columns: list,
                 default: ['terminal_id', 'shop_id', 'name']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """
        if columns is None:
            columns = ['terminal_id', 'shop_id', 'name']
        return self._send_chunk_data(TERMINALS_API_URL,
                                     terminals,
                                     columns=columns,
                                     subcolumns = subcolumns,
                                     splitter = SEPARATOR)

    @_check_columns(['shop_id', 'name', 'address', 'open_date'])
    def upload_shops(self, shops, columns = None, subcolumns = None, splitter = SEPARATOR):
        """
        Функція завантажує на сервіс дані магазинів
        Приймає список об’єктів магазина в форматі

        [
            {
                'shop_id': <shop_id>,
                'name': <name>,
                'address': <address>,
                'open_date': <open_date>

            }
            ...
        ]

        або шлях до файлу *.csv

        columns: list,
                 default: ['shop_id', 'name', 'address', 'open_date']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """
        if columns is None:
            columns = [
                       'shop_id',
                       'name',
                       'address',
                       'open_date'
                       ]
        return self._send_chunk_data(SHOPS_API_URL,
                                     shops,
                                     columns=columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)

    @_check_columns(['shop_id', 'product_id', 'date', 'original_price', 'price'])
    def upload_price(self, prices, columns = None, subcolumns = None, splitter = SEPARATOR):
        """
        Функція завантажує на сервіс дані по цінам
        Приймає список об’ктів в форматі

        [
            {
               'shop_id': <shop_id>,
               'product_id': <product_id>,
               'date': <date>,
               'original_price': <original_price>,
               'price': <price>
            }
        ]
        або шлях до файлу *.csv

        columns: list,
                 default: ['product_id', 'date', 'shop_id', 'original_price', 'price']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = ['product_id', 'date', 'shop_id', 'original_price', 'price']
        return self._send_chunk_data(PRICE_API_URL,
                                     prices,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)

    @_check_columns(['shop_id', 'product_id', 'date', 'qty', 'original_price', 'stock_total_price'])
    def upload_inventory(self, stocks, columns = None, subcolumns = None, splitter = SEPARATOR):

        """
        Функція завантажує на сервіс дані по залишкам
        Приймає список об’ктів в форматі

        [
            {
               'shop_id': <shop_id>,
               'product_id': <product_id>,
               'date': <date>,
               'qty': <qty>,
               'original_price': <original_price>,
               'stock_total_price': <price>
            }
        ]

        або шлях до файлу *.csv

        columns: list,
                 default: ['product_id', 'dt', 'shop_id', 'original_price', 'price']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = ['invoice_id', 'invoice_inner_id',
                       'shop_id', 'order_id',
                       'provider_id', 'date', 'employee_id',
                       'product_id','qty', 'original_price',
                       'stock_total_price']


        return self._send_chunk_data(STOCK_API_URL, stocks,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)


    @_check_columns(['supplier_id', 'name'])
    def upload_suppliers(self, suppliers, columns=None, subcolumns=None, splitter=SEPARATOR):
        """
        Функція завантажує на сервер дані постачальників
        Приймає список об`єктів в форматі

        [
            {
                "supplier_id": <supplier_id>,
                "name": <name>,
                "supplier_code":<supplier_code>,
                "phone":<phone>,
                "commodity_credit_days":<commodity_credit_days>,
                "address":<address>
            }
        ]
         або шлях до файлу *.csv

         columns: list,
                 default: ['supplier_id',
                           'name', 'supplier_code',
                           'phone', 'commodity_credit_days',
                           'address']

                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """
        if columns is None:
            columns = ['supplier_id',
                       'name', 'supplier_code',
                       'phone', 'commodity_credit_days',
                       'address']

        return self._send_chunk_data(SUPPLIER_URL, suppliers,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)

    @_check_columns(['document_id', 'shop_id',
                     'supplier_id', 'product_id',
                     'qty', 'document_date',
                     'responsible','order_date', 'price', 'price_total'])
    def upload_purchase_doc(self, docs, columns=None, subcolumns=None, splitter=SEPARATOR):
        """
        Функція завантажує на сервер документи на замовлення товарів
        Приймає список об`єктів в форматі

        [
            {
                "document_id": <document_id>,
                "shop_id": <shop_id>,
                "supplier_id":<supplier_id>,
                "product_id":<product_id>,
                "qty":<qty>,
                "document_date":<document_date>,
                "document_number": <document_number>,
                "responsible": <responsible>,
                "order_date": <order_date>,
                "price": "<price>",
                "price_total":<price_total>
            }
        ]
         або шлях до файлу *.csv

         columns: list,
                 default: ['document_id', 'shop_id',
                           'supplier_id', 'product_id',
                           'qty', 'document_date',
                           'responsible','order_date', 'price', 'price_total', 'document_number']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns = ['document_id', 'shop_id',
                     'supplier_id', 'product_id',
                     'qty', 'document_date',
                     'responsible','order_date',
                       'price', 'price_total', 'document_number']

        return self._send_chunk_data(PURCHASE_DOCUMENT_URL, docs,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)

    @_check_columns(['document_id', 'supplier_id', 'shop_id',
                     'document_date', 'responsible', 'product_id', 'qty', 'price', 'price_total'])
    def upload_receive_doc(self, docs, columns=None, subcolumns=None, splitter=SEPARATOR):

        """
        Функція завантажує на сервер документи отримання товарів
        Приймає список об`єктів в форматі

        [
            {
                "document_id": <document_id>,
                "shop_id": <shop_id>,
                "supplier_id":<supplier_id>,
                "product_id":<product_id>,
                "qty":<qty>,
                "document_date":<document_date>,
                "document_number": <document_number>,
                "responsible": <responsible>,
                "order_id": <order_id>,
                "price": "<price>",
                "price_total":<price_total>
            }
        ]
         або шлях до файлу *.csv

         columns: list,
                 default: ['document_id', 'shop_id',
                           'supplier_id', 'product_id',
                           'qty', 'document_date',
                           'document_number',
                           'responsible','order_id', 'price', 'price_total']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """


        if columns is None:
            columns = ['document_id', 'supplier_id', 'document_number','order_id', 'shop_id',
                     'document_date', 'responsible', 'product_id', 'qty', 'price', 'price_total']

        return self._send_chunk_data(RECEIVE_DOCUMENT_URL, docs,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)

    @_check_columns(['relocate_id', 'relocate_date', 'product_id', 'qty'])
    def upload_relocate_doc(self, docs, columns=None, subcolumns=None, splitter=SEPARATOR):


        """
        Функція завантажує на сервер документи переміщення товарів
        Приймає список об`єктів в форматі

        [
            {
                "relocate_id": <relocate_id>,
                "relocate_date": <relocate_date>,
                "sender_shop_id": <sender_shop_id>,
                "receiver_shop_id": <receiver_shop_id>,
                "product_id":<product_id>,
                "qty":<qty>
            }
        ]
         або шлях до файлу *.csv

         columns: list,
                 default: ['document_id', 'shop_id',
                           'supplier_id', 'product_id',
                           'qty', 'document_date',
                           'document_number',
                           'responsible','order_id', 'price', 'price_total', 'qty']
                 Упорядкований список колонок таблиці в файлі <filename>.csv
        splitter: str, default: ";"
                 Розділювач даних в <filename>.csv
        """

        if columns is None:
            columns =['relocate_id', 'relocate_date', 'sender_shop_id', 'receiver_shop_id', 'product_id', 'qty']

        return self._send_chunk_data(RELOCATE_DOCUMENT_URL, docs,
                                     columns = columns,
                                     subcolumns = subcolumns,
                                     splitter = splitter)


    def upload_to_service(self, email, cache=True):
        """
        Функція запускає на сервері процес завантаження і кешування
        даних. Після його завершення користувач отримає повідомлення
        на вказану адресу електронної пошти

        Parameters
        --------------
        email: str
        Електронна адреса
        cache: bool, default = True
        Вказує, чи необхідно запускати процес кешування

        Examples
        -------------
            dw_up = Up_DW(API_KEY='my_private_api_key', API_SECRET = 'my_secret')
            dw_up.upload_to_service('my_email@mail.com', cache=False)

        """

        params = {'function': 'upload_to_service',
                  'email':email,
                  'cache': cache}
        return self._post('utils', data=params)['results']

    def cache(self,
              email,
              date_from=None,
              date_to = None,
              date_list = None,
              shops = None,
              ):
        """
        Функція запускає на сервері процес кешування
        даних. Після його завершення користувач отримає повідомлення
        на вказану адресу електронної пошти
        """

        params = {'function': 'cache_data',
                  'email':email,
                  'date_from': date_from,
                  'date_to': date_to,
                  'date_list': date_list,
                  'shops': shops}
        return self._post('utils', data=params)['results']

    def clear_receipts(self, email):
        """
        Функція викликає на сервері процес видалення чеків.
         Після його завершення користувач отримає повідомлення
        на вказану адресу електронної пошти
        """
        params = {'function': 'clear_receipts',
                  'email':email}
        return self._post('utils', data=params)['results']

    def clear_client(self, email, dlt=False):
        params = {'function':'clear_client',
                  'dlt':dlt,
                  'email':email}
        return self._post('utils', data=params)['results']


    def upload_data(self, path=None):

        if path is None:
            path = os.path.dirname(os.path.realpath(__file__))
        files = ['units.csv','categories.csv',
                 'shops.csv','terminals.csv',
                 'cashiers.csv','products.csv',
                 'clients.csv','prices.csv',
                 'inventory.csv','receipts.csv']
        dr = os.listdir(path)
        if [x for x in files if x not in dr]:
            logging.error('Required files is missing')
            return False
        self.upload_units(os.path.join(path,'units.csv'))
        self.upload_cashiers(os.path.join(path,'cashiers.csv'))
        self.upload_categories(os.path.join(path,'categories.csv'))
        self.upload_shops(os.path.join(path,'shops.csv'))
        self.upload_terminals(os.path.join(path,'terminals.csv'))
        self.upload_products(os.path.join(path,'products.csv'), columns=['product_id', 'barcode', 'name', 'category_id', 'unit_id'])
        self.upload_loyalty_client_info(os.path.join(path,'clients.csv'), columns=['loyalty_id', 'cardno', 'client_name', 'client_birthday', 'is_male', 'discount'])
        self.upload_price(os.path.join(path,'prices.csv'))
        self.upload_inventory(os.path.join(path,'inventory.csv'), columns=['shop_id', 'product_id','date', 'qty', 'original_price', 'stock_total_price'])
        self.upload_receipts(os.path.join(path,'terminals.csv'), columns=['shop_id', 'terminal_id', 'cashier_id', 'loyalty_id', 'receipt_id', 'date', 'product_id','price','qty', 'total_price'])