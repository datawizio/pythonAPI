Остатки
=======

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/product-inventory/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/product-inventory/

Пример ответа:

.. code-block:: json

    {
        "count": 41858370,
        "next": "http://api.datawiz.io/api/v1/product-inventory/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/product-inventory/2018-01-16_3_5108/",
                "product_id": "5108",
                "product_url": "https://api.datawiz.io/api/v1/products/5108/",
                "shop_id": "3",
                "shop_url": "https://api.datawiz.io/api/v1/shops/3/",
                "date": "2018-01-16",
                "week_day": 1,
                "qty": "39.0000",
                "original_price": "17.7374",
                "stock_total_price": "691.7600"
            },
            {
                "url": "https://api.datawiz.io/api/v1/product-inventory/2018-01-16_3_5110/",
                "product_id": "5110",
                "product_url": "https://api.datawiz.io/api/v1/products/5110/",
                "shop_id": "3",
                "shop_url": "https://api.datawiz.io/api/v1/shops/3/",
                "date": "2018-01-16",
                "week_day": 1,
                "qty": "46.0000",
                "original_price": "13.5615",
                "stock_total_price": "623.8300"
            },
            {
                "url": "https://api.datawiz.io/api/v1/product-inventory/2018-01-16_3_5112/",
                "product_id": "5112",
                "product_url": "https://api.datawiz.io/api/v1/products/5112/",
                "shop_id": "3",
                "shop_url": "https://api.datawiz.io/api/v1/shops/3/",
                "date": "2018-01-16",
                "week_day": 1,
                "qty": "39.0000",
                "original_price": "17.2690",
                "stock_total_price": "673.4900"
            }
        ]
    }

.. class:: GET /api/v1/product-inventory/(string: date)_(string: shop_id)_(string: product_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/product-inventory/2018-01-16_3_5110/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/product-inventory/2018-01-16_3_5110/",
        "product_id": "5110",
        "product_url": "https://api.datawiz.io/api/v1/products/5110/",
        "shop_id": "3",
        "shop_url": "https://api.datawiz.io/api/v1/shops/3/",
        "date": "2018-01-16",
        "week_day": 1,
        "qty": "46.0000",
        "original_price": "13.5615",
        "stock_total_price": "623.8300"
    }

Поля ответа:

================= ============ ============ ====================================
Поле              Тип          Обязательное Описание
================= ============ ============ ====================================
url               строка       да           Ссылка на объект
product_id        строка       да           Идентификатор товара
product_url       строка       да           Название товара
shop_id           строка       да           Идентификатор магазина
product_url       строка       да           Название магазина
date              строка       да           Дата
week_day          число        да           День недели
qty               число        да           Количество товара на остатке
original_price    число        да           Себестоимость товара
stock_total_price число        да           Общая себестоимость товара
================= ============ ============ ====================================

.. class:: POST /api/v1/product-inventory/

**REST API**

Добавить объект.

Поля запроса:

================= ============ ============ ====================================
Поле              Тип          Обязательное Описание
================= ============ ============ ====================================
product_id        строка       да           Идентификатор товара
shop_id           строка       да           Идентификатор магазина
date              строка       да           Дата
qty               число        да           Количество товара на остатке
stock_total_price число        да           Общая себестоимость товара
================= ============ ============ ====================================

Уникальные поля: **date, shop_id, product_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'product_id=777&shop_id=111&date=2018-05-12&qty=5&stock_total_price=345.34' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/product-inventory/

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
    dw.upload_inventory([{
        'product_id': 777,
        'shop_id': 111,
        'date': '2018-05-12',
        'qty': 5,
        'stock_total_price': 345.34
    }])