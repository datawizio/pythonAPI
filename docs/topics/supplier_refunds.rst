Документы возвратов поставщикам
===============================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/supplier-refunds/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/supplier-refunds/

Пример ответа:

.. code-block:: json

    {
        "count": 133544,
        "next": "http://api.datawiz.io/api/v1/supplier-refunds/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/supplier-refunds/133241_48/",
                "document_id": "133241",
                "supplier_id": "32749",
                "supplier_url": "http://api.datawiz.io/api/v1/suppliers/32749/",
                "shop_id": "48",
                "shop_url": "http://api.datawiz.io/api/v1/shops/48/",
                "date": "2018-03-21T08:38:21",
                "responsible": null,
                "description": null,
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/supplier-refunds/133241_48/products/1008959/",
                        "product_id": "241843",
                        "product_url": "http://api.datawiz.io/api/v1/products/241843/",
                        "receive_document_url": null,
                        "qty": "1.0000",
                        "price": "12.0500",
                        "total_price": "12.0500"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/supplier-refunds/133241_48/products/1008960/",
                        "product_id": "241843",
                        "product_url": "http://api.datawiz.io/api/v1/products/241843/",
                        "receive_document_url": null,
                        "qty": "1.0000",
                        "price": "12.0500",
                        "total_price": "12.0500"
                    }
                ]
            },
            {
                "url": "http://api.datawiz.io/api/v1/supplier-refunds/133242_48/",
                "document_id": "133242",
                "supplier_id": "32789",
                "supplier_url": "http://api.datawiz.io/api/v1/suppliers/32789/",
                "shop_id": "48",
                "shop_url": "http://api.datawiz.io/api/v1/shops/48/",
                "date": "2018-03-21T09:02:52",
                "responsible": null,
                "description": null,
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/supplier-refunds/133242_48/products/1008963/",
                        "product_id": "11104",
                        "product_url": "http://api.datawiz.io/api/v1/products/11104/",
                        "receive_document_url": null,
                        "qty": "1.0000",
                        "price": "5.5800",
                        "total_price": "5.5800"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/supplier-refunds/(string: document_id)_(string: shop_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" http://api.datawiz.io/api/v1/supplier-refunds/133241_48/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/supplier-refunds/133241_48/",
        "document_id": "133241",
        "supplier_id": "32749",
        "supplier_url": "http://api.datawiz.io/api/v1/suppliers/32749/",
        "shop_id": "48",
        "shop_url": "http://api.datawiz.io/api/v1/shops/48/",
        "date": "2018-03-21T08:38:21",
        "responsible": null,
        "description": null,
        "products": [
            {
                "url": "http://api.datawiz.io/api/v1/supplier-refunds/133241_48/products/1008959/",
                "product_id": "241843",
                "product_url": "http://api.datawiz.io/api/v1/products/241843/",
                "receive_document_url": null,
                "qty": "1.0000",
                "price": "12.0500",
                "total_price": "12.0500"
            },
            {
                "url": "http://api.datawiz.io/api/v1/supplier-refunds/133241_48/products/1008960/",
                "product_id": "241843",
                "product_url": "http://api.datawiz.io/api/v1/products/241843/",
                "receive_document_url": null,
                "qty": "1.0000",
                "price": "12.0500",
                "total_price": "12.0500"
            }
        ]
    }


Поля ответа:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
url                   строка       да           Ссылка на объект
document_id           строка       да           Идентификатор документа
shop_id               строка       да           Идентификатор магазина
shop_url              строка       да           Ссылка на объект магазина
supplier_id           строка       да           Идентификатор поставщика
supplier_url          строка       да           Ссылка на объект поставщика
date                  строка       да           Дата возврата
responsible           строка       нет          Ответственное лицо
description           строка       нет          Описание возврата
products              список       да           Список товаров в заказе
===================== ============ ============ ===============================================

Поля ответа в списке ``products``:

==================== ============ ============ ============================================================
Поле                 Тип          Обязательное Описание
==================== ============ ============ ============================================================
url                  строка       да           Ссылка на объект
product_id           строка       да           Идентификатор товара
product_url          строка       да           Ссылка на объект товара
receive_document_url строка       нет          Ссылка на объект документа получения
total_price          число        да           Общая сумма товара
price                число        да           Цена товара
qty                  число        да           Количество товара
==================== ============ ============ ============================================================


.. class:: POST /api/v1/supplier-refunds/

**REST API**

Добавить объект.

Поля запроса:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
document_id           строка       да           Идентификатор документа
shop_id               строка       да           Идентификатор магазина
shop_url              строка       да           Ссылка на объект магазина
supplier_id           строка       да           Идентификатор поставщика
supplier_url          строка       да           Ссылка на объект поставщика
date                  строка       да           Дата возврата
responsible           строка       нет          Ответственное лицо
description           строка       нет          Описание возврата
products              список       да           Список товаров в заказе
===================== ============ ============ ===============================================

Поля запроса для объекта ``products``:

=================== ============ ============ ============================================================
Поле                Тип          Обязательное Описание
=================== ============ ============ ============================================================
product_id          строка       да           Идентификатор товара
receive_document_id строка       нет          Идетификатор документа получения
total_price         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
=================== ============ ============ ============================================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"shop_id": "44", "products": [{"price": "20.1500", "total_price": "20.1500", "product_id": "763530", "qty": "1.0000"}], "date": "2018-03-21T10:48:48", "supplier_id": "17589", "responsible": "Якоб Фон Петрович", "document_id": "568711"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/supplier-refunds/

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
    dw.upload_supplier_refunds([{
        'shop_id': 44,
        'date': '2018-03-21T10:48:48',
        'supplier_id': 17589,
        'responsible': 'Якоб Фон Петрович',
        'document_id': 568711,
        'products': [
            {
                'price': 20.1500,
                'total_price': 20.1500,
                'product_id': 763530,
                'qty': 1.0000
            }
        ]
    }])