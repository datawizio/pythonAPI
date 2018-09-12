Типы списаний
=============

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/loss-types/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/loss-types/

Пример ответа:

.. code-block:: json

    {
        "count": 24,
        "next": "http://api.datawiz.io/api/v1/loss-types/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/loss-types/18/",
                "loss_type_id": "18",
                "name": "Не кондиция"
            },
            {
                "url": "http://api.datawiz.io/api/v1/loss-types/19/",
                "loss_type_id": "19",
                "name": "Списание продукции производства"
            },
            {
                "url": "http://api.datawiz.io/api/v1/loss-types/20/",
                "loss_type_id": "20",
                "name": "Списание овощей и фруктов"
            },
            {
                "url": "http://api.datawiz.io/api/v1/loss-types/21/",
                "loss_type_id": "21",
                "name": "Статьи списания"
            }
        ]
    }

.. class:: GET /api/v1/loss-types/(string: loss_type_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" http://api.datawiz.io/api/v1/loss-types/20/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/loss-types/20/",
        "loss_type_id": "20",
        "name": "Списание овощей и фруктов"
    }


Поля ответа:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
url           строка       да           Ссылка на объект
loss_type_id  строка       да           Идентификатор типа списания
name          строка       да           Название типа списания
============= ============ ============ ================================

.. class:: POST /api/v1/loss-types/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
loss_type_id  строка       да           Идентификатор типа списания
name          строка       да           Название типа списания
============= ============ ============ ================================

Уникальные поля: **loss_type_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'loss_type_id=777&name=Расходы товаров на дегустацию' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/loss-types/

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
    dw.upload_loss_types([{
        'loss_type_id': 777,
        'name': 'Расходы товаров на дегустацию'
    }])