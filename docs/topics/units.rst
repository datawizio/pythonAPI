Единицы измерения
=================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/units/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/units/

Пример ответа:

.. code-block:: json

    {
        "count": 34,
        "next": "https://api.datawiz.io/api/v1/units/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/units/29/",
                "unit_id": "29",
                "name": "т",
                "packed": true,
                "pack_capacity": 1
            },
            {
                "url": "https://api.datawiz.io/api/v1/units/28/",
                "unit_id": "28",
                "name": "пачка",
                "packed": true,
                "pack_capacity": 1
            },
            {
                "url": "https://api.datawiz.io/api/v1/units/27/",
                "unit_id": "27",
                "name": "кг",
                "packed": true,
                "pack_capacity": 1
            }
        ]
    }

.. class:: GET /api/v1/units/(string: unit_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/units/28/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/units/28/",
        "unit_id": "28",
        "name": "пачка",
        "packed": true,
        "pack_capacity": 1
    }


Поля ответа:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
url           строка       да           Ссылка на объект
unit_id       строка       да           Идентификатор единицы измерения
name          строка       да           Название единицы измерения
packed        логический   нет          Упаковка
pack_capacity число        нет          Вместимость упаковки
============= ============ ============ ================================

.. class:: POST /api/v1/units/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
unit_id       строка       да           Идентификатор единицы измерения
name          строка       да           Название единицы измерения
packed        логический   нет          Упаковка
pack_capacity число        нет          Вместимость упаковки
============= ============ ============ ================================

Уникальные поля: **unit_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'unit_id=5&name=ящик&packed=1&pack_capacity=5' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/units/

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
    dw.upload_units([{
        'unit_id': 5,
        'name': 'ящик',
        'packed': 1,
        'pack_capacity': 5,
    }])