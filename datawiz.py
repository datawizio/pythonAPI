#!/usr/bin/env python
#coding:utf-8
# REQUIRES requests, httpsig, PyCrypto, pandas
import requests
from requests.exceptions import RequestException
from functools import wraps
from httpsig.requests_auth import HTTPSignatureAuth
import urllib
import pandas as pd
import datetime

INTERVALS = ['days', 'weeks', 'months', 'years']
MODEL_FIELDS = ['turnover', 'qty', 'receipts_qty', 'stock_qty',
                'profit', 'stock_value',
                'sold_product_value', 'self_price_per_product']
TEST_KEY_ID = 'test1@mail.com'
TEST_SECRET = 'test2@cbe47a5c9466fe6df05f04264349f32b'
API_URL = 'http://test.datawiz.io/api/v1'
DAYS = 'days'
WEEKS = 'weeks'
MONTHS = 'months'
YEARS = 'years'
HEADERS = {'Host': 'test.datawiz.io', 'Accept': 'application/json', 'Date': "Thu, 22 Oct 2015 12:47:05 GMT"}
SIGNATURE_HEADERS = ['accept', 'date', 'host']
GET_PRODUCTS_SALE_URI = 'get_products_sale'
GET_CATEGORIES_SALE_URI = 'get_categories_sale'
GET_PRODUCT = 'core-products/%s'
GET_RECEIPT = 'core-receipts'
GET_CATEGORY = 'core-categories'
SEARCH = 'search'
CLIENT = 'client'
SHOPS = 'core-shops'
PAIRS = 'pairs'
UTILS = 'utils'

class APIGetError(Exception):
    pass

