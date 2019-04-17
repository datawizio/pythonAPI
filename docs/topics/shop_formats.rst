Форматы магазинов
=================
Наличие форматов магазинов дают возможность фильтровать отчеты по каким-либо характеристикам.

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/shop-format/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/shop-format/

Пример ответа:

.. code-block:: json

    {
        "count": 5,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/shop-format/1/",
                "format_id": "1",
                "name": "S"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shop-format/2/",
                "format_id": "2",
                "name": "M"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shop-format/3/",
                "format_id": "3",
                "name": "L"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shop-format/4/",
                "format_id": "4",
                "name": "XL"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shop-format/5/",
                "format_id": "5",
                "name": "XXL"
            }
        ]
    }

.. class:: GET /api/v1/shop-format/(string: format_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/shop-format/5/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/shop-format/5/",
        "format_id": "5",
        "name": "XXL"
    }


Поля ответа:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
url          строка       да           Ссылка на объект
format_id    строка       да           Идентификатор группы
name         строка       да           Название группы
============ ============ ============ ================================

.. class:: POST /api/v1/shop-format/

**REST API**

Добавить объект.

Поля запроса:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
format_id    строка       да           Идентификатор группы
name         строка       да           Название группы
============ ============ ============ ================================

Уникальные поля: **format_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'group_id=11&name=Львовская обл.&parent_id=1' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/shop-format/

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
    dw.upload_shop_formats([{
        'format_id': 45,
        'name': 'Extra S',
    }])