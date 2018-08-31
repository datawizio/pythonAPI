Метки чеков
===========

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/receipt-markers/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/receipt-markers/

Пример ответа:

.. code-block:: json

    {
        "count": 3,
        "next": "https://api.datawiz.io/api/v1/receipt-markers/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/receipt-markers/1/",
                "marker_id": "1",
                "name": "Фискальный"
            },
            {
                "url": "http://api.datawiz.io/api/v1/receipt-markers/2/",
                "marker_id": "2",
                "name": "Не фискальный"
            },
            {
                "url": "http://api.datawiz.io/api/v1/receipt-markers/3/",
                "marker_id": "3",
                "name": "Опт"
            }
        ]
    }

.. class:: GET /api/v1/receipt-markers/(string: marker_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/receipt-markers/1/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/receipt-markers/1/",
        "marker_id": "1",
        "name": "Фискальный"
    }


Поля ответа:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
marker_id    строка       да           Идентификатор метки
name         строка       да           Название метки
============ ============ ============ ================================

.. class:: POST /api/v1/receipt-markers/

**REST API**

Добавить объект.

Поля запроса:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
marker_id    строка       да           Идентификатор метки
name         строка       да           Название метки
============ ============ ============ ================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'marker_id=11&name=Онлайн продажи' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/receipt-markers/

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
    dw.upload_receipt_markers([{
        'marker_id': 11,
        'name': 'Онлайн продажи'
    }])