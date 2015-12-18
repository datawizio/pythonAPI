#!/usr/bin/env python
#coding: utf-8

import sys
from os import path
import datetime

sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

from datawiz_upload import Up_DW
dw = Up_DW()
#Реєструємо нового користувача
name = 'new_user'
email = 'email1@mail.com'
passwd = '12345'


user = dw.register_user(name, email, passwd)

#Зберігаємо пару ключ:токен для подальшого доступу до API
print user["API_KEY"], ":" , user["API_SECRET"]
# user = {'API_KEY': 'email1@mail.com', 'API_SECRET': '78@3fe7c8a0ee5df1eba633838c73f56691'}
dw = Up_DW(API_KEY=user["API_KEY"], API_SECRET = user["API_SECRET"])

#Завантажуємо дані одиниць виміру
units = [{"unit_id": "UNIT-IDENTIFIER-1",
        "name": "UNIT-1"},
         {"unit_id": "UNIT-IDENTIFIER-2",
        "name": "UNIT-2"}]
print "Upload units"
dw.upload_units(units)

#Завантажуємо дані магазинів
shops = [{"shop_id": "SHOP-IDENTIFIER-1",
        "name": "SHOP-1",
        "address": "Golovna st. 25",
        "open_date": "2015-10-22"},
      {"shop_id": "SHOP-IDENTIFIER-2",
        "name": "SHOP-2",
        "address": "Nezalezhnosti st. 34",
        "open_date": "2014-05-27"}]
print "Upload shops"
dw.upload_shops(shops)

#Завантажуємо дані категорій
categories = [{"category_id": "CATEGORY-IDENTIFIER-1",
              "name": "PARENT-CATEGORY",
              "parent_id": None},
             {"category_id": "CATEGORY-IDENTIFIER-2",
              "name": "CHILD-CATEGORY",
              "parent_id": "CATEGORY-IDENTIFIER-1"}]
print "Upload categories"
dw.upload_categories(categories)

#Завантажуємо дані терміналів
terminals = [{"terminal_id": "TERMINAL-IDENTIFIER-1",
              "shop_id": "SHOP-IDENTIFIER-1",
              "name": "TERMINAL-1"},
             {"terminal_id": "TERMINAL-IDENTIFIER-2",
              "shop_id": "SHOP-IDENTIFIER-2",
              "name": "TERMINAL-2"}]
print "Upload terminals"
dw.upload_terminals(terminals)

#Завантажуємо дані касирів
cashiers = [{"cashier_id": "CASHIER-IDENTIFIER-1",
             "name":"CASHIER-1"},
            {"cashier_id": "CASHIER-IDENTIFIER-2",
             "name":"CASHIER-2"}]
print "Upload cashiers"
dw.upload_cashiers(cashiers)

#Завантажуємо дані товарів
products = [{"product_id": "PRODUCT-IDENTIFIER-1",
			 "article": "PRODUCT-ARTICLE",
			 "barcode": None,
			 "name": "PRODUCT-1",
			 "shop_id": "SHOP-IDENTIFIER-1",
			 "category_id": "CATEGORY-IDENTIFIER-2",
			 "unit_id": "UNIT-IDENTIFIER-1"},
            {"product_id": "PRODUCT-IDENTIFIER-2",
			 "article": "PRODUCT-ARTICLE",
			 "barcode": None,
			 "name": "PRODUCT-2",
			 "shop_id": "SHOP-IDENTIFIER-2",
			 "category_id": "CATEGORY-IDENTIFIER-2",
             "unit_id": "UNIT-IDENTIFIER-2"}]
print "Upload products"
dw.upload_products(products)

#Завантажуємо дані клієнтів програми лояльності
clients = [{"loyalty_id": "CLIENT-IDENTIFIER-1",
            "cardno": "435756ee345cc453",
            "client_name": u"Дмитро Констянтинович Переп`юк",
 	        "client_birthday": "1995-7-16",
            "is_male": True},
            {"loyalty_id": "CLIENT-IDENTIFIER-2",
             "cardno": "435756ee345cc454",
             "client_name": u"Валентина Константинівна Переп`юк",
 		     "client_birthday": "1985-10-12",
             "is_male": False}]
print "Upload loyalty"
dw.upload_loyalty_client_info(clients)

#Завантажуємо дані чеків
cartitems = [{"order_no":"1",
              "product_id": "PRODUCT-IDENTIFIER-1",
              "base_price": 5.0,
              "price": 15.0,
              "qty": 3.0,
              'total_price': 45.0},
             {"order_no":"2",
              "product_id": "PRODUCT-IDENTIFIER-2",
              "base_price": 3.0,
              "price": 6.0,
              "qty": 2.0,
              'total_price': 12.0}]
receipts = [{'order_id': 'RECEIPT-IDENTIFIER-1',
             'date': '2015-10-11 10:25:39',
             'terminal_id': 'TERMINAL-IDENTIFIER-1',
             'cartitems': cartitems,
             'loyalty_id': 'CLIENT-IDENTIFIER-1',
             "cashier_id": "CASHIER-IDENTIFIER-1",
             "shop_id": "SHOP-IDENTIFIER-1"
            },
            {'order_id': 'RECEIPT-IDENTIFIER-2',
             'date': '2015-10-11 11:33:46',
             'terminal_id': 'TERMINAL-IDENTIFIER-2',
             'cartitems': cartitems,
             'loyalty_id': 'CLIENT-IDENTIFIER-2',
             "cashier_id": "CASHIER-IDENTIFIER-2",
             "shop_id": "SHOP-IDENTIFIER-2"
}]
print "Upload receipts"
dw.upload_receipts(receipts)


#Завантажуємо дані цін на товари
prices = [{"shop_id": "SHOP-IDENTIFIER-1",
           "product_id": "PRODUCT-IDENTIFIER-1",
           "date": "2015-6-22",
           "original_price": 4.9,
           "price": 5.0},
         {"shop_id": "SHOP-IDENTIFIER-2",
          "product_id": "PRODUCT-IDENTIFIER-2",
          "date": "2015-6-22",
          "original_price": 2.8,
          "price": 3.0}]
print "Upload prices"
dw.upload_price(prices)

#Завантажуємо дані залишків товарів
inventory = [{"shop_id": "SHOP-IDENTIFIER-1",
    	     "product_id": "PRODUCT-IDENTIFIER-1",
             "date": "2015-6-22",
             "qty": 25.0,
             "original_price": 4.9,
             "stock_total_price": 122.5}]
print "Upload inventory"
dw.upload_inventory(inventory)

#Запускаємо процес індексації даних.
print dw.upload_to_service(email)






