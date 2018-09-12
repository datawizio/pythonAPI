Документы перемещения товара
============================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/relocate-documents/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/relocate-documents/

Пример ответа:

.. code-block:: json

    {
        "count": 529499,
        "next": "https://api.datawiz.io/api/v1/relocate-documents/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/",
                "shop_sender_id": "711",
                "shop_sender_url": "http://api.datawiz.io/api/v1/shops/711/",
                "shop_receiver_id": "109070",
                "shop_receiver_url": "http://api.datawiz.io/api/v1/shops/109070/",
                "date": "2018-08-21T13:07:00",
                "responsible": "Владислав",
                "total_price": "2075.1972",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/products/7093552/",
                        "product_id": "308916",
                        "product_url": "http://api.datawiz.io/api/v1/products/308916/",
                        "qty": "1.1680",
                        "price": "788.9300",
                        "total_price": "921.4702"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/products/7093551/",
                        "product_id": "305540",
                        "product_url": "http://api.datawiz.io/api/v1/products/305540/",
                        "qty": "1.3040",
                        "price": "884.7600",
                        "total_price": "1153.7270"
                    }
                ]
            },
            {
                "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T00:00:00__711_109090/",
                "shop_sender_id": "711",
                "shop_sender_url": "http://api.datawiz.io/api/v1/shops/711/",
                "shop_receiver_id": "109090",
                "shop_receiver_url": "http://api.datawiz.io/api/v1/shops/109090/",
                "date": "2018-08-21T00:00:00",
                "responsible": "Дмитрий",
                "total_price": "32045.7162",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T00:00:00__711_109090/products/7093593/",
                        "product_id": "309040",
                        "product_url": "http://api.datawiz.io/api/v1/products/309040/",
                        "qty": "0.7300",
                        "price": "690.8500",
                        "total_price": "504.3205"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/relocate-documents/(string: date)__(string: shop_sender_id)_(string: shop_receiver_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/",
        "shop_sender_id": "711",
        "shop_sender_url": "http://api.datawiz.io/api/v1/shops/711/",
        "shop_receiver_id": "109070",
        "shop_receiver_url": "http://api.datawiz.io/api/v1/shops/109070/",
        "date": "2018-08-21T13:07:00",
        "responsible": "Владислав",
        "total_price": "2075.1972",
        "products": [
            {
                "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/products/7093552/",
                "product_id": "308916",
                "product_url": "http://api.datawiz.io/api/v1/products/308916/",
                "qty": "1.1680",
                "price": "788.9300",
                "total_price": "921.4702"
            },
            {
                "url": "http://api.datawiz.io/api/v1/relocate-documents/2018-08-21T13:07:00__711_109070/products/7093551/",
                "product_id": "305540",
                "product_url": "http://api.datawiz.io/api/v1/products/305540/",
                "qty": "1.3040",
                "price": "884.7600",
                "total_price": "1153.7270"
            }
        ]
    }


Поля ответа:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
url                   строка       да           Ссылка на объект
shop_sender_id        строка       да           Идентификатор магазина отправителя
shop_sender_url       строка       да           Ссылка на объект магазина отправителя
shop_receiver_id      строка       да           Идентификатор магазина получателя
shop_receiver_url     строка       да           Ссылка на объект магазина получателя
date                  строка       да           Дата перемещения
responsible           строка       нет          Ответственное лицо
total_price           число        да           Общая сумма товара
products              список       да           Список товаров в документе перемещения
===================== ============ ============ ===============================================

Поля ответа в списке ``products``:

=================== ============ ============ ============================================================
Поле                Тип          Обязательное Описание
=================== ============ ============ ============================================================
url                 строка       да           Ссылка на объект
product_id          строка       да           Идентификатор товара
product_url         строка       да           Ссылка на объект товара
total_price         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
=================== ============ ============ ============================================================


.. class:: POST /api/v1/relocate-documents/

**REST API**

Добавить объект.

Поля запроса:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
shop_sender_id        строка       да           Идентификатор магазина отправителя
shop_receiver_id      строка       да           Идентификатор магазина получателя
date                  строка       да           Дата перемещения
responsible           строка       нет          Ответственное лицо
total_price           число        нет          Общая сумма товара
products              список       да           Список товаров в документе перемещения
===================== ============ ============ ===============================================

Уникальные поля: **date, shop_sender_id, shop_receiver_id**

Поля запроса для объекта ``products``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
product_id          строка       да           Идентификатор товара
total_price         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
================== ============ ============ ============================================================

Уникальные поля: **нет**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"shop_sender_id": "44", "shop_receiver_id": "33",  "products": [{"price": "20.1500", "price_total": "20.1500", "product_id": "763530", "qty": "1.0000"}], "date": "2018-03-21T10:48:48", "responsible": "Максим", "total_price": "628.2000"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/relocate-documents/

Пример ответа:

.. code-block:: json

    {
       "results":{
          "updated":0,
          "created":1
       }
    }

**Python клиент**

Пример запроса используя Python клиент:

.. code-block:: python

    from dwapi.datawiz_upload import Up_DW

    dw = Up_DW(API_KEY='test1@mail.com', API_SECRET='1qaz')
    dw.upload_relocate_doc([{
        'shop_sender_id': 44,
        'shop_receiver_id': 33
        'date': '2018-03-21T10:48:48',
        'responsible': 'Максим',
        'total_price': 20.1500,
        'products': [
            {
                'price': 20.1500,
                'price_total': 20.1500,
                'product_id': 763530,
                'qty': 1.0000
            }
        ]
    }])