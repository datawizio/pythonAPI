#!/usr/bin/env python
# coding:utf-8
# REQUIRES requests, httpssig, PyCrypto

from __future__ import print_function
import tempfile, os, copy
import requests, json
from requests.exceptions import RequestException
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import logging
import datetime

try:
    from urllib.parse import urlencode
except ImportError:
    # Python 2
    from urllib import urlencode


logging.basicConfig(
    format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level=logging.INFO
)

TEST_USERNAME = 'test1@mail.com'
TEST_PASSWORD = '1qaz'
CLIENT_ID = "qYmlfNCjNwDu7p6PdQGTDTsDI6wDmxP2bJXCl3hc"
CLIENT_SECRET = "HoQuYukvjCFB9G4hCZABFF7ryL10J9lT9QQsQsgDP21EdMs7JVvsdiN2e1UuosbWl90St4nMiTPrgOj1kSCWD3uOfjmqUnjXKkVV3xVZtHGJlJiBC6VXLKLr3js339l1"
HEADERS = {'Host': 'api.datawiz.io', 'Accept': 'application/json', 'Date': "Tue, 10 Nov 2015 18:11:05 GMT",
           'Content-Type': 'application/json'}
API_URL = 'https://api.datawiz.io/api/v1'
# DEFAULT_HOST = 'bi.datawiz.io'
DEFAULT_HOST = 'api.datawiz.io'
FAILED_FILE = '%s_failed.csv'


class APIGetError(Exception):
    pass


class APIUploadError(Exception):
    pass


class APIAuthError(Exception):
    pass


