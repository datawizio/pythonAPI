Акции
=====

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/sales/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/sales/

Пример ответа:

.. code-block:: json

    {
        "count": 1246,
        "next": "https://api.datawiz.io/api/v1/sale/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/sale/713/",
                "sale_id": "713",
                "shops": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "name": "Акция Кока-Кола",
                "description": "",
                "date_from": "2018-06-30",
                "date_to": "2018-07-04",
                "status": "view",
                "sale_type": null,
                "access": [
                    {
                        "sale_id": "713",
                        "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                        "product_id": "59154",
                        "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                        "shop_id": "1",
                        "shop_url": "https://api.datawiz.io/api/v1/shops/1/"
                    },
                    {
                        "sale_id": "713",
                        "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                        "product_id": "59154",
                        "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                        "shop_id": "2",
                        "shop_url": "https://api.datawiz.io/api/v1/shops/2/"
                    },
                    {
                        "sale_id": "713",
                        "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                        "product_id": "59154",
                        "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                        "shop_id": "3",
                        "shop_url": "https://api.datawiz.io/api/v1/shops/3/"
                    },
                    {
                        "sale_id": "713",
                        "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                        "product_id": "59154",
                        "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                        "shop_id": "4",
                        "shop_url": "https://api.datawiz.io/api/v1/shops/4/"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/sales/(string: sale_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/sales/713/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/sale/713/",
        "sale_id": "713",
        "shops": [
            "1",
            "2",
            "3",
            "4"
        ],
        "name": "Акция Кока-Кола",
        "description": "",
        "date_from": "2018-06-30",
        "date_to": "2018-07-04",
        "status": "view",
        "sale_type": null,
        "access": [
            {
                "sale_id": "713",
                "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                "product_id": "59154",
                "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                "shop_id": "1",
                "shop_url": "https://api.datawiz.io/api/v1/shops/1/"
            },
            {
                "sale_id": "713",
                "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                "product_id": "59154",
                "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                "shop_id": "2",
                "shop_url": "https://api.datawiz.io/api/v1/shops/2/"
            },
            {
                "sale_id": "713",
                "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                "product_id": "59154",
                "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                "shop_id": "3",
                "shop_url": "https://api.datawiz.io/api/v1/shops/3/"
            },
            {
                "sale_id": "713",
                "sale_url": "https://api.datawiz.io/api/v1/sale/713/",
                "product_id": "59154",
                "product_url": "https://api.datawiz.io/api/v1/products/59154/",
                "shop_id": "4",
                "shop_url": "https://api.datawiz.io/api/v1/shops/4/"
            }
        ]
    }

Поля ответа:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
url             строка       да           Ссылка на объект
sale_id         строка       да           Идентификатор акции
shops           список       нет          Список идентификаторов магазинов, на которые действует акция
name            строка       да           Название акции
description     строка       нет          Описание акции
date_from       строка       да           Дата начала акции
date_to         строка       да           Дата окончания акции
status          строка       нет          Статус для взаимодействия пользователей с акцией
sale_type       строка       нет          Тип акции
access          список       нет          Список доступов акции к товарам
=============== ============ ============ ============================================================

Поля ответа в списке ``access``:

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

.. class:: POST /api/v1/sales/

**REST API**

Добавить объект.

Поля запроса:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
sale_id         строка       да           Идентификатор акции
shops           список       нет          Список идентификаторов магазинов, на которые действует акция
name            строка       да           Название акции
description     строка       нет          Описание акции
date_from       строка       да           Дата начала акции
date_to         строка       да           Дата окончания акции
status          строка       нет          Статус для взаимодействия пользователей с акцией
sale_type       строка       нет          Тип акции
=============== ============ ============ ============================================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'sale_id=777&name=Акция Молоко&shops=%5B"1"%2C"2"%2C"3"%5B&date_from=2018-06-12&date_to=2018-06-20' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/sales/

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
    dw.upload_sales([{
        'sale_id': 777,
        'name': 'Акция Молоко',
        'shops': ["1", "2", "3"],
        'date_from': '2018-06-12',
        'date_to': '2018-06-20'

    }])