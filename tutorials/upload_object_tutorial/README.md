# Tutorial по загрузці даних через об’єкт.
---



###Крок 1 - установка бібліотеки datawiz.
```
git clone https://github.com/datawizio/pythonAPI.git
cd pythonAPI
pip install -r requirments.txt
```
###Крок 2 - створення нового користувача.
```
python
from datawiz_upload import Up_DW
dw = Up_DW()
user = dw.register_user('<name>', '<email>', '<password>')
print user['API_KEY'], ':' , user['API_SECRET']
```
Збережіть обрані реєстраційні дані та ключ для подальшого доступу до API.

###Крок 3 - завантаження даних.
```
#Ініціалізація екземпляру класу.
dw = Up_DW(API_KEY=user['API_KEY'], API_SECRET = user['API_SECRET'])

#Завантаження даних одиниць виміру.
units = [{"unit_id": "UNIT-IDENTIFIER-1",
        "name": "UNIT-1"},
         {"unit_id": "UNIT-IDENTIFIER-2",
        "name": "UNIT-2"}]
dw.upload_units(units)

#Завантаження даних магазинів.
shops = [{"shop_id": "SHOP-IDENTIFIER-1",
        "name": "SHOP-1",
        "address": "Golovna st. 25",
        "open_date": "2015-10-22"},
        {"shop_id": "SHOP-IDENTIFIER-2",
        "name": "SHOP-2",
        "address": "Nezalezhnosti st. 34",
        "open_date": "2014-05-27"}]
dw.upload_shops(shops)

#Завантаження даних категорій.
categories = [{"category_id": "CATEGORY-IDENTIFIER-1",
              "name": "PARENT-CATEGORY",
              "parent_id": None},
             {"category_id": "CATEGORY-IDENTIFIER-2",
              "name": "CHILD-CATEGORY",
              "parent_id": "CATEGORY-IDENTIFIER-1"}]
dw.upload_categories(categories)

#Завантаження даних терміналів.
terminals = [{"terminal_id": "TERMINAL-IDENTIFIER-1",
              "shop_id": "SHOP-IDENTIFIER-1",
              "name": "TERMINAL-1"},
             {"terminal_id": "TERMINAL-IDENTIFIER-2",
              "shop_id": "SHOP-IDENTIFIER-2",
              "name": "TERMINAL-2"}]
dw.upload_terminals(terminals)

#Завантаження даних касирів.
[{"cashier_id": "CASHIER-IDENTIFIER-1",
             "name":"CASHIER-1"},
 {"cashier_id": "CASHIER-IDENTIFIER-2",
             "name":"CASHIER-2"}]
dw.upload_cashiers(cashiers)

#Завантаження даних товарів.
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
dw.upload_products(products)

#Завантаження даних клієнтів програми лояльності.
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
dw.upload_loyalty_client_info(clients)

#Завантаження даних чеків.
cartitems = [{"order_no":"1",
              "product_id": "PRODUCT-IDENTIFIER-1",
              "base_price": 5.0,
              "price": 15.0,
              "qty": 3.0},
             {"order_no":"2",
              "product_id": "PRODUCT-IDENTIFIER-2",
              "base_price": 3.0,
              "price": 6.0,
              "qty": 2.0}]
receipts = [{'order_id': 'RECEIPT-IDENTIFIER-1',
             'date': '2015-10-11 10:25:39',
             'terminal_id': 'TERMINAL-IDENTIFIER-1',
             'cartitems': cartitems,
             'loyalty_id': 'LOYALTY-IDENTIFIER-1',
             "cashier_id": "CASHIER-IDENTIFIER-1",
             "shop_id": "SHOP-IDENTIFIER-1"
            },
            {'order_id': 'RECEIPT-IDENTIFIER-2',
             'date': '2015-10-11 11:33:46',
             'terminal_id': 'TERMINAL-IDENTIFIER-2',
             'cartitems': cartitems,
             'loyalty_id': 'LOYALTY-IDENTIFIER-2',
             "cashier_id": "CASHIER-IDENTIFIER-2",
             "shop_id": "SHOP-IDENTIFIER-2"
}]
dw.upload_receipts(receipts)

#Завантаження даних цін на товари.
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
dw.upload_price(prices)

#Завантаження даних залишків товарів.
inventory = [{"shop_id": "SHOP-IDENTIFIER-1",
    	     "product_id": "PRODUCT-IDENTIFIER-1",
             "date": "2015-6-22",
             "qty": 25.0,
             "original_price": 4.9,
             "stock_total_price": 122.5}]
dw.upload_inventory(inventory)

#Запуск процесу індексації даних.
dw.upload_to_service('<email>')
```
Після завершення кешування на вказану вами електронну адресу буде надіслано листа. Процес кешування може тривати до кількох годин.
