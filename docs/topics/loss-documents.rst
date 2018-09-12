Документы списаний
==================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/loss-documents/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/loss-documents/

Пример ответа:

.. code-block:: json

    {
        "count": 70846,
        "next": "http://api.datawiz.io/api/v1/loss-documents/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/loss-documents/69340_26/",
                "document_id": "69340",
                "stuff_id": "0",
                "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
                "loss_type_id": "19",
                "loss_type_url": "http://api.datawiz.io/api/v1/loss-types/19/",
                "shop_id": "26",
                "shop_url": "http://api.datawiz.io/api/v1/shops/26/",
                "date": "2018-03-03T15:55:25",
                "note": "",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/loss-documents/69340_26/products/600456/",
                        "product_id": "4092",
                        "product_url": "http://api.datawiz.io/api/v1/products/4092/",
                        "qty": "0.4100",
                        "price": "67.1000",
                        "total_price": "27.5100"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/loss-documents/69340_26/products/600457/",
                        "product_id": "7391",
                        "product_url": "http://api.datawiz.io/api/v1/products/7391/",
                        "qty": "0.5000",
                        "price": "43.2400",
                        "total_price": "21.6200"
                    }
                ]
            },
            {
                "url": "http://api.datawiz.io/api/v1/loss-documents/70164_2/",
                "document_id": "70164",
                "stuff_id": "0",
                "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
                "loss_type_id": "20",
                "loss_type_url": "http://api.datawiz.io/api/v1/loss-types/20/",
                "shop_id": "2",
                "shop_url": "http://api.datawiz.io/api/v1/shops/2/",
                "date": "2018-03-09T19:28:42",
                "note": "",
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/loss-documents/70164_2/products/608502/",
                        "product_id": "1080",
                        "product_url": "http://api.datawiz.io/api/v1/products/1080/",
                        "qty": "0.5620",
                        "price": "22.0800",
                        "total_price": "12.4100"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/loss-documents/(string: document_id)_(string: shop_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" http://api.datawiz.io/api/v1/loss-documents/69340_26/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/loss-documents/69340_26/",
        "document_id": "69340",
        "stuff_id": "0",
        "stuff_url": "http://api.datawiz.io/api/v1/cashiers/0/",
        "loss_type_id": "19",
        "loss_type_url": "http://api.datawiz.io/api/v1/loss-types/19/",
        "shop_id": "26",
        "shop_url": "http://api.datawiz.io/api/v1/shops/26/",
        "date": "2018-03-03T15:55:25",
        "note": "",
        "products": [
            {
                "url": "http://api.datawiz.io/api/v1/loss-documents/69340_26/products/600456/",
                "product_id": "4092",
                "product_url": "http://api.datawiz.io/api/v1/products/4092/",
                "qty": "0.4100",
                "price": "67.1000",
                "total_price": "27.5100"
            },
            {
                "url": "http://api.datawiz.io/api/v1/loss-documents/69340_26/products/600457/",
                "product_id": "7391",
                "product_url": "http://api.datawiz.io/api/v1/products/7391/",
                "qty": "0.5000",
                "price": "43.2400",
                "total_price": "21.6200"
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
loss_type_id          строка       да           Идентификатор типа списания
loss_type_url         строка       да           Ссылка на объект типа списания
shop_id               строка       да           Идентификатор магазина
shop_url              строка       да           Ссылка на объект магазина
date                  строка       да           Дата документа
note                  строка       нет          Заметка
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


.. class:: POST /api/v1/loss-documents/

**REST API**

Добавить объект.

Поля запроса:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
document_id           строка       да           Идентификатор документа
stuff_id              строка       нет          Идентификатор сотрудника
loss_type_id          строка       да           Идентификатор типа списания
shop_id               строка       да           Идентификатор магазина
date                  строка       да           Дата документа
products              список       да           Список товаров в приходной накладной
===================== ============ ============ ===============================================

Уникальные поля: **document_id. shop_id**

Поля запроса для объекта ``products``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
product_id          строка       да           Идентификатор товара
total_price         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
================== ============ ============ ============================================================

Уникальные поля: **нет**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"document_id": "44", "loss_type_id": 1, "shop_id": 23, "products": [{"price": "20.1500", "price_total": "20.1500", "product_id": "763530", "qty": "1.0000"}], "date": "2018-03-21T10:48:48"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/loss-documents/

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
    dw.upload_loss_documents([{
        'document_id': 44,
        'shop_id': 23,
        'loss_type_id': 1,
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