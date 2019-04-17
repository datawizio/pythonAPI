#!/usr/bin/env python
# coding:utf-8

from __future__ import print_function
from __future__ import absolute_import
import datetime, shutil, os, zipfile
import pandas as pd
from .datawiz_auth import Auth
from functools import wraps
import six
import csv
import warnings

INTERVALS = ['days', 'weeks', 'months', 'years']
MODEL_FIELDS = ['turnover', 'qty', 'receipts_qty', 'stock_qty',
                'profit', 'stock_value', 'turnover_rate', 'availability_sale', 'availability_stock',
                'sold_product_value', 'self_price_per_product', 'price', 'avg_receipt']
DAYS = 'days'
WEEKS = 'weeks'
MONTHS = 'months'
YEARS = 'years'
GET_PRODUCTS_SALE_URI = 'get_products_sale'
GET_CATEGORIES_SALE_URI = 'get_categories_sale'
GET_PRODUCTS_STOCK = 'products-stock'
GET_PRODUCTS_INVENTORY = 'product-inventory'
GET_CATEGORIES_STOCK = 'categories-stock'
GET_PRODUCT = 'core-products'
GET_RECEIPT = 'core-receipts'
GET_API_RECEIPT = 'receipts'
GET_CATEGORY = 'core-categories'
GET_LOYALTY_CUSTOMER = 'get_loyalty_customer'
SEARCH = 'search'
CLIENT = 'client'
SHOPS = 'core-shops'
UNITS = 'units'
TERMINALS = 'terminals'
CASHIERS = 'cashiers'
PAIRS = 'pairs'
UTILS = 'utils'
LOYALTY_SALES = 'loyalty-sales'
LOST_SALES = 'lost-sales'
SALES_PLAN = 'sales-plan'
SALES = 'sales'
SALE_INFO = 'sale-info'
SALE_DYNAMICS = 'sale-dynamics'
BRANDS = 'brands'
API_SHOPS = "shops"
GET_RAW_CATEGORIES = "categories"
RECEIPTS_DETAIL = "receipts-detail"
INVENTORY_DETAIL = "inventory-detail"
PROMOTION_DETAIL = "promotion-access-detail"
OLAP_REPORT = "olap-report"

if six.PY3:
    unicode = str


def iteritems(obj):
    if six.PY3:
        return obj.items()
    return obj.iteritems()


