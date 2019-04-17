Категорийные менеджеры
======================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/category-managers/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/category-managers/

Пример ответа:

.. code-block:: json

    {
        "count": 9,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/category-managers/6/",
                "categories": [
                    "34",
                    "52"
                ],
                "shops": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "date_from": "2017-03-13",
                "identifier": "6",
                "name": "Быкова Марфа Макаровна",
                "access_count": 79482
            },
            {
                "url": "https://api.datawiz.io/api/v1/category-managers/13/",
                "categories": [
                    "45",
                    "23"
                ],
                "shops": [
                    "40",
                    "44",
                    "45",
                    "47",
                    "48",
                    "53",
                    "54",
                    "55"
                ],
                "date_from": "2011-01-18",
                "identifier": "13",
                "name": "Агафонов Савелий Эдуардович",
                "access_count": 97656
            },
            {
                "url": "https://api.datawiz.io/api/v1/category-managers/7/",
                "categories": [
                    "34",
                    "32",
                    "12"
                ],
                "shops": [
                    "25",
                    "26",
                    "28",
                    "29",
                    "30",
                    "31",
                    "32"
                ],
                "date_from": "2017-05-26",
                "identifier": "7",
                "name": "Ковалев Владимир Дмитриевич",
                "access_count": 63492
            }
        ]
    }

.. class:: GET /api/v1/category-managers/(string: identifier)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/category-managers/6/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/category-managers/6/",
        "categories": [
            "34",
            "52"
        ],
        "shops": [
            "1",
            "2",
            "3",
            "4"
        ],
        "date_from": "2017-03-13",
        "identifier": "6",
        "name": "Быкова Марфа Макаровна",
        "access_count": 79482
    }

Поля ответа:

====================== ============ ============ ============================================
Поле                   Тип          Обязательное Описание
====================== ============ ============ ============================================
url                    строка       да           Ссылка на объект
identifier             строка       да           Идентификатор категорийного менеджера
name                   строка       да           Имя категорийного менеджера
date_from              строка       нет          Дата начала работы категорийного менеджера
categories             список       да           Список идентификаторов доступных категорий
shops                  список       да           Список идентификаторов доступных магазинов
access_count           число        да           Количество доступных связок (магазин, товар)
====================== ============ ============ ============================================

.. class:: POST /api/v1/category-managers/

**REST API**

Добавить объект.

Поля запроса:

====================== ============ ============ ===========================
Поле                   Тип          Обязательное Описание
====================== ============ ============ ===========================
identifier             строка       да           Идентификатор категорийного менеджера
name                   строка       да           Имя категорийного менеджера
date_from              строка       нет          Дата начала работы категорийного менеджера
categories             список       нет          Список идентификаторов доступных категорий
shops                  список       нет          Список идентификаторов доступных магазинов
====================== ============ ============ ===========================

Уникальные поля: **identifier**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'identifier=777&name=Данилюк Виктор' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/category-managers/

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
    dw.upload_categorymanagers([{
        'identifier': 777,
        'name': 'Данилюк Виктор'
    }])