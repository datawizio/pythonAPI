Магазины
========
Торговые точки сети клиента.

Обязательно к заполнению: **Да**

.. class:: GET /api/v1/shops/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/shops/

Пример ответа:

.. code-block:: json

    {
        "count": 39,
        "next": "https://api.datawiz.io/api/v1/shops/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/shops/30/",
                "shop_id": "30",
                "format_id": "5",
                "format_url": "https://api.datawiz.io/api/v1/shop-format/5/",
                "group_id": "15",
                "group_url": "https://api.datawiz.io/api/v1/shop-groups/15/",
                "name": "Магазин №22",
                "address": "ул. Спартака, д. 88",
                "open_date": null,
                "latitude": "49.42127200",
                "longitude": "27.00445200"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shops/32/",
                "shop_id": "32",
                "format_id": "2",
                "format_url": "https://api.datawiz.io/api/v1/shop-format/2/",
                "group_id": "15",
                "group_url": "https://api.datawiz.io/api/v1/shop-groups/15/",
                "name": "Магазин №24",
                "address": "ул. Вольная, д. 47",
                "open_date": null,
                "latitude": "49.41002700",
                "longitude": "26.94185500"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shops/2/",
                "shop_id": "2",
                "format_id": "4",
                "format_url": "https://api.datawiz.io/api/v1/shop-format/4/",
                "group_id": "7",
                "group_url": "https://api.datawiz.io/api/v1/shop-groups/7/",
                "name": "Магазин №30",
                "address": "ул. Челюскинцев, д. 71",
                "open_date": null,
                "latitude": "50.44607400",
                "longitude": "30.60523500"
            },
            {
                "url": "https://api.datawiz.io/api/v1/shops/31/",
                "shop_id": "31",
                "format_id": "3",
                "format_url": "https://api.datawiz.io/api/v1/shop-format/3/",
                "group_id": "15",
                "group_url": "https://api.datawiz.io/api/v1/shop-groups/15/",
                "name": "Магазин №23",
                "address": "ул. Садовая, д. 87",
                "open_date": null,
                "latitude": "49.43666000",
                "longitude": "26.98178100"
            }
        ]
    }

.. class:: GET /api/v1/shops/(string: shop_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/shops/30/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/shops/30/",
        "shop_id": "30",
        "format_id": "5",
        "format_url": "https://api.datawiz.io/api/v1/shop-format/5/",
        "group_id": "15",
        "group_url": "https://api.datawiz.io/api/v1/shop-groups/15/",
        "name": "Магазин №22",
        "address": "ул. Спартака, д. 88",
        "open_date": null,
        "latitude": "49.42127200",
        "longitude": "27.00445200"
    }


Поля ответа:

============ ============ ============ ================================
Поле         Тип          Обязательное Описание
============ ============ ============ ================================
url          строка       да           Ссылка на объект
shop_id      строка       да           Идентификатор магазина
format_id    строка       нет          Идентификатор формата
format_url   строка       нет          Ссылка на объект формата
group_id     строка       нет          Идентификатор группы
group_url    строка       нет          Ссылка на объект группы
name         строка       да           Название магазина
address      строка       нет          Адресс магазина
open_date    строка       нет          Дата открытия магазина
latitude     строка       нет          Широта
longitude    строка       нет          Долгота
============ ============ ============ ================================

.. class:: POST /api/v1/shops/

**REST API**

Добавить объект.

Поля запроса:

Поле         Тип          Обязательное Описание
============ ============ ============ ================================
shop_id      строка       да           Идентификатор магазина
format_id    строка       нет          Идентификатор формата
group_id     строка       нет          Идентификатор группы
name         строка       да           Название магазина
address      строка       нет          Адресс магазина
open_date    строка       нет          Дата открытия магазина
latitude     число        нет          Широта
longitude    число        нет          Долгота
============ ============ ============ ================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'shop_id=11&group_id=2&format_id=3&name=Магазин №40&address=ул. Ломоносова 5' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/shops/

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
    dw.upload_shops([{
        'shop_id': 11,
        'group_id': 2,
        'format_id': 3,
        'name': 'Магазин №40',
        'address': 'ул. Ломоносова 5'
    }])