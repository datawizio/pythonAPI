Категории
=========

Обязательно к заполнению: **Да**

.. class:: GET /api/v1/categories/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/categories/

Пример ответа:

.. code-block:: json

    {
        "count": 516,
        "next": "https://api.datawiz.io/api/v1/categories/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/categories/778062/",
                "category_id": "778062",
                "name": "Кукурузные палочки",
                "hidden": false,
                "parent_id": "74400",
                "parent_url": "https://api.datawiz.io/api/v1/categories/74400/"
            },
            {
                "url": "https://api.datawiz.io/api/v1/categories/778065/",
                "category_id": "778065",
                "name": "Попкорн",
                "hidden": false,
                "parent_id": "74400",
                "parent_url": "https://api.datawiz.io/api/v1/categories/74400/"
            },
            {
                "url": "https://api.datawiz.io/api/v1/categories/129811/",
                "category_id": "129811",
                "name": "Консервы",
                "hidden": false,
                "parent_id": "4567658",
                "parent_url": "https://api.datawiz.io/api/v1/categories/4567658/"
            }
        ]
    }

.. class:: GET /api/v1/categories/(string: category_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/categories/778062/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/categories/778062/",
        "category_id": "778062",
        "name": "Кукурузные палочки",
        "hidden": false,
        "parent_id": "74400",
        "parent_url": "https://api.datawiz.io/api/v1/categories/74400/"
    }

Поля ответа:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
url           строка       да           Ссылка на объект
category_id   строка       да           Идентификатор категории
name          строка       да           Название категории
hidden        логический   нет          Не показывать в системе
parent_id     строка       нет          Идентификатор объекта-родителя
parent_url    строка       нет          Ссылка на объект-родителя
============= ============ ============ ================================

.. class:: POST /api/v1/categories/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
category_id   строка       да           Идентификатор категории
name          строка       да           Название категории
hidden        логический   нет          Не показывать в системе
parent_id     строка       да           Идентификатор объекта-родителя
============= ============ ============ ================================

Уникальные поля: **category_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'category_id=777&name=Пиво&parent_id=444' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/categories/

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
    dw.upload_categories([{
        'category_id': 777,
        'name': 'Пиво',
        'parent_id': 444'
    }])