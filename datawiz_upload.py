#!/usr/bin/env python
#coding: utf-8
from datawiz_auth import Auth, APIGetError, APIUploadError
import pandas
import os
import logging
import json


RECEIPTS_API_URI = 'receipts'
CATEGORIES_API_URL = 'categories'
PRODUCTS_API_URL = 'products'
RECEIPTS_CHUNK_SIZE = 1000
DEFAULT_CHUNK_SIZE = 100

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

    def _send_chunk_data(self,
                         resource_url,
                         data,
                         columns=None,
                         skiprows=1,
                         splitter=';'
                         ):

        """
        Функція відправляє дані на сервер, попередньо розбивши на чанки
        columns: list ['column1', 'column2', ..., 'columnN']
        Імена колонок об’єкта DataFrame

        """

        chunk_num = 1
        if isinstance(data, list):
            # Якщо переданий список об’єктів, розбиваємо його на чанки
            for chunk in self._split_list_to_chunks(data):
                try:
                    # Відправляємо на сервер
                    self._post(resource_url , data = data)
                except APIUploadError, error:
                    #self._upload_data_recursively
                    logging.error('Receipts chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1
        # Якщо ж переданий файл *.csv
        elif isinstance(data, str) and os.path.isfile(data):
            # Читаємо файл чанками розміром DEFAULT_CHUNK_SIZE
            reader = pandas.read_csv(data,
                                     header = None,
                                     chunksize = DEFAULT_CHUNK_SIZE,
                                     names = columns,
                                     sep = splitter,
                                     skiprows = skiprows)
            logging.info('Data upload started')
            for chunk in reader:

                try:
                    # Відправляємо на сервер
                    self._post(resource_url, data = chunk.to_dict('records'))

                except APIUploadError, error:
                    #self._upload_data_recursively
                    logging.error('Data chunk #%s upload failed\n%s'%(chunk_num, error))
                chunk_num += 1
        else:
            raise TypeError('Invalid arguments')

    #TODO: Розбиває чанк на менші частини і відправляє їх на сервер.
    # Якщо відправка провалюється,розбиває чанк на ще менші частини
    def _upload_data_recursively(self, resource_url, data, delimeter = 10):
        pass

    def upload_receipts(self, receipts, splitter = ';', skiplines = 0):
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
        Параметр splitter визначає розділювач для даних в заданому файлі
        defaul:';'
        """
        receipts_buff = []
        #Колонки чеків
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
                    self._post(RECEIPTS_API_URI, data=chunk)
                    logging.info('Receipts uploaded')
                except APIUploadError:
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
                                     skiprows = skiplines)
            last_chunk = None
            logging.info('Receipts upload started')
            for chunk in reader:
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
                        self._post(RECEIPTS_API_URI, data = data)
                        logging.info('Receipts chunk #%s uploaded'%chunk_num)
                    except APIUploadError:
                        print 'err'
                        #self._upload_data_recursively
                        logging.error('Receipts chunk #%s upload failed'%chunk_num)
                    chunk_num += 1
                last_chunk = chunk
            try:
                data = self._create_request_object(last_chunk)
                self._post(RECEIPTS_API_URI, data = data)
                logging.info('Receipts chunk #%s uploaded'%chunk_num)
            except APIUploadError, error:
                #self._upload_data_recursively
                logging.error('Receipts chunk #%s upload failed\n%s'%(chunk_num, error))
        else:
            raise TypeError("Invalid params")
        return True

    def upload_categories(self, categories):
        """
        Функція відправляє на сервер дані по категоріям
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
        """
        self._send_chunk_data(CATEGORIES_API_URL,
                              categories,
                              columns = ['category_id',
                                         'name',
                                         'parent_category'
                                         ])
        return True

    def upload_products(self, products):
        """
        Функція відправляє серверу дані по товарам
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
        """
        self._send_chunk_data(PRODUCTS_API_URL,
                              products,
                              columns = ['product_id',
                                         'code',
                                         'article',
                                         'name',
                                         'category_id',
                                         'unit_id'
                                         'l',
                                         'w',
                                         'h',
                                         'rw',
                                         'review',
                                         'photo'
                                         ])
        return True

    def upload_units(self, units):

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
        """

        self._send_chunk_data(UNITS_API_URL,
                              units,
                              columns=['unit_id', 'name'])

    def upload_loyalty_client_info(self, clients):

        """
        Функція відправляє серверу дані по клієнтах
        Приймає список об’єктів клієнта в форматі

        [
            {
                   'loyalty_id': <loyalty_id>,
                   'cardno': <cardno>,
                   'shop_id': <shop_id>,
                   'registration_date': <registration_date>,
                   'client_name': <client_name>,
                   'client_lastname':<client_lastname>,
                   'is_male': <is_male>,
                   'client_birthday': <client_birthday>,
                   'adress': <adress>,
                   'email': <email>



            }
            ...
        ]

        або шлях до файлу *.csv
        """
        return self._send_chunk_data(CLIENTS_API_URL, clients, columns = [])
