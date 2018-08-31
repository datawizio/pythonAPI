Документы получения товара
==========================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/receive-documents/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/receive-documents/

Пример ответа:

.. code-block:: json

    {
        "count": 529499,
        "next": "https://api.datawiz.io/api/v1/receive-documents/?page=2",
        "previous": null,
        "results": [
            {
                "url": "http://api.datawiz.io/api/v1/receive-documents/3_469531/",
                "shop_id": "3",
                "shop_url": "http://api.datawiz.io/api/v1/shops/3/",
                "supplier_id": "531",
                "supplier_url": "http://api.datawiz.io/api/v1/suppliers/531/",
                "document_id": "469531",
                "order_id": null,
                "order_url": null,
                "document_number": "",
                "document_date": "2018-02-01T09:35:33",
                "price_total": "0.0000",
                "responsible": "Бурба Татьяна Ивановна",
                "items_qty": "20.0000",
                "doc_order": null,
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/receive-documents/3_469531/products/4093039/",
                        "document_product_id": 4093039,
                        "product_id": "242547",
                        "product_url": "http://api.datawiz.io/api/v1/products/242547/",
                        "price_total": "0.0000",
                        "qty": "20.0000",
                        "price": "0.0000"
                    }
                ]
            },
            {
                "url": "http://api.datawiz.io/api/v1/receive-documents/25_473140/",
                "shop_id": "25",
                "shop_url": "http://api.datawiz.io/api/v1/shops/25/",
                "supplier_id": "14129",
                "supplier_url": "http://api.datawiz.io/api/v1/suppliers/14129/",
                "document_id": "473140",
                "order_id": null,
                "order_url": null,
                "document_number": "",
                "document_date": "2018-02-03T09:35:18",
                "price_total": "154.5000",
                "responsible": "Чернобай Инна Николаевна",
                "items_qty": "15.0000",
                "doc_order": null,
                "products": [
                    {
                        "url": "http://api.datawiz.io/api/v1/receive-documents/25_473140/products/4113632/",
                        "document_product_id": 4113632,
                        "product_id": "11018",
                        "product_url": "http://api.datawiz.io/api/v1/products/11018/",
                        "price_total": "59.7000",
                        "qty": "5.0000",
                        "price": "11.9400"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/receive-documents/25_473140/products/4113631/",
                        "document_product_id": 4113631,
                        "product_id": "47714",
                        "product_url": "http://api.datawiz.io/api/v1/products/47714/",
                        "price_total": "59.7000",
                        "qty": "5.0000",
                        "price": "11.9400"
                    },
                    {
                        "url": "http://api.datawiz.io/api/v1/receive-documents/25_473140/products/4113630/",
                        "document_product_id": 4113630,
                        "product_id": "11502",
                        "product_url": "http://api.datawiz.io/api/v1/products/11502/",
                        "price_total": "35.1000",
                        "qty": "5.0000",
                        "price": "7.0200"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/receive-documents/(string: shop_id)_(string: document_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/receive-documents/34_2017-07-05T14:11:36_351_7555405/

Пример ответа:

.. code-block:: json

    {
        "url": "http://api.datawiz.io/api/v1/receive-documents/3_469531/",
        "shop_id": "3",
        "shop_url": "http://api.datawiz.io/api/v1/shops/3/",
        "supplier_id": "531",
        "supplier_url": "http://api.datawiz.io/api/v1/suppliers/531/",
        "document_id": "469531",
        "order_id": null,
        "order_url": null,
        "document_number": "",
        "document_date": "2018-02-01T09:35:33",
        "price_total": "0.0000",
        "responsible": "Бурба Татьяна Ивановна",
        "items_qty": "20.0000",
        "doc_order": null,
        "products": [
            {
                "url": "http://api.datawiz.io/api/v1/receive-documents/3_469531/products/4093039/",
                "document_product_id": 4093039,
                "product_id": "242547",
                "product_url": "http://api.datawiz.io/api/v1/products/242547/",
                "price_total": "0.0000",
                "qty": "20.0000",
                "price": "0.0000"
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
document_number       строка       нет          Номер документа
order_id              строка       нет          Идентификатор документа заказа товара
order_url             строка       нет          Ссылка на объект документа заказа товара
document_date         строка       да           Дата получения товара
doc_order             строка       нет          Идентификатор документа заказа товара
price_total           число        да           Общая сумма товаров в поставке
items_qty             число        да           Общее количество товаров в поставке
responsible           строка       нет          Ответственное лицо
products              список       да           Список товаров в заказе
===================== ============ ============ ===============================================

Поля ответа в списке ``products``:

=================== ============ ============ ============================================================
Поле                Тип          Обязательное Описание
=================== ============ ============ ============================================================
url                 строка       да           Ссылка на объект
document_product_id число        да           Идентификатор объекта в системе
product_id          строка       да           Идентификатор товара
product_url         строка       да           Ссылка на объект товара
price_total         число        да           Общая сумма товара
price               число        да           Цена товара
qty                 число        да           Количество товара
=================== ============ ============ ============================================================


.. class:: POST /api/v1/receive-documents/

**REST API**

Добавить объект.

Поля запроса:

===================== ============ ============ ===============================================
Поле                  Тип          Обязательное Описание
===================== ============ ============ ===============================================
document_id           строка       да           Идентификатор документа
shop_id               строка       да           Идентификатор магазина
supplier_id           строка       да           Идентификатор поставщика
document_number       строка       нет          Номер документа
order_id              строка       нет          Идентификатор документа заказа товара
document_date         строка       да           Дата получения товара
doc_order             строка       нет          Идентификатор документа заказа товара
price_total           число        да           Общая сумма товаров в поставке
items_qty             число        да           Общее количество товаров в поставке
responsible           строка       нет          Ответственное лицо
products              список       да           Список товаров в заказе
===================== ============ ============ ===============================================

Поля запроса для объекта ``products``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
product_id          строка      да           Идентификатор товара
price_total         число       да           Общая сумма товара
price               число       да           Цена товара
qty                 число       да           Количество товара
================== ============ ============ ============================================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"shop_id": "44", "products": [{"price": "20.1500", "price_total": "20.1500", "product_id": "763530", "qty": "1.0000"}], "document_date": "2018-03-21T10:48:48", "supplier_id": "17589", "document_number": "S10-00007776", "responsible": "Якоб Фон Петрович", "items_qty": "28.0000", "document_id": "568711", "price_total": "628.2000"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/receive-documents/

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
    dw.upload_receive_doc([{
        'shop_id': 44,
        'document_date': '2018-03-21T10:48:48',
        'supplier_id': 17589,
        'document_number': 'S10-00007776',
        'responsible': 'Якоб Фон Петрович',
        'items_qty': 28.0000,
        'document_id': 568711,
        'price_total': 628.2000
        'products': [
            {
                'price': 20.1500,
                'price_total': 20.1500,
                'product_id': 763530,
                'qty': 1.0000
            }
        ]
    }])