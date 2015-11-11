#!/usr/bin/env python
#coding: utf-8
from datawiz_auth import Auth, APIGetError, APIUploadError
import pandas
import os

RECEIPTS_API_URI = 'receipts'
RECEIPTS_CHUNK_SIZE = 1000

class Up_DW(Auth):

    def _create_request_object(self, buff, columns = []):

        """
        Функція формує правильний json-об’єкт для відправки на сервер

        """

        def _group_cartitems(receipt):
            cartitem_columns = ['order_no', 'product_id', 'base_price', 'qty', 'total_price']
            cartitems = receipt[cartitem_columns].reset_index('date').to_dict(orient = 'records')
            total_price = (receipt.price*receipt.qty).sum()
            return pandas.Series({'cartitems': cartitems, 'total_price': total_price})
        df = pandas.DataFrame().from_records(buff, columns=columns)
        df = df.groupby('date' 'order_id', 'shop', 'terminal', 'cashier_id', 'loyalty_id').apply(_group_cartitems)
        df = df.reset_index()
        return df.to_dict(orient = 'records')
    #To DO: Розбиває чанк на менші частини і відправляє їх на сервер. Якщо відправка провалюється,
    #розбиває чанк на ще менші частини
    def _upload_data_recursively(self, resource_url, data, delimeter = 10):
        pass

    def upload_receipts(self, receipts, splitter = ';'):
        """

        Функція відправляє на сервер дані по чеках
        Приймає об’єкт-чек в форматі

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
        #Колонки чеків, order_no генерується динамічно
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
                    'total_price',
                    'order_no']
        chunk_number = 1
        if isinstance(receipts, dict):
            return self._post(RECEIPTS_API_URI, data = receipts)
        elif isinstance(receipts, str) and os.path.isfile(receipts):
            with open(receipts) as file:
                print 'Upload started'
                for line in file:
                    row = line.split(splitter).append(1)
                    if len(row) != len(columns) - 1:
                        print 'Broken line'
                        continue
                    if receipts_buff and receipts_buff[-1][4] == row[4]:
                        row[-1] = receipts_buff[-1][-1] + 1
                        receipts_buff.append(row)
                        continue
                    if len(receipts_buff) >= RECEIPTS_CHUNK_SIZE:
                        data = self._create_request_object(receipts_buff, columns = columns)
                        try:
                            self._post(RECEIPTS_API_URI, data = data)
                            receipts_buff = []
                            print 'Chunk %s uploaded'%chunk_number
                        except APIUploadError:
                            #self._upload_data_recursively(data)
                            print 'Chunk %s failed'%chunk_number
                        chunk_number += 1
                    receipts_buff.append(row)
                print 'Upload ends'
        else:
            raise TypeError("Invalid params")
        return True