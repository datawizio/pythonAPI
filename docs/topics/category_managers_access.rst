Доступы категорийных менеджеров
===============================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/categorymanager-products/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/categorymanager-products/

Пример ответа:

.. code-block:: json

    {
        "count": 887913,
        "next": "https://api.datawiz.io/api/v1/categorymanager-products/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/categorymanager-products/9_6_5225_2016-01-01/",
                "manager_id": "9",
                "product_id": "5225",
                "shop_id": "6",
                "date_from": "2016-01-01",
                "date_to": "2018-01-01"
            },
            {
                "url": "https://api.datawiz.io/api/v1/categorymanager-products/9_6_5293_2016-01-01/",
                "manager_id": "9",
                "product_id": "5293",
                "shop_id": "6",
                "date_from": "2016-01-01",
                "date_to": "2018-01-01"
            },
            {
                "url": "https://api.datawiz.io/api/v1/categorymanager-products/9_6_5538_2017-01-01/",
                "manager_id": "9",
                "product_id": "5538",
                "shop_id": "6",
                "date_from": "2017-01-01",
                "date_to": "2018-01-01"
            }
        ]
    }

.. class:: GET /api/v1/categorymanager-products/(string: manager_id)_(string: shop_id)_(string: product_id)_(string: date_from)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/categorymanager-products/9_6_5538_2017-01-01/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/categorymanager-products/9_6_5538_2017-01-01/",
        "manager_id": "9",
        "product_id": "5538",
        "shop_id": "6",
        "date_from": "2017-01-01",
        "date_to": "2018-01-01"
    }


Поля ответа:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
url             строка       да           Ссылка на объект
manager_id      строка       да           Идентификатор менеджера
product_id      строка       да           Идентификатор товара
shop_id         строка       да           Идентификатор магазина
date_from       строка       да           Дата начала работы со следующей связкой
date_to         строка       да           Дата окончания работы со следующей связкой
=============== ============ ============ ============================================================

.. class:: POST /api/v1/categorymanager-products/

**REST API**

Добавить объект.

Поля запроса:

=============== ============ ============ ============================================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ============================================================
manager_id      строка       да           Идентификатор менеджера
product_id      строка       да           Идентификатор товара
shop_id         строка       да           Идентификатор магазина
date_from       строка       нет          Дата начала работы со следующей связкой
date_to         строка       нет          Дата окончания работы со следующей связкой
=============== ============ ============ ============================================================

Уникальные поля: **manager_id, shop_id, product_id, date_from**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'manager_id=777&product_id=111&shop_id=888' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/categorymanager-products/

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
    dw.upload_categorymanageraccess/([{
        'manager_id': 777,
        'product_id': 111,
        'shop_id': 888
    }])