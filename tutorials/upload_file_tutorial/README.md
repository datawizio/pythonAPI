# Tutorial по загрузці даних через файл.
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
dw.upload_units('upload_file_tutorial/data/units.csv')

#Завантаження даних магазинів.
dw.upload_shops('upload_file_tutorial/data/shops.csv')

#Завантаження даних категорій.
dw.upload_categories('upload_file_tutorial/data/categories.csv')

#Завантаження даних терміналів.
dw.upload_terminals('upload_file_tutorial/data/terminals.csv')

#Завантаження даних касирів.
dw.upload_cashiers('upload_file_tutorial/data/cashiers.csv')

#Завантаження даних товарів.
dw.upload_products('upload_file_tutorial/data/products.csv')

#Завантаження даних клієнтів програми лояльності.
dw.upload_loyalty_client_info('upload_file_tutorial/data/loyalty.csv')

#Завантаження даних чеків.
dw.upload_receipts('upload_file_tutorial/data/receipts.csv')

#Завантаження даних ціни на товари.
dw.upload_price('upload_file_tutorial/data/price.csv')

#Завантаження даних залишків товарів.
dw.upload_inventory('upload_file_tutorial/data/inventory.csv')

#Запуск процесу індексації даних. Після його завершення надійде лист на вказану вами електронну адресу.
dw.upload_to_service('<email>')
```
Після завершення кешування на вказану вами електронну адресу буде надіслано листа. Процес кешування може тривати до кількох годин.
