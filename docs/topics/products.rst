Товары
======

Обязательно к заполнению: **Да**

.. class:: GET /api/v1/products/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/products/

Пример ответа:

.. code-block:: json

    {
        "count": 19917,
        "next": "https://api.datawiz.io/api/v1/products/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/products/3390/",
                "product_id": "3390",
                "name": "Стартовый пакет Vodafone Red S",
                "article": "18581",
                "barcode": "",
                "category_id": "779963",
                "category_url": "https://api.datawiz.io/api/v1/categories/779963/",
                "brand_id": "1345",
                "brand_url": "https://api.datawiz.io/api/v1/brands/1345/",
                "producer_id": null,
                "producer_url": null,
                "unit_id": "1",
                "unit_url": "https://api.datawiz.io/api/v1/units/1/",
                "active": true,
                "width": null,
                "height": null,
                "depth": null
            },
            {
                "url": "https://api.datawiz.io/api/v1/products/3473/",
                "product_id": "3473",
                "name": "Сигареты Sobranie Gold",
                "article": "10959",
                "barcode": "904,4820000535182,46128416,46085351,4033100063084",
                "category_id": "1002",
                "category_url": "https://api.datawiz.io/api/v1/categories/1002/",
                "brand_id": "1191",
                "brand_url": "https://api.datawiz.io/api/v1/brands/1191/",
                "producer_id": null,
                "producer_url": null,
                "unit_id": "1",
                "unit_url": "https://api.datawiz.io/api/v1/units/1/",
                "active": true,
                "width": null,
                "height": null,
                "depth": null
            },
            {
                "url": "https://api.datawiz.io/api/v1/products/3479/",
                "product_id": "3479",
                "name": "Сигареты Красные Столичные",
                "article": "2042",
                "barcode": "4820000363433,4820000361590,288",
                "category_id": "1002",
                "category_url": "https://api.datawiz.io/api/v1/categories/1002/",
                "brand_id": "1207",
                "brand_url": "https://api.datawiz.io/api/v1/brands/1207/",
                "producer_id": null,
                "producer_url": null,
                "unit_id": "1",
                "unit_url": "https://api.datawiz.io/api/v1/units/1/",
                "active": false,
                "width": null,
                "height": null,
                "depth": null
            }
        ]
    }

.. class:: GET /api/v1/products/(string: product_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/products/3479/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/products/3479/",
        "product_id": "3479",
        "name": "Сигареты Красные Столичные",
        "article": "2042",
        "barcode": "4820000363433,4820000361590,288",
        "category_id": "1002",
        "category_url": "https://api.datawiz.io/api/v1/categories/1002/",
        "brand_id": "1207",
        "brand_url": "https://api.datawiz.io/api/v1/brands/1207/",
        "producer_id": null,
        "producer_url": null,
        "unit_id": "1",
        "unit_url": "https://api.datawiz.io/api/v1/units/1/",
        "active": false,
        "width": null,
        "height": null,
        "depth": null
    }

Поля ответа:

============= ============ ============ ====================================
Поле          Тип          Обязательное Описание
============= ============ ============ ====================================
url           строка       да           Ссылка на объект
product_id    строка       да           Идентификатор товара
name          строка       да           Название товара
article       строка       нет          Артикул
barcode       строка       нет          Штрих-код
category_id   строка       да           Идентификатор категории
category_url  строка       да           Ссылка на объект категории
brand_id      строка       нет          Идентификатор бренда
brand_url     строка       нет          Ссылка на объект бренда
producer_id   строка       нет          Идентификатор производителя
producer_url  строка       нет          Ссылка на объект производителя
unit_id       строка       нет          Идентификатор единицы измерения
unit_url      строка       нет          Ссылка на объект единицы измерения
active        логический   нет          Активный
width         число        нет          Ширина товара
height        число        нет          Высота товара
depth         число        нет          Глубина товара
============= ============ ============ ====================================

.. class:: POST /api/v1/products/

**REST API**

Добавить объект.

Поля запроса:

============= ============ ============ ================================
Поле          Тип          Обязательное Описание
============= ============ ============ ================================
product_id    строка       да           Идентификатор товара
name          строка       да           Название товара
article       строка       нет          Артикул
barcode       строка       нет          Штрих-код
category_id   строка       да           Идентификатор категории
brand_id      строка       нет          Идентификатор бренда
producer_id   строка       нет          Идентификатор производителя
unit_id       строка       нет          Идентификатор единицы измерения
active        логический   нет          Активный
width         число        нет          Ширина товара
height        число        нет          Высота товара
depth         число        нет          Глубина товара
============= ============ ============ ================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'product_id=777&name=Яблоко Голден&category_id=444' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/products/

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
    dw.upload_products([{
        'product_id': 777,
        'name': 'Яблоко Голден',
        'category_id': 444'
    }])