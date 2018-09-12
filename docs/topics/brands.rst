Бренды
======

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/brands/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/brands/

Пример ответа:

.. code-block:: json

    {
        "count": 1286,
        "next": "https://api.datawiz.io/api/v1/brands/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/brands/111/",
                "brand_id": "111",
                "name": "Shura"
            },
            {
                "url": "https://api.datawiz.io/api/v1/brands/4525/",
                "brand_id": "4525",
                "name": "Exactly Milky"
            },
            {
                "url": "https://api.datawiz.io/api/v1/brands/97/",
                "brand_id": "97",
                "name": "Beger"
            },
            {
                "url": "https://api.datawiz.io/api/v1/brands/135/",
                "brand_id": "135",
                "name": "Nabeer"
            }
        ]
    }

.. class:: GET /api/v1/brands/(string: brand_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/brands/97/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/brands/97/",
        "brand_id": "97",
        "name": "Beger"
    }


Поля ответа:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
url           строка       да           Ссылка на объект
brand_id      строка       да           Идентификатор бренда
name          строка       да           Название бренда
============= ============ ============ ================================

.. class:: POST /api/v1/brands/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
brand_id      строка       да           Идентификатор бренда
name          строка       да           Название бренда
============= ============ ============ ================================

Уникальные поля: **brand_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'brand_id=777&name=Gibro' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/brands/

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
    dw.upload_brands([{
        'brand_id': 777,
        'name': 'Gibro'
    }])