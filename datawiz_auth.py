#!/usr/bin/env python
#coding:utf-8
# REQUIRES requests, httpsig, PyCrypto


import requests, json
from requests.exceptions import RequestException
from httpsig.requests_auth import HTTPSignatureAuth
import urllib

TEST_KEY_ID = 'test1@mail.com'
TEST_SECRET = 'test2@cbe47a5c9466fe6df05f04264349f32b'
HEADERS = {'Host': 'test.datawiz.io', 'Accept': 'application/json', 'Date': "Tue, 10 Nov 2015 18:11:05 GMT", 'Content-Type':'application/json'}
SIGNATURE_HEADERS = ['accept', 'date', 'host']
# API_URL = 'http://dwappserver1.cloudapp.net/api/v1'
API_URL = 'http://test.datawiz.io/api/v1'
FAILED_FILE = '%s_failed.csv'

class APIGetError(Exception):
    pass

class APIUploadError(Exception):
    pass

class Auth:

    def __init__(self, API_KEY = TEST_KEY_ID , API_SECRET = TEST_SECRET):
        # Ініціалізуємо екземпляр класу, якщо не отримали API_KEY i API_SECRET, використовуємо тестові параметри
        self.API_KEY, self.API_SECRET = API_KEY, API_SECRET

    def _to_csv(self, data, filename):
        fh = open(filename, 'a+')
        for item in data:
            line = ';'.join([str(x) if x is not None else '' for x in item.values()])
            fh.write(line+'\n')
        fh.close()
    def _get(self, resource_url, params={}, data = {}):
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
            response = requests.get('%s/%s/?%s'%(API_URL, resource_url, urllib.urlencode(params).replace('None', '')),
                                    auth = auth,
                                    headers = HEADERS,
                                    data=json.dumps(data))
        except RequestException, error:
            raise APIGetError("Error, while loading data. %s"%error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if not response.status_code in [requests.codes.OK, requests.codes.CREATED]:
            try:
                error = response.json().get('detail', '')
                raise APIGetError('Error, while loading data. %s'%error)
            # Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIGetError('%s %s'%(response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.text:
            return response.json()
        return {}

    def _post(self, resource_url, params={}, data = {}, chunk = False):
        """
        Функція підписує заголовки, указані в SIGNATURE_HEADERS, і відправляє запит до вказаного API resource_url,
        передаючи серверу параметри із params
        Повертає словник в форматі json
        """
        signature_headers = ['accept', 'date', 'host']
        headers = HEADERS
        headers['content-type'] = "application/json"
        auth = HTTPSignatureAuth(key_id = self.API_KEY,
                    secret = self.API_SECRET,
                    algorithm = 'hmac-sha256',
                    headers = signature_headers)

        # Відсилаємо запит до api, параметри кодуємо функцією urlencode.
        try:
            response = requests.post('%s/%s/'%(API_URL, resource_url), data = json.dumps(data),  auth = auth, headers = headers)
        except RequestException, error:
            raise APIUploadError("Error, while loading data. %s"%error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if not response.status_code in [requests.codes.OK, requests.codes.CREATED]:
            try:
                error = response.json()
                print error
                # print error
                # Якщо data - це чанк, виду [obj, obj, ...]
                if chunk and isinstance(error, list):
                    # Вичисляємо список індексів елементів чанку, які викликали помилку
                    failed_elements = [error.index(x) for x in error if x!={}]
                    # Формуємо чанк, який не буде викликати помилку на сервері
                    data = [x for x in data if data.index(x) not in failed_elements]
                    # Відправляємо сформований чанк на сервер
                    requests.post('%s/%s/'%(API_URL, resource_url), data = json.dumps(data),  auth = auth, headers = headers)
                    # Повертаємо індекси невірних елементів, для подальшої обробки, або виводу користувачу
                    return failed_elements
                raise APIUploadError('Error, while loading data. %s'%str(error.get('detail', '')))
            # Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIUploadError('%s %s'%(response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.text and not chunk:
            return response.json()
        return {}

    def _put(self, resource_url, params={}, data = {}):

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
            response = requests.put('%s/%s/'%(API_URL, resource_url), params = params, data = json.dumps(data),  auth = auth, headers = HEADERS)
        except RequestException, error:
            raise APIUploadError("Error, while loading data. %s"%error)

        # Якщо сервер повертає помилку, виводимо її
        # Формат відповіді сервера {'detail':'error message'}
        if not response.status_code in [requests.codes.OK, requests.codes.CREATED]:
            try:
                error = response.json().get('detail', '')
                raise APIGetError('Error, while loading data. %s'%error)
            # Якщо сервер не повернув помилку, як об’єкт json
            except ValueError:
                raise APIUploadError('%s %s'%(response.status_code, response.reason))
        # Інакше повертаємо результат
        if response.text:
            return response.json()
        return {}

    def _options(self, resource_url):
        auth = HTTPSignatureAuth(key_id = self.API_KEY,
                    secret = self.API_SECRET,
                    algorithm = 'hmac-sha256',
                    headers = SIGNATURE_HEADERS)
        try:
            response = requests.options('%s/%s/'%(API_URL, resource_url), auth = auth, headers = HEADERS)
        except RequestException, error:
            raise APIUploadError("Error, while loading data. %s"%error)
        return response.json()