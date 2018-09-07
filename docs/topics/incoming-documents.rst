Приходные накладные
===================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/incoming-documents/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/incoming-documents/

Пример ответа:

.. code-block:: json

    {
        "count": 32526,
        "next": "http://api.datawiz.io/api/v1/incoming-documents/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/incoming-documents/32298_24/",
                "document_id": "32298",
                "stuff_id": "0",
                "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
                "shop_id": "24",
                "shop_url": "http://api.datawiz.io/api/v1/shops/24/",
                "date": "2018-03-01T17:07:27",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/incoming-documents/32298_24/products/406764/",
                        "product_id": "7200",
                        "product_url": "http://api.datawiz.io/api/v1/products/7200/",
                        "qty": "0.0980",
                        "price": "81.2200",
                        "total_price": "7.9600"
                    }
                ]
            },
            {
                "url": "http://api.datawiz.io/api/v1/incoming-documents/32329_48/",
                "document_id": "32329",
                "stuff_id": "0",
                "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
                "shop_id": "48",
                "shop_url": "http://api.datawiz.io/api/v1/shops/48/",
                "date": "2018-03-02T06:00:00",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/incoming-documents/32329_48/products/406855/",
                        "product_id": "47809",
                        "product_url": "http://api.datawiz.io/api/v1/products/47809/",
                        "qty": "6.0000",
                        "price": "22.8600",
                        "total_price": "137.1600"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/incoming-documents/32329_48/products/406856/",
                        "product_id": "968602",
                        "product_url": "http://api.datawiz.io/api/v1/products/968602/",
                        "qty": "1.4900",
                        "price": "52.0000",
                        "total_price": "77.4800"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/incoming-documents/(string: document_id)_(string: shop_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" http://api.datawiz.io/api/v1/incoming-documents/32298_24/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/incoming-documents/32298_24/",
        "document_id": "32298",
        "stuff_id": "0",
        "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
        "shop_id": "24",
        "shop_url": "http://api.datawiz.io/api/v1/shops/24/",
        "date": "2018-03-01T17:07:27",
        "products": [
            {
                "url": "http://api.datawiz.io/api/v1/incoming-documents/32298_24/products/406764/",
                "product_id": "7200",
                "product_url": "http://api.datawiz.io/api/v1/products/7200/",
                "qty": "0.0980",
                "price": "81.2200",
                "total_price": "7.9600"
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
total_price         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
=================== ============ ============ ============================================================


.. class:: POST /api/v1/incoming-documents/

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
total_price         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
================== ============ ============ ============================================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"document_id": "44", "shop_id": 23, "products": [{"price": "20.1500", "price_total": "20.1500", "product_id": "763530", "qty": "1.0000"}], "date": "2018-03-21T10:48:48"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/incoming-documents/

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
    dw.upload_incoming_documents([{
        'document_id': 44,
        'shop_id': 23,
        'date': '2018-03-21T10:48:48',
        'products': [
            {
                'price': 20.1500,
                'price_total': 20.1500,
                'product_id': 763530,
                'qty': 1.0000
            }
        ]
    }])