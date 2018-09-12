Кассиры
=======

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/cashiers/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/cashiers/

Пример ответа:

.. code-block:: json

    {
        "count": 3122,
        "next": "https://api.datawiz.io/api/v1/cashiers/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/cashiers/133/",
                "cashier_id": "133",
                "name": "Аксенова Прасковья Матвеевна"
            },
            {
                "url": "https://api.datawiz.io/api/v1/cashiers/10096/",
                "cashier_id": "10096",
                "name": "Воробьев Николай Владленович"
            },
            {
                "url": "https://api.datawiz.io/api/v1/cashiers/10101/",
                "cashier_id": "10101",
                "name": "Самойлова Любовь Кузминична"
            },
            {
                "url": "https://api.datawiz.io/api/v1/cashiers/10242/",
                "cashier_id": "10242",
                "name": "Соловьев Никанор Брониславович"
            }
        ]
    }

.. class:: GET /api/v1/cashiers/(string: cashier_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/cashiers/10242/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/cashiers/10242/",
        "cashier_id": "10242",
        "name": "Соловьев Никанор Брониславович"
    }


Поля ответа:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
url           строка       да           Ссылка на объект
cashier_id    строка       да           Идентификатор кассира
name          строка       да           Название кассира
============= ============ ============ ================================

.. class:: POST /api/v1/cashiers/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
cashier_id    строка       да           Идентификатор кассира
name          строка       да           Название кассира
============= ============ ============ ================================

Уникальные поля: **cashier_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'cashier_id=888&name=Брендан Айк' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/cashiers/

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
    dw.upload_cashiers([{
        'cashier_id': 888,
        'name': 'Брендан Айк'
    }])