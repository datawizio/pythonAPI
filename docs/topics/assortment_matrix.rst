Ассортиментная матрица
======================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/product-matrix/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/product-matrix/

Пример ответа:

.. code-block:: json

    {
        "count": 634456,
        "next": null,
        "previous": null,
        "results": [
            {
                "product_id": "48620",
                "product_url": "http://api.datawiz.io/api/v1/products/48620/",
                "shop_id": "23",
                "shop_url": "http://api.datawiz.io/api/v1/shops/23/",
                "date_from": "2018-08-01",
                "date_to": "2018-08-17"
            },
            {
                "product_id": "48620",
                "product_url": "http://api.datawiz.io/api/v1/products/48620/",
                "shop_id": "23",
                "shop_url": "http://api.datawiz.io/api/v1/shops/23/",
                "date_from": "2018-08-08",
                "date_to": "2018-08-10"
            },
            {
                "product_id": "48620",
                "product_url": "http://api.datawiz.io/api/v1/products/48620/",
                "shop_id": "23",
                "shop_url": "http://api.datawiz.io/api/v1/shops/23/",
                "date_from": "2018-08-09",
                "date_to": "2018-08-09"
            },
            {
                "product_id": "48620",
                "product_url": "http://api.datawiz.io/api/v1/products/48620/",
                "shop_id": "23",
                "shop_url": "http://api.datawiz.io/api/v1/shops/23/",
                "date_from": "2018-07-15",
                "date_to": "2018-07-17"
            }
        ]
    }

Поля ответа:

============= ============ ============ ===================================
Поле          Тип          Обязательное Описание
============= ============ ============ ===================================
shop_id         строка       да           Идентификатор магазина
shop_url        список       да           Ссылка на объект магазина
product_id      строка       да           Идентификатор товара
product_url     строка       да           Ссылка на объект товара
date_from       строка       да           Дата начала реализации товара
date_to         строка       нет          Дата окончания реализации товара
============= ============ ============ ===================================

.. class:: POST /api/v1/product-matrix/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ===================================
Поле          Тип          Обязательное Описание
============= ============ ============ ===================================
shop_id         строка       да           Идентификатор магазина
product_id      строка       да           Идентификатор товара
date_from       строка       да           Дата начала реализации товара
date_to         строка       нет          Дата окончания реализации товара
============= ============ ============ ===================================

Уникальные поля: **shop_id, product_id, date_from**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'shop_id=10&product_id=34&date_from=2018-05-20' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/product-matrix/

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
    dw.upload_product_matrix([{
        'shop_id': 10,
        'product_id': 34,
        'date_from': '2018-05-20'
    }])