class DW:


    def __init__(self, API_KEY = TEST_KEY_ID , API_SECRET = TEST_SECRET):
        # Ініціалізуємо екземпляр класу, якщо не отримали API_KEY i API_SECRET, використовуємо тестові параметри
        self.API_KEY, self.API_SECRET = API_KEY, API_SECRET

    def _check_params(func):
        """
        Функція-декоратор, приймає іменовані аргументи і звіряє їх з заданим шаблоном
        """
        def id_list(var):
            if isinstance(var, list):
                return splitter.join([str(x) for x in var])
            return var
        @wraps(func)
        def wrapper(self, **kwargs):

            # Отримуємо в kwargs всі іменовані аргументи функції, яку декоруємо
            for kwarg in kwargs:
                # Перевіряємо по шаблону, чи аргумент коректного типу
                if kwarg in params and isinstance(kwargs[kwarg], params[kwarg]['types']):
                    # Викликаємо задану в шаблоні функцію для обробки даних
                   kwargs[kwarg] = params[kwarg]['call'](kwargs[kwarg])
                elif kwarg in params and not isinstance(kwargs[kwarg], params[kwarg]['types']):
                    raise TypeError('Incorrect param type for <%s> '%i)
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
                       'call': lambda x: x},
                'date_to':
                      {'types': datetime.date,
                      'call': lambda x: x},
                'interval':
                      {'types': str,
                       'call': lambda x: x if x in INTERVALS else None},
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
                }
        return wrapper


    def _get(self, resource_url, params={}):
        """
        Функція підписує заголовки, указані в SIGNATURE_HEADERS, і відправляє запит до вказаного API resource_url,
        передаючи серверу параметри із params
        Повертає словник в форматі json
        """

        auth = HTTPSignatureAuth(key_id = self.API_KEY,
                    secret = self.API_SECRET,
                    algorithm = 'hmac-sha256',
                    headers = SIGNATURE_HEADERS)

        # Відсилаємо запит до api, параметри кодуємо функцією urlencode.
        # Особливість urlencode - кодує значення somevar = None в строку "somevar=None", тому замінюємо всі None на пусті значення
        try:
            response = requests.get('%s/%s/?%s'%(API_URL, resource_url, urllib.urlencode(params).replace('None', '')), auth = auth, headers = HEADERS)
        except RequestException, error:
            raise APIGetError("Error, while loading data. %s"%error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if response.status_code != requests.codes.OK:
            try:
                error = response.json().get('detail', '')
                raise APIGetError('Error, while loading data. %s'%error)
            #Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIGetError('%s %s'%(response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.text:
            return response.json()
        return {}
    def _post(self, resource_url, params={}):
        """
        Функція підписує заголовки, указані в SIGNATURE_HEADERS, і відправляє запит до вказаного API resource_url,
        передаючи серверу параметри із params
        Повертає словник в форматі json
        """

        auth = HTTPSignatureAuth(key_id = self.API_KEY,
                    secret = self.API_SECRET,
                    algorithm = 'hmac-sha256',
                    headers = SIGNATURE_HEADERS)

        # Відсилаємо запит до api, параметри кодуємо функцією urlencode.
        try:
            response = requests.post('%s/%s/'%(API_URL, resource_url), params = params, auth = auth, headers = HEADERS)
        except RequestException, error:
            raise APIGetError("Error, while loading data. %s"%error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if response.status_code != requests.codes.OK:
            try:
                error = response.json().get('detail', '')
                raise APIGetError('Error, while loading data. %s'%error)
            #Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIGetError('%s %s'%(response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.text:
            return response.json()
        return {}


    def _deserialize(self, obj, fields = {}):
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
            dw.get_products_sale(products = [2833024, 2286946],by='turnover',
				shops = [305, 306, 318, 321], 
				date_from = datetime.date(2015, 8, 9), 
				date_to = datetime.date(2015, 9, 9),
				interval = datawiz.WEEKS)
			Повернути дані обороту по товарах з id [2833024, 2286946], від 9-8-2015 до 9-9-2015
			по магазинах  [305, 306, 318, 321], згрупованні по тижнях
				
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
        result = self._get(GET_PRODUCTS_SALE_URI, params = params)
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
            dw.get_categories_sale(categories = [50599, 50600],by='turnover',
				shops = [305, 306, 318, 321],
				date_from = datetime.date(2015, 8, 9),
				date_to = datetime.date(2015, 9, 9),
				interval = datawiz.WEEKS)
			Повернути дані обороту по категоріях з id [50599, 50600], від 9-8-2015 до 9-9-2015
			по магазинах  [305, 306, 318, 321], згрупованні по тижнях

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
        result = self._get(GET_CATEGORIES_SALE_URI, params = params)
        # Якщо результат коректний, повертаємо DataFrame з результатом, інакше - пустий DataFrame
        if result:
            return pd.read_json(result)
        return pd.DataFrame()

    def get_product(self, product_id):
        """
        Parameters:
        ------------
        product_id: int

        Returns
        ------------
            Повертає словник в форматі json
        {   "category_id": <category_id>,
            "category_name": <category_name>,
            "identifier": <product_identifier>,
            "product_id": <product_id>,
            "product_name": <product_name>,
            "unit_id": <unit_id>,
            "unit_name": <unit_name>
        }

        Examples
        -----------
            dw = datawiz.DW()
            dw.get_product(2280001)
        """
        if not isinstance(product_id, int):
            raise TypeError("Incorrect param type")
        return self._get(GET_PRODUCT%product_id)

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
                "receipt_id": <receipt_id>
            }

        Examples
        -----------
            dw = datawiz.DW()
            dw.get_receipt(19623631)
        """

        if not isinstance(receipt_id, int):
            raise TypeError("Incorrect param type")
        receipt =  self._get('%s/%s'%(GET_RECEIPT, receipt_id))
        if receipt:
            cartitems = [self._deserialize(x, fields = {"price": float, 'qty': float}) for x in receipt['cartitems']]
            receipt = self._deserialize(receipt, fields = {"turnover": float})
            receipt['cartitems'] = cartitems
        return receipt


    @_check_params
    def get_receipts(self, categories=None,
                            products=None,
                            shops = None,
                            date_from = None,
                            date_to = None,
                            weekday = None,
                            type = 'full'):
        """
            Parameters:
            ------------
            products: int,list
                id товару, або список з id по яких буде робитися вибірка
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
            type: str, {'full', 'short'}
                Тип виводу продуктів в чеку
                default: 'full'

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

        if not type in ['full', 'short']:
            raise TypeError("Incorrect param type")
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'categories':  categories,
                  'products': products,
                  'weekday': weekday,
                  'type': type}
        #Отримуємо список чеків
        receipts = self._get(GET_RECEIPT, params = params)
        result = []
        #Приводимо строкові значення в словнику json до рідних типів python
        for receipt in receipts:
            cartitems =  [self._deserialize(x, fields = {"price": float, 'qty': float}) for x in receipt['cartitems']]
            receipt = self._deserialize(receipt, fields = {"turnover": float})
            receipt['cartitems'] = cartitems
            result.append(receipt)
        return result
    def get_category(self, category_id = None):
        """
            Parameters:
            ------------
            category_id: int, default: None
            id категорії, яку вибираємо. Якщо не заданий, береться категорія найвищого рівня

            Returns
            ------------
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
            dw.get_category(51171)
        """
        if not isinstance(category_id, (int, type(None))):
            raise TypeError("Incorrect param type")
        return  self._get(GET_CATEGORY, params = {'category':category_id})

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

        shops = self._get(SHOPS)['results']
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

        return  self._deserialize(self._get(CLIENT), fields = {'shops': dict})
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
        початкова дата вибірки
        date_to: datetime
        кінцева дата вибірки
        shops: int, list
        id магазину або список магазинів
        hours: list [<0...23>, <0...23>, ...]
        Години
        week_day: int, str, default: "all"
        День тижня
        product_id: int
        Id продукта
        category_id: int
        id категорії
        price_from: int, defaul: 0

        price_to: int, default: 10000

        pair_by: str, ["category", "product"], default: "category"

        map: int, default: 1
        show: str, ['id', 'name', 'both'], default: 'id'

        Returns
        ------------
        Повертає об’єкт DataFrame з результатами вибірки

        Examples
        ------------
        dw = datawiz.DW()
        dw.get_pairs(date_from = datetime.date(2015, 10, 1),
                    date_to = datetime.date(2015, 10, 3),
                    category_id = 50601,
                    show = 'both')
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
        results = self._get(PAIRS, params = params)['results']
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
        typ: str ['category', 'products'], default: "category"
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
        id_list = ','.join([str(x) for x in id_list])
        params = {'id_list': id_list,
                  'id_type': typ,
                  'function': 'id2name'}
        return dict(self._post(UTILS, params = params)['results'])

    def name2id(self, name_list, typ = 'category'):
        """
        Params
        ------------
        name_list: list [<int>, <int>, <int>, ...]
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

        splitter = '%dsf^45%'
        #Перевіряємо аргументи на правильність
        if not typ in ['category', 'product']:
            raise TypeError("Incorrect param type")
        if not isinstance(name_list, list):
            raise TypeError("Incorrect param type")
        #Формуємо параметри і отримуємо результат запиту по цим параметрам
        name_list = splitter.join(name_list)
        params = {'name_list': name_list,
                  'id_type': typ,
                  'function': 'name2id'}
        return dict(self._post(UTILS, params = params)['results'])
