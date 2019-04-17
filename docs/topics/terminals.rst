Кассы
=====

Обязательно к заполнению: **Да**

.. class:: GET /api/v1/terminals/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/terminals/

Пример ответа:

.. code-block:: json

    {
        "count": 334,
        "next": "https://api.datawiz.io/api/v1/terminals/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/terminals/113/",
                "terminal_id": "113",
                "name": "Касса №1",
                "shop_id": "40",
                "shop_url": "https://api.datawiz.io/api/v1/shops/40/"
            },
            {
                "url": "https://api.datawiz.io/api/v1/terminals/114/",
                "terminal_id": "114",
                "name": "Касса №2",
                "shop_id": "40",
                "shop_url": "https://api.datawiz.io/api/v1/shops/40/"
            },
            {
                "url": "https://api.datawiz.io/api/v1/terminals/115/",
                "terminal_id": "115",
                "name": "Касса №3",
                "shop_id": "40",
                "shop_url": "https://api.datawiz.io/api/v1/shops/40/"
            }
        ]
    }

.. class:: GET /api/v1/terminals/(string: terminal_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/terminals/113/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/terminals/113/",
        "terminal_id": "113",
        "name": "Касса №1",
        "shop_id": "40",
        "shop_url": "https://api.datawiz.io/api/v1/shops/40/"
    }


Поля ответа:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
url          строка       да           Ссылка на объект
terminal_id  строка       да           Идентификатор кассы
shop_id      строка       да           Идентификатор магазина
shop_url     строка       да           Ссылка на объект магазина
name         строка       да           Название кассы
============ ============ ============ ================================

.. class:: POST /api/v1/terminals/

**REST API**

Добавить объект.

Поля запроса:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
terminal_id  строка       да           Идентификатор кассы
shop_id      строка       да           Идентификатор магазина
name         строка       да           Название кассы
============ ============ ============ ================================

Уникальные поля: **terminal_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'shop_id=11&name=Касса №34&terminal_id=34' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/terminals/

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
    dw.upload_terminals([{
        'shop_id': 11,
        'name': 'Касса №34',
        'terminal_id': 34
    }])