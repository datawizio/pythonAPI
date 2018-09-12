Производители
=============

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/producers/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/producers/

Пример ответа:

.. code-block:: json

    {
        "count": 12,
        "next": "https://api.datawiz.io/api/v1/producers/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/producers/111/",
                "producer_id": "111",
                "name": "Shura"
            },
            {
                "url": "https://api.datawiz.io/api/v1/producers/4525/",
                "producer_id": "4525",
                "name": "Exactly Milky"
            },
            {
                "url": "https://api.datawiz.io/api/v1/producers/97/",
                "producer_id": "97",
                "name": "Beger"
            },
            {
                "url": "https://api.datawiz.io/api/v1/producers/135/",
                "producer_id": "135",
                "name": "Nabeer"
            }
        ]
    }

.. class:: GET /api/v1/producers/(string: producer_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/producers/97/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/producers/97/",
        "producer_id": "97",
        "name": "Beger"
    }


Поля ответа:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
url           строка       да           Ссылка на объект
producer_id   строка       да           Идентификатор производителя
name          строка       да           Название производителя
============= ============ ============ ================================

.. class:: POST /api/v1/producers/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
producer_id   строка       да           Идентификатор производителя
name          строка       да           Название производителя
============= ============ ============ ================================

Уникальные поля: **producer_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'producer_id=777&name=Gibro' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/producers/

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
    dw.upload_producers([{
        'producer_id': 777,
        'name': 'Gibro'
    }])