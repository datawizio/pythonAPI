Группы магазинов
================
Наличие групп магазинов дает возможность формировать отчеты в разрезе областей, регионов или по каким-нибудь другим характеристикам.

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/shop-groups/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/shop-groups/

Пример ответа:

.. code-block:: json

    {
       "count":2,
       "next":"https://api.datawiz.io/api/v1/shop-groups/?page=2",
       "previous":null,
       "results":[
          {
             "url":"https://api.datawiz.io/api/v1/shop-groups/1/",
             "group_id":"1",
             "name":"Украина",
             "parent_id":null,
             "parent_url":"",
             "region_codes":[
                "ua-zp"
             ]
          },
          {
             "url":"https://api.datawiz.io/api/v1/shop-groups/10/",
             "group_id":"10",
             "name":"Запорожская обл.",
             "parent_id":"1",
             "parent_url":"https://api.datawiz.io/api/v1/shop-groups/1/",
             "region_codes":[
                "ua-zp"
             ]
          },
          {
             "url":"https://api.datawiz.io/api/v1/shop-groups/9/",
             "group_id":"9",
             "name":"Харьковская обл.",
             "parent_id":"1",
             "parent_url":"https://api.datawiz.io/api/v1/shop-groups/1/",
             "region_codes":[
                "ua-kk"
             ]
          }
       ]
    }

.. class:: GET /api/v1/shop-groups/(string: group_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/shop-groups/9/

Пример ответа:

.. code-block:: json

    {
       "url":"https://api.datawiz.io/api/v1/shop-groups/9/",
       "group_id":"9",
       "name":"Харьковская обл.",
       "parent_id":"1",
       "parent_url":"https://api.datawiz.io/api/v1/shop-groups/1/",
       "region_codes":[
          "ua-kk"
       ]
    }


Поля ответа:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
url          строка       да           Ссылка на объект
group_id     строка       да           Идентификатор группы
name         строка       да           Название группы
parent_id    строка       нет          Идентификатор группы-родителя
parent_url   строка       нет          Ссылка на объект-родителя
region_codes массив строк нет          Список кодов регионов группы
============ ============ ============ ================================

.. class:: POST /api/v1/shop-groups/

**REST API**

Добавить объект.

Поля запроса:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
group_id     строка       да           Идентификатор группы
name         строка       да           Название группы
parent_id    строка       нет          Идентификатор группы-родителя
region_codes массив строк нет          Список кодов регионов группы
============ ============ ============ ================================

Уникальные поля: **group_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'group_id=11&name=Львовская обл.&parent_id=1' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/shop-groups/

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
    dw.upload_shop_groups([{
        'group_id': 45,
        'name': 'Львовская обл.',
        'parent_id': 1,
    }])