class DW(Auth):
    def _check_params(func):
        """
        Функція-декоратор, приймає іменовані аргументи і звіряє їх з заданим шаблоном
        """

        def id_list(var):
            if isinstance(var, list):
                return var  # splitter.join([str(x) for x in var])
            return [var]

        def value_in_list(var, lst):
            if var in lst:
                return var
            raise ValueError('Incorrect param value <%s>' % var)

        def value_or_iter_in_list(var, lst):
            if isinstance(var, list):
                if all([x if x in lst else None for x in var]):
                    return var
                raise ValueError('Incorrect param value <%s>' % var)
            elif var in lst:
                return [var]
            raise ValueError('Incorrect param value <%s>' % var)

        def stringify_date(date, format='%Y-%m-%d'):
            if isinstance(date, str):
                datetime.datetime.strptime(date, format)
                return date
            elif isinstance(date, (datetime.date, datetime.datetime)):
                return date.strftime(format)
            return None

        @wraps(func)
        def wrapper(self, **kwargs):

            # Отримуємо в kwargs всі іменовані аргументи функції, яку декоруємо
            for kwarg in kwargs:
                # Перевіряємо по шаблону, чи аргумент коректного типу
                if kwarg in params and isinstance(kwargs[kwarg], params[kwarg]['types']):
                    # Викликаємо задану в шаблоні функцію для обробки даних
                    kwargs[kwarg] = params[kwarg]['call'](kwargs[kwarg])
                elif kwarg in params and not isinstance(kwargs[kwarg], params[kwarg]['types']):
                    raise TypeError('Incorrect param type for <%s> ' % kwarg)
            return func(self, **kwargs)

        splitter = ','
        # Шаблони для змінних - в types допустимі типи, в call функція обробки данних змінної
        params = {'shops':
                      {'types': (int, list),
                       'call': id_list},
                  'categories':
                      {'types': (int, list),
                       'call': id_list},
                  'category':
                      {'types': int,
                       'call': lambda x: x},
                  'products':
                      {'types': (int, list),
                       'call': id_list},
                  'date_from':
                      {'types': (datetime.date, str),
                       'call': stringify_date},
                  'date_to':
                      {'types': (datetime.date, str),
                       'call': stringify_date},
                  'date': {'types': (datetime.date, str),
                           'call': lambda x: stringify_date(x, format="%Y-%m")},
                  'interval':
                      {'types': str,
                       'call': lambda x: value_in_list(x, INTERVALS)},
                  'loyalty':
                      {'types': (int, list),
                       'call': id_list},
                  'by':
                      {'types': (str, list),
                       'call': lambda x: value_or_iter_in_list(x, MODEL_FIELDS)},
                  'weekday':
                      {'types': int,
                       'call': lambda x: value_in_list(x, range(7))},
                  'weekdays':
                      {'types': list,
                       'call': id_list},
                  'id_list': {'types': list,
                              'call': id_list},
                  'price_from':
                      {'types': int,
                       'call': lambda x: x},
                  'price_to':
                      {'types': int,
                       'call': lambda x: x},
                  'hours': {'types': list,
                            'call': id_list},
                  'cardno': {'types': (str, list),
                             'call': id_list},
                  'sale_id': {'types': (int, list),
                              'call': id_list},
                  'name': {'types': (str, list),
                           'call': id_list},
                  'loyalty_id': {'types': (int, list),
                                 'call': id_list},
                  'on': {'types': str,
                         'call': lambda x: value_in_list(x, ['category', 'shops'])},
                  'level': {'types': int,
                            'call': lambda x: x},
                  'per_shop': {'types': bool,
                               'call': lambda x: x},
                  'window': {'types': int,
                             'call': lambda x: x},
                  'join': {'types': bool,
                           'call': lambda x: bool(x)},
                  'documents': {'types': dict,
                                'call': lambda x: x},

                  }
        return wrapper

    def _prepare_raw_results(self, results):
        res = {}
        for key, value in iteritems(results):
            if isinstance(key, (str, unicode)) and not 'url' in key:
                res[key] = value
        return res

    def _get_raw_data(self, url, params={}, params_data={}):
        """
        Функція для посторінкового завантаження даних. Повертає генератор
        """

        page = 1
        has_next = True

        while has_next:
            params.update({'page': page})
            data = self._get(url, params=params, data=params_data)
            results = data.get('results', [])

            has_next = bool(data.get('next'))
            page += 1
            yield [self._prepare_raw_results(x) for x in results]

    def _get_data_by_daterange(self, func, date_from, date_to):

        date_range = [x.date() for x in pd.date_range(start=date_from, end=date_to)]
        for date in date_range:
            yield func(date_from=date, date_to=date)

    def _sort_columns(self, dataframe, columns):
        columns_difference = set(dataframe.columns) - set(columns)
        columns_union = set(columns) & set(dataframe.columns)
        # TODO: add sorting of union columns
        ordered_columns = list(columns_difference) + columns
        return dataframe[ordered_columns]

    def _prepare_df_view(self, dataframe, view_type, view_column, index_column="date", columns_order=None, show=None):

        if columns_order is not None and isinstance(columns_order, list):
            dataframe = self._sort_columns(dataframe, columns_order)

        if view_type == "represent":
            if not view_column in dataframe.columns:
                raise ValueError("Unknown view column")
            if show is not None and show == "both":
                dataframe['mixed_name_column'] = dataframe[view_column].astype(str) + '_' + dataframe['name']
                view_column = "mixed_name_column"
            elif show is not None and show == "name":
                view_column = "name"
            data_fields = [x for x in dataframe.columns if x in MODEL_FIELDS]
            if len(data_fields) == 0:
                raise ValueError("Unknown data field")
            elif len(data_fields) > 1:
                warnings.warn("Received more than one data column, result truncated")
            data_field = data_fields[0]
            dataframe = dataframe.set_index([index_column, view_column])
            return dataframe[data_field].unstack(view_column).fillna(0)
        elif view_type == 'raw' or view_type is None:
            return dataframe
        warnings.warn("No view for this viewtype, original dataframe returned")
        return dataframe

    def _deserialize(self, obj, fields={}):
        """
        Функція десеріалізує об’єкт, приводячи поля в fields до рідних типів Python
        """
        datetime_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d'
        date_fields = ['date', 'date_from', 'date_to']
        for key, value in iteritems(obj):
            if key in date_fields and obj[key]:
                obj[key] = datetime.datetime.strptime(value, datetime_format)
            elif key in fields:
                try:
                    obj[key] = fields[key](obj[key])
                except TypeError:
                    pass
        return obj

    @_check_params
    def get_products_sale(self, categories=None,
                          shops=None,
                          products=None,
                          date_from=None,
                          date_to=None,
                          weekday=None,
                          interval="days",
                          by=None,
                          show="id",
                          view_type="represent"):
        """
        Parameters:
        ------------
        products: int,list
            id товару, або список з id по яких буде робитися вибірка.
        categories: int,list
            id категорії, або список з id по яких буде робитися вибірка
        shops: int,list
            id магазину, або список з id по яких буде робитися вибірка
        weekday:  int {понеділок - 0, неділя - 6}
            день тижня по якому буде робитися вибірка
        date_from: datetime
            початкова дата вибірки
        date_to: datetime
            кінцева дата вибірки
            Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
            Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
             або останій день відповідно існування магазину.
        interval: str,{"days","months","weeks","years", default: "days" }
            залежно від параметра, результат буде згруповано по днях, тижях, місяцях, або роках.
        by: str,
                    {"turnover": Оборот,
                    "qty": Кількість проданих товарів,
                    "receipts_qty": Кількість чеків,
                    "profit": прибуток,
                    "sold_product_value": собівартість проданих товарів,
                    "self_price_per_product": ціна за одиницю товару,
                    "price": середня ціна товару
            default: "turnover"}
            поле, по якому хочемо отримати результат вибірки.

        show: str,
                    {"name": <category_name> для назв колонок,
                     "id": <category_id> для назв колонок,
                     "both": <category_id>_<category_name> для назв колонок,
                     default: "name"

        Returns:
        ------------
            повертає об’єкт DataFrame з результатами вибірки
             _______________________________________
                     |product1|product2 |...productN|
            _______________________________________
             date1   |   by   |    by  |    by    |
             date2   |   by   |    by  |    by    |
             ...
             dateN   |   by   |    by  |    by    |

        Examples:
            dw = datawiz.DW()
            dw.get_products_sale(products = [2833024, 2286946, 'sum'],by='turnover',
                shops = [305, 306, 318, 321],
                date_from = datetime.date(2015, 8, 9),
                date_to = datetime.date(2015, 9, 9),
                interval = datawiz.WEEKS)
            Повернути дані обороту по товарах з id [2833024, 2286946], від 9-8-2015 до 9-9-2015
            по магазинах  [305, 306, 318, 321], згрупованні по тижнях
            Передавши параметр "sum" останнім елементом списку, отримаємо
            додаткову колонку з сумою відповідного показника
        """

        # Формуємо словник параметрів і отримуємо результат запиту по цих параметрах
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'products': products,
                  'categories': categories,
                  'select': by or ["turnover"],
                  'interval': interval,
                  'weekday': weekday,
                  'show': show
                  }

        result = self._post(GET_PRODUCTS_SALE_URI, data=params)["results"]
        # Якщо результат коректний, повертаємо DataFrame з результатом, інакше - пустий DataFrame
        if result:
            dataframe = pd.DataFrame.from_records(result)
            return self._prepare_df_view(dataframe, view_type,
                                         view_column="product",
                                         columns_order=by,
                                         show=show)
        return pd.DataFrame()

    @_check_params
    def get_categories_sale(self, categories=None,
                            shops=None,
                            date_from=None,
                            date_to=None,
                            weekday=None,
                            interval='days',
                            by=None,
                            show='name',
                            view_type='represent',
                            window=30,
                            per_shop=False
                            ):
        """
        Parameters:
        ------------
        categories: int,list
            id категорії, або список з id по яких буде робитися вибірка
        shops: int,list
            id магазину, або список з id по яких буде робитися вибірка
        weekday:  int {понеділок - 0, неділя - 6}
            день тижня по якому буде робитися вибірка
        date_from: datetime
            початкова дата вибірки
        date_to: datetime
            кінцева дата вибірки
            Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
            Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
             або останій день відповідно існування магазину.
        interval: str,{"days","months","weeks","years", default: "days" }
            залежно від параметра, результат буде згруповано по днях, тижях, місяцях, або роках.
        by: str,
                    {"turnover": Оборот,
                    "qty": Кількість проданих товарів,
                    "profit": прибуток,
                    "sold_product_value": собівартість проданих товарів,
                    "receipts_qty": кількість чеків
            default: "turnover"}
            поле, по якому хочемо отримати результат вибірки.
        show: str,
                    {"name": <category_name> для назв колонок,
                     "id": <category_id> для назв колонок,
                     "both": <category_id>_<category_name> для назв колонок,
                     default: "name"
        Returns:
        ------------
            повертає об’єкт DataFrame з результатами вибірки
             _______________________________________
                     |category1|category2 |...categoryN|
            _______________________________________
             date1   |   by   |    by  |    by    |
             date2   |   by   |    by  |    by    |
             ...
             dateN   |   by   |    by  |    by    |

        Examples
        ------------
            dw = datawiz.DW()
            dw.get_categories_sale(categories = [50599, 50600, "sum"],by='turnover',
                shops = [305, 306, 318, 321],
                date_from = datetime.date(2015, 8, 9),
                date_to = datetime.date(2015, 9, 9),
                interval = datawiz.WEEKS)
            Повернути дані обороту по категоріях з id [50599, 50600], від 9-8-2015 до 9-9-2015
            по магазинах  [305, 306, 318, 321], згрупованні по тижнях
            Передавши параметр "sum" останнім елементом списку, отримаємо
            додаткову колонку з сумою відповідного показника
        """

        # Формуємо словник параметрів і отримуємо результат запиту по цих параметрах
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'categories': categories,
                  'select': by or ["turnover"],
                  'interval': interval,
                  'weekday': weekday,
                  'window': window,
                  'show': show,
                  'per_shop': per_shop
                  }
        result = self._post(GET_CATEGORIES_SALE_URI, data=params)["results"]
        # Якщо результат коректний, повертаємо DataFrame з результатом, інакше - пустий DataFrame
        if result:
            dataframe = pd.DataFrame.from_records(result)
            return self._prepare_df_view(dataframe, view_type,
                                         view_column="category",
                                         columns_order=by,
                                         show=show)
        return pd.DataFrame()

    @_check_params
    def get_product(self, products=None, limit=None):
        """
        Parameters:
        ------------
        products: int, list, default: None
        Id товару, або список id

        Returns
        ------------
        Повертає товар, або список товарів в форматі


        {   "category_id": <category_id>,
            "category_name": <category_name>,
            "identifier": <product_identifier>,
            "product_id": <product_id>,
            "product_name": <product_name>,
            "unit_id": <unit_id>,
            "unit_name": <unit_name>,
            "barcode": <barcode>
        }

        Examples
        -----------
            dw = datawiz.DW()
            dw.get_product(products=2280001)
        """
        if products is not None and len(products) == 1:
            return self._get('%s/%s' % (GET_PRODUCT, products[0]))
        result = []

        page_size = 25000

        for r in self._get_raw_data(GET_PRODUCT,
                                    params={"limit": limit, "page_size": page_size},
                                    params_data={'products': products}):
            result.extend(r)

        return result

    def get_receipt(self, receipt_id):
        """
        Parameters:
        ------------
        receipt_id: int

        Returns
        ------------
            Повертає словник в форматі json
            {
                "date": <receipt_date>,
                    "cartitems": [{
                                "product_id": <product_id>,
                                "product_name": <product_name>,
                                "price": <price>,
                                "qty": <qty>,
                                "category_id": <category_id>,
                                "category_name": <category_name>
                                }],
                "total_price": <total_price>,
                "receipt_id": <receipt_id>,
                "loyalty_id": <loyalty_id>
            }

        Examples
        -----------
            dw = datawiz.DW()
            dw.get_receipt(19623631)
        """

        if not isinstance(receipt_id, int):
            raise TypeError("Incorrect param type")
        receipt = self._post(GET_RECEIPT, params={'receipt_id': receipt_id})
        if receipt:
            cartitems = [self._deserialize(x, fields={"price": float, 'qty': float}) for x in receipt['cartitems']]
            receipt = self._deserialize(receipt, fields={"turnover": float})
            receipt['cartitems'] = cartitems
        return receipt

    @_check_params
    def get_receipts(self,
                     products=None,
                     shops=None,
                     categories=None,
                     loyalty=None,
                     date_from=None,
                     date_to=None,
                     weekday=None,
                     hours=None,
                     type='full',
                     only_loyalty=False
                     ):
        """
            Parameters:
            ------------
            products: int,list
                id товару, або список з id по яких буде робитися вибірка
            shops: int,list
                id магазину, або список з id по яких буде робитися вибірка
            weekday:  int {понеділок - 0, неділя - 6}
                день тижня по якому буде робитися вибірка
            hours: int, list
                година або список годин, по яких буде робитися вибірка
            date_from: datetime
                початкова дата вибірки
            date_to: datetime
                кінцева дата вибірки
                Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
                Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
                 або останій день відповідно існування магазину.
            type: str, {'full', 'short', 'info'}
                Тип виводу продуктів в чеку
                default: 'full'
            loyalty: int, list
                id клієнта або список клієнтів програми лояльності
            only_loyalty: bool, default: False
                Якщо True, повертає тільки чеки клієнтів програми лояльності

            Returns:
            ------------
                Повертає список з чеками
                [
                    {
                     "receipt_id": <receipt_id>,
                     "date": <receipt_datetime>,
                     "cartitems": <cartitems>
                     "total_price": <total_price>
                    },
                     ....
                ],
                де cartitems залежить від аргумента type
                Для type = "full" :

                [
                    {
                        "product_id": <product_id>,
                        "product_name": <product_name>,
                        "category_id": <category_id>,
                        "category_name": <category_name>,
                        "qty": <qty>,
                        "price": <price>
                    },
                    {
                        "product_id": <product_id>,
                        "product_name": <product_name>,
                        "category_id": <category_id>,
                        "category_name": <category_name>,
                        "qty": <qty>,
                        "price": <price>
                    }
                    .....
                ]

                для type = "short"
                    [<product1_id>, <product2_id>, ... , <productN_id>]

                для type = "info" функція повертає результат в вигляді об’єкта DataFrame

                ------------------------------------------------------------------
                |    date   |     loyalty_id   |    receipt_id    |   turnover   |
                ------------------------------------------------------------------
                |   <date> |    <loyalty_id>  |    <receipt_id>  |   <turnover> |




            Examples
            -------------------
            dw = datawiz.DW()
            dw.get_receipts(categories = [50599, 50600],
                    shops = [305, 306, 318, 321],
                    date_from = datetime.date(2015, 8, 9),
                    date_to = datetime.date(2015, 9, 9),
                    type = "short")
                Отримати всі чеки які включають продукти, що належать категоріям [50599, 50600],
                по магазинах [305, 306, 318, 321]
                за період з 2015, 8, 9  - 2015, 9, 9 в скороченому вигляді
            """

        if not type in ['full', 'short', 'info']:
            raise TypeError("Incorrect param type")
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'categories': categories,
                  'products': products,
                  'weekday': weekday,
                  'hours': hours,
                  'type': type,
                  'loyalty': loyalty,
                  'only_loyalty': only_loyalty}
        # Отримуємо список чеків
        receipts = self._post(GET_RECEIPT, data=params)['results']
        result = []
        if type == 'info' and receipts:
            return pd.DataFrame.from_records(receipts)
        # Приводимо строкові значення в словнику json до рідних типів python
        for receipt in receipts:
            cartitems = receipt['cartitems']
            if type == 'full':
                cartitems = [self._deserialize(x, fields={"price": float, 'qty': float}) for x in cartitems]
            receipt = self._deserialize(receipt, fields={"turnover": float})
            receipt['cartitems'] = cartitems
            result.append(receipt)
        return result

    @_check_params
    def get_category(self, categories=None):
        """
            Parameters:
            ------------
            category: int, list, default: None
            id категорії, яку вибираємо, або список id.
            Якщо не заданий, береться категорія найвищого рівня


            Returns
            ------------
            Повертає об’єкт категорії або список об’єктів виду:

            {
                "children": [
                    {<child_category_id>: <child_category_name>}
                    ...
                    ],
                "category_id": <category_id>,
                "category_name": <category_name>,
                "products": [
                    {<product_id>: <product_name>}
                    ...
                    ],
                "parent_category_id": <parent_category_id>
                "parent_category_name": <parent_category_name>
            }


            Examples
            -----------
            dw = datawiz.DW()
            dw.get_category(categories = [51171, 51172])
        """
        if categories is not None and len(categories) == 1:
            return self._get('%s/%s' % (GET_CATEGORY, categories[0]))
        return self._get(GET_CATEGORY, data={'categories': categories})

    def search(self, query, by="product", level=None):
        """
            Parameters:
            ------------
            query: str
            Пошуковий запит

            by: str, {"category", "product",
                        default: "product"}
            Пошук по категоріям або по продуктам


            Returns
            ------------
            Повертає список з результатами пошуку

            [
                { <product_id>: <product_name> }
                { <product_id>: <product_name> }
                ...

            ]
            або
            [
                { <category_id>: <category_name> }
                { <category_id>: <category_name> }
                ...

            ]


        """
        if not isinstance(by, (str, unicode)):
            raise TypeError("Incorrect param type")
        if by not in ["product", "category", "barcode", "all"]:
            raise TypeError("Incorrect param type")
        params = {'q': query, 'select': by}
        if level is not None:
            params['level'] = level
        return dict(self._get(SEARCH, params=params)['results'])

    def get_shops(self):
        """
        Returns
        ----------
        Повертає список магазинів клієнта
        [ {
            '<shop_id>': {
                            "name": <shop_name>,
                            "area": <shop_area>,
                            "longitude": <shop_longitude>,
                            "latitude": <shop_latitude>,
                            "address": <shop_address>,
                            "open_date": <shop_open_date>

            }
            ...
        } ]


        """
        # отримуємо дані
        shops = dict(self._get(SHOPS)['results'])
        # Приводимо їх до рідних типів Python
        for shop_id, shop in iteritems(shops):
            shops[shop_id] = self._deserialize(shop, fields={"longitude": float, "latitude": float})
        return shops

    def get_client_info(self):
        """
        Returns
        ----------
        Повертає інформацію про клієнта
        {
            "shops": [
                        {"<shop_id>": "<shop_name>"},
                        ...
                     ],
            "name": <client_name>,
            "date_from": <date_from>,
            "date_to": <date_to>
        }
        """

        return self._deserialize(self._get(CLIENT), fields={'shops': dict})

    def raw_brands(self, chunk_size=10000, **kwargs):
        """
        Returns
        ----------
        Повертає список всіх брендів клієнта (Ітератор, де кожен елемент це масив)
            [
                {"brand_id": "<brand_id>", "name": "<brand_name>"},
                ...
            ]
        """
        kwargs.update({"page_size": chunk_size})
        return self._get_raw_data(BRANDS, params=kwargs)

    def raw_shops(self, **kwargs):
        """
        Returns
        ----------
        Повертає список всіх магазинів клієнта (Ітератор, де кожен елемент це масив)
            [
                {"shop_id": "<shop_id>", "name": "<shop_name>"},
                ...
            ]
        """
        return self._get_raw_data(API_SHOPS, params=kwargs)

    def raw_categories(self, chunk_size=10000, **kwargs):
        """
        Returns
        ----------
        Повертає список всіх категорій клієнта (Ітератор, де кожен елемент це масив)
            [
                {"category_id": "<category_id>", "name": "<category_name>", "parent_id": "<parent_id>"},
                ...
            ]
        """
        kwargs.update({"page_size": chunk_size})
        return self._get_raw_data(GET_RAW_CATEGORIES, params=kwargs)

    def raw_products(self, chunk_size=10000, **kwargs):
        """
            Returns
            ----------
            Повертає список всіх продуктів клієнта (Ітератор, де кожен елемент це масив)
        """
        kwargs.update({"page_size": chunk_size})
        return self._get_raw_data(GET_PRODUCT, params=kwargs)

    def _custom_load(self, url, **params):
        page = 1
        has_next = True
        while has_next:
            params.update({'page': page})
            data = self._post(url, data=params)
            results = data.get('results', {"table": [], "has_next": False})
            has_next = results.get("has_next", False)
            page += 1
            yield results["table"]

    @_check_params
    def raw_inventory(self, date_from=None, date_to=None, chunk_size=10000, **kwargs):
        """
            Returns
            ----------
            Повертає залишки клієнта за вибраний період (Ітератор, де кожен елемент це масив)
        """
        kwargs.update({"page_size": chunk_size, "date_from": date_from, "date_to": date_to})
        return self._custom_load(INVENTORY_DETAIL, **kwargs)

    @_check_params
    def sale_items(self,
                   date_from=None,
                   date_to=None,
                   chunk_size=10000,
                   **kwargs
                   ):
        kwargs.update({"page_size": chunk_size, "date_from": date_from, "date_to": date_to})
        return self._custom_load(RECEIPTS_DETAIL, **kwargs)

    @_check_params
    def promotion_access(self,
                         date_from=None,
                         date_to=None,
                         chunk_size=10000,
                         **kwargs
                         ):
        kwargs.update({"page_size": chunk_size, "date_from": date_from, "date_to": date_to})
        return self._custom_load(PROMOTION_DETAIL, **kwargs)

    @_check_params
    def get_pairs(self,
                  date_from=None,
                  date_to=None,
                  shops=None,
                  hours=None,
                  product_id=None,
                  category_id=None,
                  price_from=0,
                  price_to=10000,
                  pair_by='category',
                  week_day='all',
                  map=1,
                  show='id',
                  ):
        """
        Parameters:
        ------------
        date_from: datetime
        Початкова дата періоду побудови пар
        date_to: datetime
        Кінцева дата періоду побудови пар
        shops: int, list
        id магазину або список магазинів
        hours: list [<0...23>, <0...23>, ...]
        Години
        week_day:  int<0...6>, default: "all"
        День тижня
        product_id: int
        id продукта
        category_id: int
        id категорії
        price_from: int, defaul: 0
        Ціна від
        price_to: int, default: 10000
        Ціна до
        pair_by: str, ["category", "product"], default: "category"
        Побудова пар для категорій чи продуктів
        map: int, default: 1
        на якому рівні рахувати супутні товари
        show: str, ['id', 'name', 'both'], default: 'id'
        Показувати id, ім’я, або обидва параметри

        Returns
        ------------
        Повертає об’єкт DataFrame з результатами вибірки
        Для параметра show = "id"

            ------------------------------------------
            0name | 1name |...| Nname | <data columns> |
            -------------------------------------------
            <id> | <id>  |...| <id>  |     <data>     |

            ...
        Для параметра show = "both"

            ------------------------------------------
            0name | 0name_name |...| Nname | Nname_name | <data_columns> |
            -------------------------------------------
            <id> |    <name>  |...| <id>  |  <name>    |   <data>       |

        При pair_by = "category", функція будує пари для категорій (або категорії, указаної в category_id),
        pair_by = "product" - для продуктів (або продукта, указаного в product_id).

        Examples
        ------------
        dw = datawiz.DW()
        dw.get_pairs(date_from = datetime.date(2015, 10, 1),
                    date_to = datetime.date(2015, 10, 3),
                    category_id = 50601,
                    show = 'both')
        Побудувати пари за період 2015, 10, 1 - 2015, 10, 3 для категорії 50601,
        показати id та ім’я категорій

        """
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'price_from': price_from,
                  'price_to': price_to,
                  'shops': shops,
                  'hours': hours,
                  'weekday': week_day,
                  'pair_by': pair_by,
                  'product_id': product_id,
                  'category_id': category_id,
                  'map': map,
                  'show': show
                  }
        results = self._post(PAIRS, data=params)['results']
        if results:
            return pd.DataFrame.from_records(results)
        return pd.DataFrame()
        # if result:
        #     return pd.read_json(result)
        # return pd.DataFrame()

    def id2name(self, id_list, typ='category'):
        """
        Params
        ------------
        id_list: list [<int>, <int>, <int>, ...]
        Список id
        typ: str {'category', 'products'}, default: "category"
        Тип id (для категорій, чи продуктів)

        Returns
        ------------
        Повертає словник, де ключами є id, а значеннями імена
        {'<category_id>': <category_name>
            ...
        }
        або
        {'<product_id>': <product_name>}
        """
        # Перевіряємо аргументи на правильність
        if not typ in ['category', 'product']:
            raise TypeError("Incorrect param type")
        if not isinstance(id_list, list):
            raise TypeError("Incorrect param type")
        # Формуємо параметри і отримуємо результат запиту по цим параметрам
        # id_list = ','.join([str(x) for x in id_list])
        params = {'id_list': id_list,
                  'id_type': typ,
                  'function': 'id2name'}
        return dict(self._post(UTILS, data=params)['results'])

    def name2id(self, name_list, typ='category', level=None):
        """
        Params
        ------------
        name_list: list [<str>, <str>, <str>, ...]
        Список імен
        typ: str ['category', 'products'], default: "category"
        Тип імен (для категорій, чи продуктів)

        Returns
        ------------
        Повертає словник, де ключами є імена, а значеннями id
        {'<category_name>': <category_id>
            ...
        }
        або
        {'<product_name>': <product_id>
        ...
        }
        """

        # splitter = '%dsf^45%'
        # Перевіряємо аргументи на правильність
        if not typ in ['category', 'product']:
            raise TypeError("Incorrect param type")
        if not isinstance(name_list, list):
            raise TypeError("Incorrect param type")
        # Формуємо параметри і отримуємо результат запиту по цим параметрам
        params = {'name_list': name_list,
                  'id_type': typ,
                  'function': 'name2id',
                  'level': level
                  }
        return dict(self._post(UTILS, data=params)['results'])

    def get_parent(self, categories, level=1, type='category'):
        """
        Params
        ---------------
        categories: int, list
            id категорії або список id
        level: int
            рівень батьківської категорії
        type: str, {"category", "product"}, default: "category"
            Тип id (для категорій чи продуктів)
        Returns
        ---------------
        Повертає словник, де ключами є id категорії,
        а значеннями id  батьківської категорії

            {
                <category_id>: <parent_category_id>
                ...
            }

        Examples
        --------------
        dw = datawiz.DW()
        dw.get_parent([3445, 4123, 96660], level = 2)

        Отримати батьківські категорії 2-го рівня для категорій з id 3445, 4123, 96660
        """

        if not type in ['category', 'product']:
            raise TypeError("Incorrect param type")
        if isinstance(categories, int):
            categories = [categories]

        params = {'categories': categories,
                  'level': level,
                  'function': 'get_parent',
                  'id_type': type}
        return self._post(UTILS, data=params)['results']

    @_check_params
    def get_loyalty_customer(self,
                             date_from=None,
                             date_to=None,
                             shops=None,
                             name=None,
                             loyalty_id=None,
                             cardno=None,
                             type='loyalty_id'):
        """
        Params
        ------------
        date_from: date
            початкова дата вибірки
        date_to: date
            кінцева дата вибірки
        Якщо проміжок [date_from, date_to] не заданий, вибірка буде за весь час існування магазину.
        Якщо ж заданий тільки один з параметрів то замість іншого буде використанно перший
        або останій день відповідно існування магазину.
        shops: int, list
            id магазину або список id
        name: str, list
            ім’я клієнта або список імен
        loyalty_id: int, list
            id клієнта або список id
        cardno: int, list
            номер карти клієнта або список номерів
        type: str, {'loyalty_id', 'cardno', 'name'} , default: "loyalty_id"
            Вид інформації в першій колонці
        Returns
        -----------

        Повертає об’єкт DataFrame з результатами вибірки
        -----------------------------------------------------------------------------------------------------
                       |   last_visit  |  spend  |     number_visits     |   shop_name1    | shop_name2 ...  |
                        -------------------------------------------------------------------------------------
        |<loyalty_id > | <last_visit>  | <spend> | <number_visits_total> | <number_visits> | <number_visits> |
        |<loyalty_id>  | <last_visit>  | <spend> | <number_visits_total> | <number_visits> | <number_visits> |
        ...

        Examples
        -----------
        dw = datawiz.DW()
        dw.get_loyalty_customer(date_from = datetime.date(2015, 7, 8),
                                date_to = datetime.date(2015, 8, 8),
                                shops = [1234, 4545])

        Отримати дані по клієнтах програми лояльності для магазинів 1234, 4545
        за період 8-7-2015 - 8-8-2015
        """

        if not type in ['loyalty_id', 'name', 'cardno']:
            raise TypeError("Incorrect param type")

        params = {
            'date_from': date_from,
            'date_to': date_to,
            'shops': shops,
            'name': name,
            'loyalty_id': loyalty_id,
            'cardno': cardno,
            'type': type
        }
        result = self._post(GET_LOYALTY_CUSTOMER, data=params)['results']
        if not result:
            return pd.DataFrame()
        return pd.DataFrame.from_records(result)

    @_check_params
    def get_products_stock(self,
                           date_from=None,
                           date_to=None,
                           shops=None,
                           categories=None,
                           products=None,
                           show='id',
                           by=None,
                           view_type="represent"):
        """
        Parameters:
        ------------
        categories: int,list
            id категорії, або список з id по яких буде робитися вибірка
        products: int, list
            id продукта, або список з id по яких буде робитися вибірка
        shops: int,list
            id магазину, або список з id по яких буде робитися вибірка
        date_from: datetime
            початкова дата вибірки
        date_to: datetime
            кінцева дата вибірки
            Якщо заданий тільки date_to, вибірка буде проводитись тільки для date_to
                Якщо заданий тільки date_from, вибірка буде проводитися починаючи з date_from
        by: str,
                    {
                    "qty": Кількість товарів на залишку,
                    "stock_value": собівартість товарів на залишку,

            default: "qty"}
            поле, по якому хочемо отримати результат вибірки.
        show: str,
                    {"name": <product_name> для назв колонок,
                     "id": <product_id> для назв колонок,
                     "both": <product_id>_
                     <product_name> для назв колонок,
                     default: "id"
        Returns:
        ------------
            повертає об’єкт DataFrame з результатами вибірки
             _______________________________________
                     |product1|product2 |...productN|
            _______________________________________
             date1   |   by   |    by  |    by    |
             date2   |   by   |    by  |    by    |
             ...
             dateN   |   by   |    by  |    by    |

        Examples
        ------------
            dw = datawiz.DW()
            dw.get_products_stock(categories = [68805, 69607], by='stock_value',
				shops = [601, 641],
				date_from = datetime.date(2015, 8, 9),
				date_to = datetime.date(2015, 9, 9),
				)
			Повернути дані вартості товарів на залишку для товарів категорій з id [68805, 69607], від 9-8-2015 до 9-9-2015
			по магазинах  [601, 641],
        """

        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'categories': categories,
                  'products': products,
                  'show': show,
                  'select': ['stock_qty']}
        result = self._post(GET_PRODUCTS_STOCK, data=params)["results"]
        if result:
            dataframe = pd.DataFrame.from_records(result)
            return self._prepare_df_view(dataframe, view_type,
                                         view_column="product",
                                         columns_order=by,
                                         show=show)
        return pd.DataFrame()

    # @_check_params
    def get_products_inventory(self, date=None, shop_id=None, product_id=None, show_url=False):

        params = {'date': date,
                  'shop_id': shop_id,
                  'product_id': product_id,
                  'page_size': 100000}
        result = self._get(GET_PRODUCTS_INVENTORY, params=params)["results"]
        if result:
            dataframe = pd.DataFrame.from_records(result)
            if not show_url:
                columns = filter(lambda x: 'url' not in x, dataframe.columns)
                dataframe = dataframe[columns]
            return dataframe
        return pd.DataFrame()

    def get_api_receipts(self, date=None, shop_id=None, show_url=False):

        params = {'date': date, 'shop_id': shop_id, 'page_size': 100000}
        result = self._get(GET_API_RECEIPT, params=params)["results"]
        if result:
            dataframe = pd.DataFrame.from_records(result)
            if not show_url:
                columns = filter(lambda x: 'url' not in x, dataframe.columns)
                dataframe = dataframe[columns]
            return dataframe
        return pd.DataFrame()

    @_check_params
    def get_categories_stock(self,
                             date_from=None,
                             date_to=None,
                             shops=None,
                             categories=None,
                             show='id',
                             by=None,
                             view_type="represent"):
        """
        Parameters:
        ------------
        categories: int,list
            id категорії, або список з id по яких буде робитися вибірка
        shops: int,list
            id магазину, або список з id по яких буде робитися вибірка
        date_from: datetime
            початкова дата вибірки
        date_to: datetime
            кінцева дата вибірки
            Якщо заданий тільки date_to, вибірка буде проводитись тільки для конкретної дати
            Якщо заданий тільки date_from, вибірка буде проводитися починаючи з date_from
        by: str,
                    {
                    "qty": Кількість товарів на залишку,
                    "stock_value": собівартість товарів на залишку,

            default: "qty"}
            поле, по якому хочемо отримати результат вибірки.
        show: str,
                    {"name": <category_name> для назв колонок,
                     "id": <category_id> для назв колонок,
                     "both": <category_id>_
                     <category_name> для назв колонок,
                     default: "id"
        Returns:
        ------------
            повертає об’єкт DataFrame з результатами вибірки
             _______________________________________
                     |category1|category2 |...categoryN|
            _______________________________________
             date1   |   by   |    by  |    by    |
             date2   |   by   |    by  |    by    |
             ...
             dateN   |   by   |    by  |    by    |

        Examples
        ------------
            dw = datawiz.DW()
            dw.get_categories_stock(categories = [68805, 69607], by='stock_value',
                shops = [601, 641],
                date_from = datetime.date(2015, 8, 9),
                date_to = datetime.date(2015, 9, 9),
                )
            Повернути дані вартості товарів на залишку для категорій з id [68805, 69607], від 9-8-2015 до 9-9-2015
            по магазинах  [601, 641],
        """
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'categories': categories,
                  'show': show,
                  'select': by or ['stock_qty']}

        result = self._post(GET_CATEGORIES_STOCK, data=params)['results']
        if result:
            dataframe = pd.DataFrame.from_records(result)
            return self._prepare_df_view(dataframe, view_type,
                                         view_column="category",
                                         columns_order=by,
                                         show=show)
        return pd.DataFrame()

    @_check_params
    def get_lost_sales(self,
                       date_from=None,
                       date_to=None,
                       shops=None,
                       category=None,
                       ):
        """
        Parameters:
        ------------
        category: int
            id категорії
        shops: int,list
            id магазину, або список з id по яких буде робитися вибірка
        date_from: datetime
            початкова дата вибірки
        date_to: datetime
            кінцева дата вибірки

        Returns:
        ------------
            повертає об’єкт DataFrame з результатами вибірки
             _______________________________________
                             |Avg sales|Losing Days |losing turnover|Lost Sales Quantity|Product Name|
            _______________________________________
             <product_id>   |  <data> |  <data    |     <data>     |        <data>      |   <data>   |
             <product_id>   |  <data> |  <data    |     <data>     |        <data>      |   <data>   |
             ...
             <product_id>   |  <data> |  <data    |     <data>     |        <data>      |   <data>   |

        Examples
        ------------
            dw = datawiz.DW()
            dw.get_lost_sales(category = 68805,
                shops = [601, 641],
                date_from = datetime.date(2015, 8, 9),
                date_to = datetime.date(2015, 9, 9),
                )
            Повернути дані по товарних дірах для категорії з id 68805, від 9-8-2015 до 9-9-2015
            по магазинах  [601, 641],
        """
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'category': category}

        data = self._post(LOST_SALES, data=params)
        if not data['results']:
            return pd.DataFrame()
        return pd.DataFrame.from_records(data['results'])

    @_check_params
    def get_sales_plan(self,
                       date=None,
                       category=None,
                       shops=None,
                       by='qty',
                       show='name',
                       on='category'):

        """
        Parameters:
        ------------------
        date: datetime, str {"%Y-%m"},
        Період, по якому хочемо отримати результати
        category: int
        id категорії, для якої хочемо отримати результат
        shops: int, list
        id магазину, або список id, по яких буде робитись вибірка
        by: str {'qty': кількість продажів,
                'turnover': оборот,
                'receipts_qty': кількість чеків
                }
        тип таблиці
        show: str, {'id', 'name', 'both'}
        тип виводу для іменованих колонок
        on: str {'category', 'shops'}
        параметр визначає, як саме групувати результати (по категоріях чи магазинах)


        Returns
        ------------
        Повертає об’єкт DataFrame в форматі

        для on = "shops"

        diff    |   diff_percent  |  estimate |  predicted  |  real  |  shop   |
        ------------------------------------------------------------------------
        <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shop1> |
        <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shop2> |
        ...
        <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shopN> |



        для on = "category"

        category    |    diff    |   diff_percent  |  estimate |  predicted  |  real  |  shop   |
        ----------------------------------------------------------------------------------------
        <category1>  |  <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shop1> |
        <category2>  |  <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shop1> |
        <category1>  |  <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shop2> |
        <category2>  |  <data>  |      <data>    |   <data>  |    <data>   | <data>  | <shop2> |






        Examples
        -----------------
        dw = datawiz.DW()
        dw.get_sales_plan(category = 68805,
                shops = [601, 641],
                date = datetime.date(2015, 8, 1),
            )
        """

        params = {'date': date,
                  'category': category,
                  'shops': shops,
                  'select': by,
                  'on': on,
                  'show': show}

        result = self._post(SALES_PLAN, data=params)['results']
        if not result:
            return pd.DataFrame()

        return pd.DataFrame.from_records(result)

    @_check_params
    def get_sales(self,
                  date_from=None,
                  date_to=None,
                  sale_id=None,
                  shops=None):

        """
        Parameters
        --------------------
        date_from: datetime
        Початкова дата вибірки
        date_to: datetime
        Кінцева дата вибірки
        sale_id: int, list
        id акції, або список id

        Returns
        -------------------------
        Повертає об`єкт DataFrame в форматі


        date_from   |  date_to  |   profit   |  qty  |   receipts_qty  | sale_id  | turnover |
        --------------------------------------------------------------------------------------
        <date_from> | <date_to> | <profit>   | <qty> |  <receipts_qty> | <sale_id>| <turnover>
        <date_from> | <date_to> | <profit>   | <qty> |  <receipts_qty> | <sale_id>| <turnover>
        <date_from> | <date_to> | <profit>   | <qty> |  <receipts_qty> | <sale_id>| <turnover>

        Examples
        -----------------------
        dw = datawiz.DW()
        dw.get_sales(date_from = datetime.date(2015, 8, 9),
				date_to = datetime.date(2015, 9, 9)

		Повернути всі акції, що проходили в період з 9-8-2015  по  9-9-2015)




        """

        params = {'date_from': date_from,
                  'date_to': date_to,
                  'sale_id': sale_id,
                  'sale_shops': shops}
        result = self._post(SALES, data=params)['results']
        if not result:
            return pd.DataFrame()
        return pd.DataFrame.from_records(result)

    def get_sale_info(self, sale_id, shops=None):
        """
        Parameters
        -------------
        sale_id: int
        Id акції
        shops: int, list
        id магазину, або список id, для яких хочемо отримати
        результат

        Returns
        -------------
        Повертає об`єкт DataFrame в форматі

        Product Name|Product Price|Product price difference|...|turnover_diff|turnover_percent_diff
        --------------------------------------------------------------------------------------------
           <data>   |    <data>   |         <data>         |...|    <data>   |      <data>          |
           <data>   |    <data>   |         <data>         |...|    <data>   |      <data>          |
           <data>   |    <data>   |         <data>         |...|    <data>   |      <data>          |



        Examples
        --------------
        dw = datawiz.DW()
        dw.get_sale_info(45)

        Повернути інформацію для акції з id=45

        """

        params = {'sale_id': sale_id,
                  'sale_shops': shops}
        result = self._post(SALE_INFO, data=params)['results']
        if not result:
            return pd.DataFrame()
        return pd.DataFrame.from_records(result)

    @_check_params
    def get_sales_dynamics(self,
                           sale_id=None,
                           shops=None,
                           date_from=None,
                           date_to=None,
                           by='turnover',
                           show='name'):

        """
        Parameters
        -----------
        sale_id: int, list
        Id акції, або список id
        shops: int, list
        Id магазину, або список id
        date_from: datetime, str {%Y-%m-%d}
        Початкова дата вибірки
        date_to: datetime, str {%Y-%m-%d}
        Кінцева дата вибірки
        by: str, {'turnover', 'receipts_qty', default='turnover'}

        """

        params = {'sale_id': sale_id,
                  'sale_shops': shops,
                  'date_from': date_from,
                  'date_to': date_to,
                  'by': by,
                  'show': show}
        result = self._post(SALE_DYNAMICS, data=params)['results']
        if result:
            return pd.DataFrame.from_records(result)
        return pd.DataFrame()

    @_check_params
    def get_loyalty_sales(self,
                          shops=None,
                          date_from=None,
                          date_to=None,
                          ):

        """
        Parameters
        -----------
        shops: int, list
        Id магазину, або список id
        date_from: datetime, str {%Y-%m-%d}
        Початкова дата вибірки
        date_to: datetime, str {%Y-%m-%d}
        Кінцева дата вибірки

        """

        params = {
            'shops': shops,
            'date_from': date_from,
            'date_to': date_to
        }

        result = self._post(LOYALTY_SALES, data=params)['results']
        if not result:
            return pd.DataFrame()
        return pd.DataFrame.from_records(result)

    @_check_params
    def get_olap_report(self,
                        documents=None,
                        shops=None,
                        date_from=None,
                        date_to=None,
                        join=None):
        """
        Parameters
        -----------
        documents: {
            "<doc_type>": {
                "group_by": [<group_by_column>, ..],
                "agg": {
                    "<agg_column>": "<agg_func>",
                    ...,
                },
            ...
        }
            <doc_type>: purchases, inventory, receives, relocates, supplier_refunds, stocktaking, incoming, losses
            <group_by_column>: date, shop_id (shop_sender_id, shop_receiver_id для relocates), product_id
            <agg_column>: qty, price (original_price для inventory), total_price (stock_total_price для inventory), profit (для receipts)
            <agg_func>: sum, mean, max, min, count

        shops:
        Id магазину, або список id
        date_from: datetime, str {%Y-%m-%d}
        Початкова дата вибірки
        date_to: datetime, str {%Y-%m-%d}
        Кінцева дата вибірки
        join: bool
        Об'єднувати таблиці в одну

        """
        documents = documents or {}
        params = documents.copy()

        params.update({
            'shops': shops,
            'date_from': date_from,
            'date_to': date_to,
            'join': join or False
        })

        result = self._post(OLAP_REPORT, data=params)['results']
        return {document_type: pd.DataFrame.from_records(data) for document_type, data in result.items()}

    def _zipdir(self, path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file), file)

    def download_data(self, path=None):
        csv.register_dialect('unixpwd', delimiter=';', lineterminator='\n')
        if path is None:
            path = os.path.dirname(os.path.realpath(__file__))
        tmp_dir = os.path.join(path, 'tmp')
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)
        files = {'cashiers': ('cashiers', ['cashier_id', 'name']),
                 'shops': ('shops', ['shop_id', 'name', 'address', 'open_date', 'longitude', 'latitude']),
                 'terminals': ('terminals', ['terminal_id', 'shop_id', 'name']),
                 'units': ('units', ['unit_id', 'name']),
                 'products': ('products', ['product_id', 'barcode', 'name', 'category_id', 'unit_id']),
                 'clients': (
                     'loyalty', ['loyalty_id', 'cardno', 'client_name', 'client_birthday', 'is_male', 'discount']),
                 'categories': ('categories', ['category_id', 'name', 'parent_id']),
                 'prices': ('date-prices', ['shop_id', 'product_id', 'date', 'original_price', 'price']),
                 'inventory': (
                     'product-inventory',
                     ['shop_id', 'product_id', 'date', 'qty', 'original_price', 'stock_total_price']),
                 'receipts': ('core-cartitem',
                              ['shop_id', 'terminal_id', 'cashier_id', 'loyalty_id', 'receipt_id', 'date', 'product_id',
                               'price', 'qty', 'total_price'])}

        for file, data in iteritems(files):

            print('Donwloading %s' % file)
            self.logging.info('Donwloading %s' % file)
            with open(os.path.join(tmp_dir, '%s.csv' % file), 'w') as fh:
                writer = csv.DictWriter(fh, fieldnames=data[1], dialect='unixpwd')
                writer.writeheader()
                for items in self._get_raw_data(data[0]):
                    [writer.writerow(
                        dict((k, v.encode('utf-8') if isinstance(v, unicode) else v) for k, v in iteritems(x))) for x
                        in items]
                print('%s done' % file)
                self.logging.info('%s done!' % file)

        ziph = zipfile.ZipFile(os.path.join(path, 'archive-%s.zip') % datetime.datetime.now().strftime('%Y-%m-%d'), 'w')
        self._zipdir(tmp_dir, ziph)
        ziph.close()
        shutil.rmtree(tmp_dir)
        self.logging.info('All done!')
