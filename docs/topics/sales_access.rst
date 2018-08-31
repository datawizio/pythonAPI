Доступы акций
=============

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/sale-products/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/sale-products/

Пример ответа:

.. code-block:: json

    {
        "count": 155816,
        "next": "https://api.datawiz.io/api/v1/sale-products/?page=2",
        "previous": null,
        "results": [
            {
                "sale_id": "1",
                "sale_url": "https://api.datawiz.io/api/v1/sale/1/",
                "product_id": "88158",
                "product_url": "https://api.datawiz.io/api/v1/products/88158/",
                "shop_id": "1",
                "shop_url": "https://api.datawiz.io/api/v1/shops/1/"
            },
            {
                "sale_id": "1",
                "sale_url": "https://api.datawiz.io/api/v1/sale/1/",
                "product_id": "88158",
                "product_url": "https://api.datawiz.io/api/v1/products/88158/",
                "shop_id": "2",
                "shop_url": "https://api.datawiz.io/api/v1/shops/2/"
            },
            {
                "sale_id": "1",
                "sale_url": "https://api.datawiz.io/api/v1/sale/1/",
                "product_id": "88158",
                "product_url": "https://api.datawiz.io/api/v1/products/88158/",
                "shop_id": "3",
                "shop_url": "https://api.datawiz.io/api/v1/shops/3/"
            }
        ]
    }

Поля ответа:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
sale_id         строка       да           Идентификатор акции
sale_url        список       да           Ссылка на объект акции
product_id      строка       да           Идентификатор товара
product_url     строка       да           Ссылка на объект товара
shop_id         строка       да           Идентификатор магазина
shop_url        строка       да           Ссылка на объект магазина
=============== ============ ============ ============================================================

.. class:: POST /api/v1/sale-products/

**REST API**

Добавить объект.

Поля запроса:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
sale_id         строка       да           Идентификатор акции
product_id      строка       да           Идентификатор товара
shop_id         строка       да           Идентификатор магазина
=============== ============ ============ ============================================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'sale_id=777&product_id=111&shop_id=888' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/sale-products/

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
    dw.upload_sale_access/([{
        'sale_id': 777,
        'product_id': 111,
        'shop_id': 888
    }])