Документы инвентаризаций
========================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/stock-taking-documents/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/stock-taking-documents/

Пример ответа:

.. code-block:: json

    {
        "count": 29608,
        "next": "http://api.datawiz.io/api/v1/stock-taking-documents/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29123_24/",
                "document_id": "29123",
                "stuff_id": "0",
                "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
                "shop_id": "24",
                "shop_url": "http://api.datawiz.io/api/v1/shops/24/",
                "date": "2018-03-01T17:07:27",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29123_24/products/2167001/",
                        "product_id": "7200",
                        "product_url": "http://api.datawiz.io/api/v1/products/7200/",
                        "stock_qty": "0.0000",
                        "fact_qty": "0.0980"
                    }
                ]
            },
            {
                "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29144_48/",
                "document_id": "29144",
                "stuff_id": "0",
                "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
                "shop_id": "48",
                "shop_url": "http://api.datawiz.io/api/v1/shops/48/",
                "date": "2018-03-02T06:00:00",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29144_48/products/2167969/",
                        "product_id": "5550",
                        "product_url": "http://api.datawiz.io/api/v1/products/5550/",
                        "stock_qty": "0.0000",
                        "fact_qty": "0.0000"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29144_48/products/2167970/",
                        "product_id": "7024",
                        "product_url": "http://api.datawiz.io/api/v1/products/7024/",
                        "stock_qty": "0.2900",
                        "fact_qty": "0.2900"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29144_48/products/2167971/",
                        "product_id": "5229",
                        "product_url": "http://api.datawiz.io/api/v1/products/5229/",
                        "stock_qty": "0.7200",
                        "fact_qty": "0.7540"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/stock-taking-documents/(string: document_id)_(string: shop_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" http://api.datawiz.io/api/v1/stock-taking-documents/29123_24/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29123_24/",
        "document_id": "29123",
        "stuff_id": "0",
        "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
        "shop_id": "24",
        "shop_url": "http://api.datawiz.io/api/v1/shops/24/",
        "date": "2018-03-01T17:07:27",
        "products": [
            {
                "url": "http://api.datawiz.io/api/v1/stock-taking-documents/29123_24/products/2167001/",
                "product_id": "7200",
                "product_url": "http://api.datawiz.io/api/v1/products/7200/",
                "stock_qty": "0.0000",
                "fact_qty": "0.0980"
            }
        ]
    }


Поля ответа:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
url                   строка       да           Ссылка на объект
document_id           строка       да           Идентификатор документа
stuff_id              строка       нет          Идентификатор сотрудника
stuff_url             строка       нет          Ссылка на объект сотрудника
shop_id               строка       да           Идентификатор магазина
shop_url              строка       да           Ссылка на объект магазина
date                  строка       да           Дата документа
products              список       да           Список товаров в приходной накладной
===================== ============ ============ ===============================================

Поля ответа в списке ``products``:

=================== ============ ============ ============================================================
Поле                Тип          Обязательное Описание
=================== ============ ============ ============================================================
url                 строка       да           Ссылка на объект
product_id          строка       да           Идентификатор товара
product_url         строка       да           Ссылка на объект товара
stock_qty           число        да           Реальное количество товара на остатке
fact_qty            число        да           Фактическое количество товара на остатке
=================== ============ ============ ============================================================


.. class:: POST /api/v1/stock-taking-documents/

**REST API**

Добавить объект.

Поля запроса:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
document_id           строка       да           Идентификатор документа
stuff_id              строка       нет          Идентификатор сотрудника
shop_id               строка       да           Идентификатор магазина
date                  строка       да           Дата документа
products              список       да           Список товаров в приходной накладной
===================== ============ ============ ===============================================

Поля запроса для объекта ``products``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
product_id          строка       да           Идентификатор товара
stock_qty           число        да           Реальное количество товара на остатке
fact_qty            число        да           Фактическое количество товара на остатке
================== ============ ============ ============================================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"document_id": "44", "shop_id": 23, "products": [{"fact_qty": "20.1500", "stock_qty": "18.1500", "product_id": "763530"}], "date": "2018-03-21T10:48:48"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/stock-taking-documents/

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
    dw.upload_stock_taking_documents([{
        'document_id': 44,
        'shop_id': 23,
        'date': '2018-03-21T10:48:48',
        'products': [
            {
                'fact_qty': 20.1500,
                'stock_qty': 18.1500,
                'product_id': 763530,
            }
        ]
    }])