#!/usr/bin/env python
#coding: utf-8

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


import datetime
from datawiz_upload import Up_DW
dw = Up_DW()

#Реєструємо нового користувача
print "Type username"
name = raw_input()
print "Type email"
email = raw_input()
print "Type password"
passwd = raw_input()

user = dw.register_user(name, email, passwd)
#Зберігаємо пару ключ:токен для подальшого доступу до API
print user["API_KEY"], ":" , user["API_SECRET"]
dw = Up_DW(API_KEY=user["API_KEY"], API_SECRET = user["API_SECRET"])

#Завантажуємо дані одиниць виміру
print "Upload units"
dw.upload_units("units.csv")
#Завантажуємо дані магазинів
print "Upload shops"
dw.upload_shops("shops.csv")
#Завантажуємо дані категорій
print "Upload categories"
dw.upload_categories("categories.csv")
#Завантажуємо дані терміналів
print "Upload terminals"
dw.upload_terminals("terminals.csv")
#Завантажуємо дані касирів
print "Upload cashiers"
dw.upload_cashiers("cashiers.csv")
#Завантажуємо дані товарів
print "Upload products"
dw.upload_products("products.csv")
#Завантажуємо дані клієнтів програми лояльності
print "Upload loyalty_client_info"
dw.upload_loyalty_client_info("loyalty.csv")
#Завантажуємо дані чеків
print "Upload receipts"
dw.upload_receipts("receipts.csv")
#Завантажуємо дані цін на товари
print "Upload price"
dw.upload_price("price.csv")
#Завантажуємо дані залишів товарів
print "Upload inventory"
dw.upload_inventory("inventory.csv")
#Запускаємо процес індексації даних. Після його завершення
#отримаємо листа на вказану електронну адресу.
print "Upload to service"
dw.upload_to_service(email)
