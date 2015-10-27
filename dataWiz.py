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
MODEL_FIELDS = ['total_price', 'qty', 'receipts_qty', 'stock_qty']
TEST_KEY_ID = 'Sandbox'
TEST_SECRET = 'my secret key'
API_URL = 'http://test.datawiz.io/api/v1'
DAYS = 'days'
WEEKS = 'weeks'
MONTHS = 'months'
YEARS = 'years'
HEADERS = {'Host': 'test.datawiz.io', 'Accept': 'application/json', 'Date': "Thu, 22 Oct 2015 12:47:05 GMT"}
SIGNATURE_HEADERS = ['accept', 'date', 'host']
GET_PRODUCTS_SALE_URI = 'get_products_sale'



class APIGetError(Exception):
    pass

class DataWiz:
    """"
    Цей клас дозволяє здійснювати виклики функцій API
    """


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
                       'call': lambda x: x if x in range(7) else None}
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

    @_check_params
    def get_products_sale(self, categories=None,
                          shops = None,
                          products = None,
                          date_from = None,
                          date_to = None,
                          weekday = None,
                          interval = "days",
                          by = "total_price",):
        """
        :param shops: id магазину, або список id
        :param products: id продукта, або список id
        :param date_from: початкова дата вибірки
        :param date_to: кінцева дата вибірки
        Якщо проміжок [date_from, date_to] не заданий, вибірка буде до date_to, починаючи з date_from, або за весь час
        :param interval: [default: "days" ] залежно від параметра, результат буде згруповано по днях, тижях, місяцях, або роках. Доступні параметри "days", "weeks", "months", "years"
        :param by: [default: "total_price"] поле, по якому хочемо отримати результат вибірки. Доступні поля "total_price", "qty", "stock_qty", "receipts_qty"
        :param weekday: день тижня (понеділок - 0, неділя - 6)
        :return: повертає об’єкт DataFrame.
         _______________________________________
                 |product1|product2 |...productN|
        _______________________________________
         date1   |   by   |    by  |    by    |
         date2   |   by   |    by  |    by    |
         ...
         dateN   |   by   |    by  |    by    |
        """

        # Формуємо словник параметрів і отримуємо результат запиту по цих параметрах
        params = {'date_from': date_from,
                  'date_to': date_to,
                  'shops': shops,
                  'products': products,
                  'categories':  categories,
                  'select' : by,
                  'interval': interval,
                  'weekday': weekday}
        result = self._get(GET_PRODUCTS_SALE_URI, params = params)
        # Якщо результат коректний, повертаємо DataFrame з результатом, інакше - пустий DataFrame
        if result:
            return pd.read_json(result)
        return pd.DataFrame()