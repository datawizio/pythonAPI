"""
Основний клас для роботи з API - datawiz.DW
Ініціалізація:
	api = datawiz.DW(API_KEY, API_SECRET)
де API_KEY, API_SECRET - авторизаційні дані для доступу до API
Якщо не задати, використовуються тестові параметри

Методи класу:
	api.get_products_sale(categories = None, shops = None, products = None,
			      date_from = None, date_to = None, weekday = None,
			      by = 'total_price', interval = 'days') - повертає об’єкт DataFrame з результатами вибірки

Див. help(api.<func_name>) для детального опису
"""

import datetime
import datawiz as dw
date_from = datetime.date(2015, 8, 9)
date_to = datetime.date(2015, 9, 12)
api = dw.DW()
result = api.get_products_sale(shops = [305, 306, 318, 321], date_from = date_from, date_to = date_to, products = [2833024, 2286946], interval = dw.WEEKS, by='stock_qty')