class Auth:
    def __init__(self, API_KEY=None, API_SECRET=None, HOST=None, log=logging, use_tmp_auth=True):
        # Ініціалізуємо екземпляр класу, якщо не отримали API_KEY i API_SECRET, використовуємо тестові параметри
        self.HEADERS = HEADERS
        self.API_URL = API_URL
        if API_KEY is None:
            self.API_KEY, self.API_SECRET = TEST_USERNAME, TEST_PASSWORD
        else:
            self.API_KEY, self.API_SECRET = API_KEY, API_SECRET
        self._set_host(HOST)
        self.use_tmp_auth = use_tmp_auth
        self.access_data = self._load_access_data()
        self.client = self.load_client()
        self.logging = log

    def _get_tmp_file_path(self):
        temp_dir = os.path.join(tempfile.gettempdir(), "dwapi")
        temp_file = os.path.join(temp_dir, "data.csv")
        if not os.path.isdir(temp_dir):
            os.mkdir(temp_dir)
        if not os.path.isfile(temp_file):
            open(temp_file, 'w').close()
        return temp_file

    def _load_access_data(self):
        temp_file = self._get_tmp_file_path()
        try:
            data = json.load(open(temp_file))
        except Exception:
            data = {}
        if not self.HEADERS["Host"] in data or data.get('token_date') != str(
                datetime.datetime.now().date()) or not self.use_tmp_auth:
            data[self.HEADERS["Host"]] = {}
        return data

    def _write_access_data(self):
        self.access_data['token_date'] = str(datetime.datetime.now().date())
        temp_file = self._get_tmp_file_path()
        try:
            json.dump(self.access_data, open(temp_file, "w"))
        except Exception as e:
            print(e)

    def _token_update_handler(self, token):
        self.access_data[self.HEADERS["Host"]][self.API_KEY] = token
        self._write_access_data()

    def load_client(self):
        if self.API_KEY in self.access_data[self.HEADERS["Host"]]:
            token = self.access_data[self.HEADERS['Host']][self.API_KEY]
        else:
            if self.API_SECRET is None:
                raise APIAuthError("Refresh token is expired. To obtain new token, please, specify API SECRET argument")
            oauth = OAuth2Session(client=LegacyApplicationClient(client_id=CLIENT_ID))
            token = oauth.fetch_token(token_url="https://%s/%s/" % (self.HEADERS['Host'], "api/o/token"),
                                      username=self.API_KEY,
                                      password=self.API_SECRET,
                                      client_id=CLIENT_ID,
                                      client_secret=CLIENT_SECRET)
            self._token_update_handler(token)

        client = OAuth2Session(CLIENT_ID, token=token,
                               auto_refresh_kwargs={"client_id": CLIENT_ID,
                                                    "client_secret": CLIENT_SECRET},
                               auto_refresh_url="https://%s/%s/" % (self.HEADERS['Host'], "api/o/token"),
                               token_updater=self._token_update_handler)
        # client = requests.Session()
        # client.auth = httpsBasicAuth(self.API_KEY, self.API_SECRET)
        return client

    def _to_csv(self, data, filename):
        fh = open(filename, 'a+')
        for item in data:
            line = ';'.join([str(x) if x is not None else '' for x in item.values()])
            fh.write(line + '\n')
        fh.close()

    def _get(self, resource_url, params=None, data={}):
        """
        Функція підписує заголовки, указані в SIGNATURE_HEADERS, і відправляє запит до вказаного API resource_url,
        передаючи серверу параметри із params
        Повертає словник в форматі json
        """

        # Відсилаємо запит до api, параметри кодуємо функцією urlencode.
        # Особливість urlencode - кодує значення somevar = None в строку "somevar=None",
        # тому замінюємо всі None на пусті значення
        params = params or {}
        try:
            response = self.client.get(
                '%s/%s/?%s' % (self.API_URL, resource_url, urlencode(params).replace('None', '')),
                headers=self.HEADERS,
                data=json.dumps(data))
        except RequestException as error:
            raise APIGetError("Error, while loading data. %s" % error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if not response.status_code in [requests.codes.OK, requests.codes.CREATED]:
            try:
                error = response.json().get('detail', '')
                raise APIGetError('Error, while loading data. %s' % error)
            # Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIGetError('%s %s' % (response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.content:
            return response.json()
        return {}

    def _post(self, resource_url, params=None, data={}, chunk=False):
        """
        Функція підписує заголовки, указані в SIGNATURE_HEADERS, і відправляє запит до вказаного API resource_url,
        передаючи серверу параметри із params
        Повертає словник в форматі json
        """
        headers = self.HEADERS
        headers['content-type'] = "application/json"
        params = params or {}

        # Відсилаємо запит до api, параметри кодуємо функцією urlencode.
        try:
            response = self.client.post(
                '%s/%s/?%s' % (self.API_URL, resource_url, urlencode(params).replace('None', '')),
                data=json.dumps(data), headers=headers)

        except RequestException as error:
            raise APIUploadError("Error, while loading data. %s" % error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if not response.status_code in [requests.codes.OK, requests.codes.CREATED]:
            try:
                error = response.json()
                # print error
                # Якщо data - це чанк, виду [obj, obj, ...]
                if chunk and isinstance(error, list):
                    # Вичисляємо список індексів елементів чанку, які викликали помилку
                    failed_elements = [error.index(x) for x in error if x]

                    # Формуємо чанк, який не буде викликати помилку на сервері
                    data = [x for x in data if data.index(x) not in failed_elements]
                    failed_elements = [x for x in error if error.index(x) in failed_elements]
                    # self.logging.error(resource_url.upper()+' '+str(failed_elements))
                    # Відправляємо сформований чанк на сервер
                    self.client.post('%s/%s/' % (API_URL, resource_url), data=json.dumps(data), headers=headers)
                    # Повертаємо індекси невірних елементів, для подальшої обробки, або виводу користувачу
                    return failed_elements
                raise APIUploadError('Error, while loading data. %s' % str(error.get('detail', '')))
            # Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIUploadError('%s %s' % (response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.content and not chunk:
            # print response.json()
            return response.json()
        return {}

    def _put(self, resource_url, params={}, data={}):

        """
        Функція підписує заголовки, указані в SIGNATURE_HEADERS, і відправляє запит до вказаного API resource_url,
        передаючи серверу параметри із params
        Повертає словник в форматі json
        """

        # Відсилаємо запит до api, параметри кодуємо функцією urlencode.
        try:
            response = self.client.put('%s/%s/' % (self.API_URL, resource_url), params=params, data=json.dumps(data),
                                       headers=self.HEADERS)
        except RequestException as error:
            raise APIUploadError("Error, while loading data. %s" % error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if not response.status_code in [requests.codes.OK, requests.codes.CREATED]:
            try:
                error = response.json().get('detail', '')
                raise APIGetError('Error, while loading data. %s' % error)
            # Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIUploadError('%s %s' % (response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.text:
            return response.json()
        return {}

    def _options(self, resource_url):
        try:
            response = self.client.options('%s/%s/' % (self.API_URL, resource_url), headers=self.HEADERS)
        except RequestException as error:
            raise APIUploadError("Error, while loading data. %s" % error)
        return response.json()

    def _set_host(self, host=None):
        if host is None:
            host = DEFAULT_HOST
        self.HEADERS['Host'] = host
        # self.API_URL = 'http://%s/api/v1' % host
        self.API_URL = 'https://%s/api/v1' % host
        return True

    def unstack_df(self, df, by, show):
        if df.empty:
            return df
        cols = list(df.columns)
        cols.pop(cols.index(by))
        group_cols = cols[:]
        cols.pop(cols.index('date'))
        sum_series = None
        if 'sum' in df.columns:
            group_cols.pop(group_cols.index('sum'))
            cols.pop(cols.index('sum'))
            sum_series = df.set_index('date')['sum'].to_frame()
        col_id = cols[0]
        if show == 'both':
            if len(cols) > 1:
                cols.pop(cols.index(cols[0]))
            col_id = cols[0]
        df = df.groupby(group_cols).agg('sum')
        df = df[by].unstack(col_id).fillna(0)

        if type(sum_series) == type(df):
            df = df.join(sum_series, how='inner')
        return df

    def generate_secret(self, email, password):
        self.API_KEY, self.API_SECRET = email, password
        self.load_client()
        return {"API_KEY": email,
                "API_SECRET": password}
