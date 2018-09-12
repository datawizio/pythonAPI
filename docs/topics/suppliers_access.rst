Доступы поставщиков
===================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/supplier-products/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/supplier-products/

Пример ответа:

.. code-block:: json

    {
        "count": 265947,
        "next": "https://api.datawiz.io/api/v1/supplier-products/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/supplier-products/16744_29_748135/",
                "supplier_id": "16744",
                "product_id": "748135",
                "shop_id": "29",
                "bonus": "0.000",
                "deferment": 0,
                "date_from": null,
                "date_to": null
            },
            {
                "url": "https://api.datawiz.io/api/v1/supplier-products/16744_35_748168/",
                "supplier_id": "16744",
                "product_id": "748168",
                "shop_id": "35",
                "bonus": "0.000",
                "deferment": 0,
                "date_from": null,
                "date_to": null
            },
            {
                "url": "https://api.datawiz.io/api/v1/supplier-products/16744_47_748258/",
                "supplier_id": "16744",
                "product_id": "748258",
                "shop_id": "47",
                "bonus": "0.000",
                "deferment": 0,
                "date_from": null,
                "date_to": null
            }
        ]
    }

.. class:: GET /api/v1/supplier-products/(string: supplier_id)_(string: shop_id)_(string: product_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/supplier-products/16744_47_748258/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/supplier-products/16744_47_748258/",
        "supplier_id": "16744",
        "product_id": "748258",
        "shop_id": "47",
        "bonus": "0.000",
        "deferment": 0,
        "date_from": null,
        "date_to": null
    }

Поля ответа:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
url             строка       да           Ссылка на объект
supplier_id     строка       да           Идентификатор поставщика
product_id      список       да           Идентификатор товара
shop_id         строка       да           Идентификатор магазина
bonus           строка       да           Бонус поставщику
deferment       строка       да           Отсрочка поставки
date_from       строка       нет          Дата начала работы с поставщиком
date_to         строка       нет          Дата окончания работы с поставщиком
=============== ============ ============ ============================================================

.. class:: POST /api/v1/supplier-products/

**REST API**

Добавить объект.

Поля запроса:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
supplier_id     строка       да           Идентификатор поставщика
product_id      список       да           Идентификатор товара
shop_id         строка       да           Идентификатор магазина
bonus           строка       нет          Бонус поставщику
deferment       строка       нет          Отсрочка поставки
date_from       строка       нет          Дата начала работы с поставщиком
date_to         строка       нет          Дата окончания работы с поставщиком
=============== ============ ============ ============================================================

Уникальные поля: **supplier_id, shop_id, product_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'supplier_id=777&product_id=888&shop_id=111&date_from=2018-06-10' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/supplier-products/

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
    dw.upload_suppliers_access([{
        'supplier_id': 777,
        'product_id': 888,
        'shop_id': 111,
        'date_from': '2018-06-10',
    }])