Группы клиентов программы лояльности
====================================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/loyalty-group/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/loyalty-group/

Пример ответа:

.. code-block:: json

    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/loyalty-group/1/",
                "name": "Голден карта",
                "group_id": "1"
            },
            {
                "url": "https://api.datawiz.io/api/v1/loyalty-group/2/",
                "name": "Премиум карта",
                "group_id": "2"
            }
        ]
    }

.. class:: GET /api/v1/loyalty-group/(string: group_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/loyalty-group/1/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/loyalty-group/1/",
        "name": "Голден карта",
        "group_id": "1"
    }

Поля ответа:

=============== ============ ============ ====================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ====================================
url             строка       да           Ссылка на объект
group_id        строка       да           Идентификатор группы
name            строка       да           Название группы
=============== ============ ============ ====================================

.. class:: POST /api/v1/loyalty-group/

**REST API**

Добавить объект.

Поля запроса:

=============== ============ ============ ================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ================================
group_id        строка       да           Идентификатор группы
name            строка       да           Название группы
=============== ============ ============ ================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'group_id=777&name=Вип карта&cardno=9845344534867234' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/loyalty-group/

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
    dw.upload_loyalty_group([{
        'group_id': 777,
        'name': 'Вип карта',
    }])