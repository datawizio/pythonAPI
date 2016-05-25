![] (https://cloud.githubusercontent.com/assets/3691333/15537779/e7fc0194-2280-11e6-8f25-3bb4120e2399.png)

Клієнт призначений для роботи з REST API [datawiz.io](http://datawiz.io). Дозволяє провести підключення та завантажити дані (чеки, товари, ціни, залишки) на сервіс для аналізу. Також дозволяє швидко отримати доступ до важливих аналітичних даних. Основний формат представлення даних - таблиці **pandas.DataFrame**. 

##Можливості
- Отримання даних користувача і статистики по ним
- Завантаження користувацьких даних на сервіс    

##Перші кроки
**Установка**    
```
git clone https://github.com/datawizio/pythonAPI.git
cd pythonAPI
python setup.py install
```    
**Використання**    
Отримання даних користувача        
```
>> from dwapi import datawiz    
>> dw = datawiz.DW()    
>> dw.get_client_info()    
     {u'date_from': datetime.datetime(2014, 5, 1, 1, 2, 7),
      u'date_to': datetime.datetime(2015, 11, 18, 22, 0),
      u'name': u'test2',
      u'shops': {595: u'Shop \u211602',
      601: u'Shop \u211603',
      641: u'Shop \u211601'}}
```    
Отримання даних продажів по категоріям    
```
>> from dwapi import datawiz    
>> dw = datawiz.DW()
>> dw.get_categories_sale(date_from="2015-10-11", date_to="2015-10-15")    
            АЛКОГОЛЬНА ГРУПА  БАКАЛІЯ  ВИРОБНИЦТВО  ЗАЛИШКИ  ЗАПАЛЬНИЧКИ
2015-10-11            563.71  4888.41       710.37    46.95       161.66
2015-10-12             58.97  5456.42       607.92   112.24       266.05
2015-10-13            300.63  5491.73       730.42    38.94       175.05
2015-10-14            352.47  4881.90       806.42    18.99       172.49
2015-10-15            388.47  4665.21       631.63    23.14       183.55    

```    
Отримання списку акцій    
```
>> from dwapi import datawiz    
>> dw = datawiz.DW()    
>> dw.get_sales()    
    date_from     date_to  profit  qty  receipts_qty  sale_id
0  2015-05-01  2015-06-30       0    0         16576       40
1  2015-03-03  2015-03-23       0    0          3121       41
2  2015-09-01  2015-09-30       0    0          1484       75
3  2015-09-01  2015-09-30       0    0          3471      131
4  2016-05-15  2016-05-21       0    0             0      140
5  2016-05-05  2016-05-20       0    0             0      142
```
##API    
Клієнт містить 3 класи, які виконують тільки свій ряд функцій    
Кожен клас приймає в якості аргументів ключ(`API_KEY`) і секрет(`API_SECRET`), необхідні для доступу до API. Якщо вони не задані, будуть використані параметри входу тестового користувача.    

**datawiz.DW**    
Містить функції для отримання даних.    
_Приклад роботи_    
```
>> from dwapi import datawiz    
>> dw = datawiz.DW("MyClientID", "MyClientSecret")    
>> dw.get_shops()    
   {641: {u'name': u'Shop \u211601', u'area': 1.0, u'longitude': 25.9581826,     
   u'address': u'\u0432\u0443\u043b. \u041f\u0435\u0442\u0440\u0430     \u0421\u0430\u0433\u0430\u0439\u0434\u0430\u0447\u043d\u043e\u0433\u043e,    
    25\u0431', u'latitude': 48.2874084, u'open_date': None
     }}
```    
, де `MyClientID` та `MyClientSecret`  - дані для доступу до API    

**datawiz_upload.Up_DW**    
Містить функції для завантаження даних на аналітичний сервіс [bi.datawiz.io](http://bi.datawiz.io)    
_Приклад роботи_    
```
>> from dwapi import datawiz_upload    
>> updw = datawiz_upload.Up_DW("MyClientID", "MyClientSecret")    
>> updw.upload_cashiers([{"cashier_id":"1", "name":"Vasya"}])
```    
, де `MyClientID` та `MyClientSecret`  - дані для доступу до API    

**datawiz_auth.Auth**    
Відповідає за авторизацію користувача. Містить функції для управління обліковим записом клієнта.    
_Приклад роботи_         
```
>> from dwapi import datawiz_auth    
>> auth = datawiz_auth.Auth("MyClientID", "MyClientSecret")    
>> auth.register_user("myusername","myemail@mail.com", "mypassword")   
   {
   'API_KEY': 'myusername',
   'API_SECRET': 'asdjf43rgjdg93'
   }
```    
, де `MyClientID` та `MyClientSecret`  - дані для доступу до API    
##Документація     
**Документація українською**    
- [Отримання даних](https://github.com/datawizio/pythonAPI/wiki/API-documentation)    
- [Завантаження даних](https://github.com/datawizio/pythonAPI/wiki/Upload-data)    

**Документация на русском**    
- [Получение данных](https://github.com/datawizio/pythonAPI/wiki/API-documentation-(rus))    
- [Загрузка данных](https://github.com/datawizio/pythonAPI/wiki/Upload-data-(rus))    

**Documentation in English**    
- [Get data](https://github.com/datawizio/pythonAPI/wiki/API-documentation-(eng))    
- [Upload data](https://github.com/datawizio/pythonAPI/wiki/Upload-data-(eng))    

##Туторіали    
- [Туторіали українською](https://github.com/datawizio/pythonAPI/wiki/Tutorials)    
- [Туториалы на русском](https://github.com/datawizio/pythonAPI/wiki/Tutorials-(rus))    
- [Tutorials in english](https://github.com/datawizio/pythonAPI/wiki/Tutorials-(eng))    

##Ліцензія    
**GNU General Public License**  - [GPLv3](http://www.gnu.org/copyleft/gpl.html)    

##Контакти    
email:[info@datawiz.io](mailto:info@datawiz.io)    
tel.  +38 (050) 337-73-53
