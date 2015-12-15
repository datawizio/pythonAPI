#!/usr/bin/env python
#coding: utf-8

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


import datetime
from datawiz_upload import Up_DW
dw = Up_DW()

#Реєструємо нового користувача
name = 'new_user'
email = 'my_email@mail.com'
passwd = '12345'

user = dw.register_user(name, email, passwd)
#Зберігаємо пару ключ:токен для подальшого доступу до API
print user["API_KEY"], ":" , user["API_SECRET"]
dw = Up_DW(API_KEY=user["API_KEY"], API_SECRET = user["API_SECRET"])

#Завантажуємо дані одиниць виміру
print "Upload units"
dw.upload_units("data/units.csv")

#Завантажуємо дані магазинів
print "Upload shops"
dw.upload_shops("data/shops.csv")

#Завантажуємо дані категорій
print "Upload categories"
dw.upload_categories("data/categories.csv")

#Завантажуємо дані терміналів
print "Upload terminals"
dw.upload_terminals("data/terminals.csv")

#Завантажуємо дані касирів
print "Upload cashiers"
dw.upload_cashiers("data/cashiers.csv")

#Завантажуємо дані товарів
print "Upload products"
dw.upload_products("data/products.csv", columns = ['product_id',
                                                   'article',
                                                   'name',
                                                   'category_id',
                                                   'unit_id'])

#Завантажуємо дані клієнтів програми лояльності
print "Upload loyalty_client_info"
dw.upload_loyalty_client_info("data/loyalty.csv", ['loyalty_id', 'cardno', 'client_name', 'client_birthday'])

#Завантажуємо дані чеків
print "Upload receipts"
dw.upload_receipts("data/receipts.csv")

#Завантажуємо дані цін на товари
print "Upload price"
dw.upload_price("data/price.csv")

#Завантажуємо дані залишів товарів
print "Upload inventory"
dw.upload_inventory("data/inventory.csv")

#Запускаємо процес індексації даних. Після його завершення
#отримаємо листа на вказану електронну адресу.
print "Upload to service"
dw.upload_to_service(email)
