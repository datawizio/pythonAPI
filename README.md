![] (https://cloud.githubusercontent.com/assets/3691333/15537779/e7fc0194-2280-11e6-8f25-3bb4120e2399.png)

Клієнт призначений для роботи з REST API [datawiz.io](http://datawiz.io)

##Можливості
- Отримання даних користувача
- Отримання статистики    
- Завантаження користувацьких даних    

##Швидкий старт
**Установка**    
```
git clone https://github.com/datawizio/pythonAPI.git
cd pythonAPI
python setup.py install
```    
**Використання**    
Отримання даних користувача (в даному випадку тестового користувача)     
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
              Алкогольна група...    
    2015-10-11       563.71...
```    

##Документація     
**Документація українською**    
- [Отримання даних](https://github.com/datawizio/pythonAPI/wiki/API-documentation)    
- [Завантаження даних](https://github.com/datawizio/pythonAPI/wiki/Upload-data)    

**Документация на русском**    
- [Получение данных](https://github.com/datawizio/pythonAPI/wiki/API-documentation-(rus))    
- [Загрузка данных](https://github.com/datawizio/pythonAPI/wiki/Upload-data-(rus))    

**Documentation in English**    
- [Get data](https://github.com/datawizio/pythonAPI/wiki/API-documentation-(eng))    
- [Download data](https://github.com/datawizio/pythonAPI/wiki/Upload-data-(eng))    

##Туторіали    
- [Туторіали українською](https://github.com/datawizio/pythonAPI/wiki/Tutorials)    
- [Туториалы на русском](https://github.com/datawizio/pythonAPI/wiki/Tutorials-(rus))    
- [Tutorials in english](https://github.com/datawizio/pythonAPI/wiki/Tutorials-(eng))    

##Ліцензія    
