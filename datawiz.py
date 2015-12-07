#!/usr/bin/env python
#coding:utf-8

import datetime
import pandas as pd
from datawiz_auth import Auth
from functools import wraps

INTERVALS = ['days', 'weeks', 'months', 'years']
MODEL_FIELDS = ['turnover', 'qty', 'receipts_qty', 'stock_qty',
                'profit', 'stock_value',
                'sold_product_value', 'self_price_per_product']
DAYS = 'days'
WEEKS = 'weeks'
MONTHS = 'months'
YEARS = 'years'
GET_PRODUCTS_SALE_URI = 'get_products_sale'
GET_CATEGORIES_SALE_URI = 'get_categories_sale'
GET_PRODUCT = 'core-products'
GET_RECEIPT = 'core-receipts'
GET_CATEGORY = 'core-categories'
GET_LOYALTY_CUSTOMER = 'get_loyalty_customer'
SEARCH = 'search'
CLIENT = 'client'
SHOPS = 'core-shops'
PAIRS = 'pairs'
UTILS = 'utils'


class DW(Auth):

    def _check_params(func):
        """
        Функція-декоратор, приймає іменовані аргументи і звіряє їх з заданим шаблоном
        """
        def id_list(var):
            if isinstance(var, list):
                return var#splitter.join([str(x) for x in var])
            return [var]
        @wraps(func)
        def wrapper(self, **kwargs):

            # Отримуємо в kwargs всі іменовані аргументи функції, яку декоруємо
            for kwarg in kwargs:
                # Перевіряємо по шаблону, чи аргумент коректного типу
                if kwarg in params and isinstance(kwargs[kwarg], params[kwarg]['types']):
                    # Викликаємо задану в шаблоні функцію для обробки даних
                   kwargs[kwarg] = params[kwarg]['call'](kwargs[kwarg])
                elif kwarg in params and not isinstance(kwargs[kwarg], params[kwarg]['types']):
                    raise TypeError('Incorrect param type for <%s> '%kwarg)
            return func(self, **kwargs)
        splitter = ','
        # Шаблони для змінних - в types допустимі типи, в call функція обробки данних змінної
        params = {'shops':
                      {'types':(int, list),
                       'call': id_list},
                  'categories':
                      {'types':(int, list),
                       'call': id_list},
                  'products':
                      {'types':(int, list),
                       'call': id_list},
                  'date_from':
                      {'types': datetime.date,
                       'call': lambda x: str(x)},
                  'date_to':
                      {'types': datetime.date,
                      'call': lambda x: str(x)},
                  'interval':
                      {'types': str,
                       'call': lambda x: x if x in INTERVALS else None},
                  'loyalty':
                      {'types': (int, list),
                       'call': id_list},
                  'by':
                      {'types': str,
                       'call': lambda x: x if x in MODEL_FIELDS else None},
                  'weekday':
                      {'types': int,
                       'call': lambda x: x if x in range(7) else None},
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
                  'name': {'types': (str, list),
                           'call': id_list},
                  'loyalty_id': {'types': (int, list),
                                 'call': id_list}
                }
        return wrapper

    def _deserialize(self, obj, fields={}):
        """
        Функція десеріалізує об’єкт, приводячи поля в fields до рідних типів Python
        """
        datetime_format = '%Y-%m-%d %H:%M:%S'
        date_format = '%Y-%m-%d'
        date_fields = ['date', 'date_from', 'date_to']
        for key, value in obj.iteritems():
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
                          shops = None,
                          products = None,
                          date_from = None,
                          date_to = None,
                          weekday = None,
                          interval = "days",
                          by = "turnover",
                          show = "name"):
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
                    "stock_qty": Кількість товарів на залишку,
                    "receipts_qty": Кількість чеків,
                    "profit": прибуток,
                    "stock_value": собівартість товарів на залишку,
                    "sold_product_value": собівартість проданих товарів,
                    "self_price_per_product": ціна за одиницю товару
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
                  'categories':  categories,
                  'select' : by,
                  'interval': interval,
                  'weekday': weekday,
                  'show': show
                  }
        result = self._get(GET_PRODUCTS_SALE_URI, data = params)
        # Якщо результат коректний, повертаємо DataFrame з результатом, інакше - пустий DataFrame
        if result:
            return pd.read_json(result)
        return pd.DataFrame()

    @_check_params
    def get_categories_sale(self, categories=None,
                            shops = None,
                            date_from = None,
                            date_to = None,
                            weekday = None,
                            interval = 'days',
                            by = 'turnover',
                            show = 'name'):
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
                    "stock_qty": Кількість товарів на залишку,
                    "profit": прибуток,
                    "stock_value": собівартість товарів на залишку,
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
                  'categories':  categories,
                  'select' : by,
                  'interval': interval,
                  'weekday': weekday,
                  'show': show}
        result = self._get(GET_CATEGORIES_SALE_URI, data = params)
        # Якщо результат коректний, повертаємо DataFrame з результатом, інакше - пустий DataFrame
        if result:
            return pd.read_json(result)
        return pd.DataFrame()


    @_check_params
    def get_product(self, products=None):
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
            return self._get('%s/%s'%(GET_PRODUCT, products[0]))
        return self._get(GET_PRODUCT, data = {'products': products})

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
        receipt =  self._get(GET_RECEIPT, params = {'receipt_id': receipt_id})
        if receipt:
            cartitems = [self._deserialize(x, fields = {"price": float, 'qty': float}) for x in receipt['cartitems']]
            receipt = self._deserialize(receipt, fields = {"turnover": float})
            receipt['cartitems'] = cartitems
        return receipt


    @_check_params
    def get_receipts(self,
                            products=None,
                            shops = None,
                            categories = None,
                            loyalty = None,
                            date_from = None,
                            date_to = None,
                            weekday = None,
                            hours = None,
                            type = 'full',
                            only_loyalty = False
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
                  'loyalty':loyalty,
                  'only_loyalty':only_loyalty}
        # Отримуємо список чеків
        receipts = self._get(GET_RECEIPT, data = params)['results']
        result = []
        if type == 'info' and receipts:
            return pd.DataFrame.from_records(receipts)
        # Приводимо строкові значення в словнику json до рідних типів python
        for receipt in receipts:
            cartitems = receipt['cartitems']
            if type == 'full':
                cartitems =  [self._deserialize(x, fields = {"price": float, 'qty': float}) for x in cartitems]
            receipt = self._deserialize(receipt, fields = {"turnover": float})
            receipt['cartitems'] = cartitems
            result.append(receipt)
        return result

    @_check_params
    def get_category(self, categories = None):
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
            return self._get('%s/%s'%(GET_CATEGORY, categories[0]))
        return self._get(GET_CATEGORY, data = {'categories': categories})

    def search(self, query, by = "product"):
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

        if not by in ["product", "category"]:
            raise TypeError("Incorrect param type")
        return dict(self._get(SEARCH, params = {'q': query, 'by': by})['results'])

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
        #отримуємо дані
        shops = dict(self._get(SHOPS)['results'])
        #Приводимо їх до рідних типів Python
        for shop_id, shop in shops.iteritems():
            shops[shop_id] = self._deserialize(shop, fields = {"longitude": float, "latitude": float})
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

        return self._deserialize(self._get(CLIENT), fields = {'shops': dict})

    @_check_params
    def get_pairs(self,
                  date_from = None,
                  date_to = None,
                  shops = None,
                  hours = None,
                  product_id = None,
                  category_id = None,
                  price_from = 0,
                  price_to = 10000,
                  pair_by = 'category',
                  week_day = 'all',
                  map = 1,
                  show ='id',
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
        results = self._get(PAIRS, data = params)['results']
        if results:
            return pd.read_json(results)
        return pd.DataFrame()
        # if result:
        #     return pd.read_json(result)
        # return pd.DataFrame()
    def id2name(self, id_list, typ = 'category'):
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
        #Перевіряємо аргументи на правильність
        if not typ in ['category', 'product']:
            raise TypeError("Incorrect param type")
        if not isinstance(id_list, list):
            raise TypeError("Incorrect param type")
        #Формуємо параметри і отримуємо результат запиту по цим параметрам
        # id_list = ','.join([str(x) for x in id_list])
        params = {'id_list': id_list,
                  'id_type': typ,
                  'function': 'id2name'}
        return dict(self._post(UTILS, data = params)['results'])

    def name2id(self, name_list, typ = 'category'):
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
                  'function': 'name2id'}
        return dict(self._post(UTILS, data = params)['results'])


    def get_parent(self, categories, level = 1, type='category'):
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
        return self._post(UTILS, data = params)['results']

    @_check_params
    def get_loyalty_customer(self,
                             date_from = None,
                             date_to = None,
                             shops = None,
                             name = None,
                             loyalty_id = None,
                             cardno = None,
                             type = 'loyalty_id'):
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
        result = self._get(GET_LOYALTY_CUSTOMER, data = params)['results']
        if not result:
            return pd.DataFrame()
        return pd.read_json(result)

    def get_tasks(self):
        pass