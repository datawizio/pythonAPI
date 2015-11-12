#!/usr/bin/env python
#coding: utf-8
from datawiz_auth import Auth, APIGetError, APIUploadError
import pandas
import os
import logging



RECEIPTS_API_URI = 'receipts'
RECEIPTS_CHUNK_SIZE = 1000
logging.basicConfig(
    format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
    level = logging.DEBUG)

class Up_DW(Auth):

    def _create_request_object(self, buff, columns = []):

        """
        Функція формує правильний json-об’єкт для відправки на сервер

        """

        def _group_cartitems(receipt):
            cartitem_columns = ['product_id', 'base_price', 'qty', 'total_price']
            cartitems = receipt[cartitem_columns]
            cartitems['order_no'] = range(1, len(cartitems))
            cartitems['price'] = cartitems['base_price']
            cartitems = cartitems.to_dict(orient = 'records')
            total_price = (receipt.price*receipt.qty).sum()
            return pandas.Series({'cartitems': cartitems, 'total_price': total_price})
        df = pandas.DataFrame(buff)
        df = df.groupby('date' 'order_id', 'shop', 'terminal', 'cashier_id', 'loyalty_id')\
            .apply(_group_cartitems)
        df = df.reset_index()
        return df.to_dict(orient = 'records')
    def _split_list_to_chunks(self, lst, chunk_size=100):
        """
        Функція-генератор: розбиває список на чанки відповідно
        до розміру chunk_size
        """

        chunk_size = max(1, chunk_size)
        for i in xrange(0 , len(lst), chunk_size):
            yield lst[i:i+chunk_size]

    #TODO: Розбиває чанк на менші частини і відправляє їх на сервер.
    # Якщо відправка провалюється,розбиває чанк на ще менші частини
    def _upload_data_recursively(self, resource_url, data, delimeter = 10):
        pass
    def upload_receipts(self, receipts, splitter = ';'):
        """

        Функція відправляє на сервер дані по чеках
        Приймає список об’єктів чека в форматі

        {
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
        #Якщо переданий список об’єктів чека
        if isinstance(receipts, list):
            #Розбмиваємо список на частини і відправляємо на сервер
            for chunk in self._split_list_to_chunks(receipts,
                                                    chunk_size=RECEIPTS_CHUNK_SIZE):
                try:
                    self._post(RECEIPTS_API_URI, data=chunk)
                    logging.info('Receipts uploaded')
                except APIUploadError:
                    #self._upload_data_recursively
                    logging.error('Receipts upload failed')
            return True
        #Якщо ж переданий шлях до файлу
        elif isinstance(receipts, str) and os.path.isfile(receipts):
            #Читаємо файл чанками розміром RECEIPTS_CHUNK_SIZE
            reader = pandas.read_csv(header = None,
                                     chunksize = RECEIPTS_CHUNK_SIZE,
                                     names = columns)
            tmp_chunk = None
            chunk_num = 1
            logging.info('Receipts upload started')
            for chunk in reader:
                if tmp_chunk:
                    order_id = list(chunk.tail(1)['order_id'])[0]
                    #Чанк, в якому немає останнього чека з попереднього чанка
                    chunk = chunk[chunk['order_id'] != order_id]
                    receipt_chunk = chunk[chunk['order_id'] == order_id]
                    #Додаємо в попередній чанк частини чека, розбиті пандою
                    tmp_chunk = tmp_chunk.append(receipt_chunk)
                    #Створюємо об’єкт запиту для передачі на сервер
                    data = self._create_request_object(tmp_chunk)
                    try:
                        self._post(RECEIPTS_API_URI, data = data)
                        logging.info('Receipts chunk #%s uploaded'%chunk_num)
                    except APIUploadError:
                        #self._upload_data_recursively
                        logging.error('Receipts chunk #%s upload failed'%chunk_num)
                    chunk_num += 1
                tmp_chunk = chunk
        else:
            raise TypeError("Invalid params")
        return True