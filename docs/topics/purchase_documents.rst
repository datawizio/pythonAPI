Документы заказа товара
=======================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/purchase-documents/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/purchase-documents/

Пример ответа:

.. code-block:: json

    {
        "count": 529499,
        "next": "https://api.datawiz.io/api/v1/purchase-documents/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/purchase-documents/2018-03-21T10:48:48_44_S10-00007776_568711/",
                "document_id": "568711",
                "shop_id": "44",
                "shop_url": "https://api.datawiz.io/api/v1/shops/44/",
                "supplier_id": "17589",
                "supplier_url": "https://api.datawiz.io/api/v1/suppliers/17589/",
                "document_number": "S10-00007776",
                "receive_date": "2018-03-21T10:48:48",
                "order_date": "2018-03-21T10:48:48",
                "price_total": "44.1000",
                "items_qty": "2.0000",
                "responsible": "Чаюн Наталья Николаевна",
                "commodity_credit_days": 0,
                "products": [
                    {
                        "url": "https://api.datawiz.io/api/v1/purchase-documents/2018-03-21T10:48:48_44_S10-00007776_568711/products/5986697/",
                        "document_product_id": 5986697,
                        "product_id": "763530",
                        "product_url": "https://api.datawiz.io/api/v1/products/763530/",
                        "price_total": "20.1500",
                        "qty": "1.0000",
                        "price": "20.1500"
                    },
                    {
                        "url": "https://api.datawiz.io/api/v1/purchase-documents/2018-03-21T10:48:48_44_S10-00007776_568711/products/5986696/",
                        "document_product_id": 5986696,
                        "product_id": "763517",
                        "product_url": "https://api.datawiz.io/api/v1/products/763517/",
                        "price_total": "23.9500",
                        "qty": "1.0000",
                        "price": "23.9500"
                    }
                ]
            },
            {
                "url": "https://api.datawiz.io/api/v1/purchase-documents/2017-01-11T16:49:41_20_MSA-00000705_67496/",
                "document_id": "67496",
                "shop_id": "20",
                "shop_url": "https://api.datawiz.io/api/v1/shops/20/",
                "supplier_id": "15943",
                "supplier_url": "https://api.datawiz.io/api/v1/suppliers/15943/",
                "document_number": "MSA-00000705",
                "receive_date": "2017-01-11T16:49:41",
                "order_date": "2017-01-11T16:49:41",
                "price_total": "295.0600",
                "items_qty": "11.0000",
                "responsible": "Лялюк Яна Алексеевна",
                "commodity_credit_days": 0,
                "products": [
                    {
                        "url": "https://api.datawiz.io/api/v1/purchase-documents/2017-01-11T16:49:41_20_MSA-00000705_67496/products/94558/",
                        "document_product_id": 94558,
                        "product_id": "4548",
                        "product_url": "https://api.datawiz.io/api/v1/products/4548/",
                        "price_total": "13.5000",
                        "qty": "3.0000",
                        "price": "4.5000"
                    },
                    {
                        "url": "https://api.datawiz.io/api/v1/purchase-documents/2017-01-11T16:49:41_20_MSA-00000705_67496/products/94557/",
                        "document_product_id": 94557,
                        "product_id": "4857",
                        "product_url": "https://api.datawiz.io/api/v1/products/4857/",
                        "price_total": "136.0400",
                        "qty": "4.0000",
                        "price": "34.0100"
                    },
                    {
                        "url": "https://api.datawiz.io/api/v1/purchase-documents/2017-01-11T16:49:41_20_MSA-00000705_67496/products/94556/",
                        "document_product_id": 94556,
                        "product_id": "4859",
                        "product_url": "https://api.datawiz.io/api/v1/products/4859/",
                        "price_total": "145.5200",
                        "qty": "4.0000",
                        "price": "36.3800"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/purchase-documents/(string: order_date)_(string: shop)_(string: document_number)_(string: identifier)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/purchase-documents/34_2017-07-05T14:11:36_351_7555405/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/purchase-documents/2018-03-21T10:48:48_44_S10-00007776_568711/",
        "document_id": "568711",
        "shop_id": "44",
        "shop_url": "https://api.datawiz.io/api/v1/shops/44/",
        "supplier_id": "17589",
        "supplier_url": "https://api.datawiz.io/api/v1/suppliers/17589/",
        "document_number": "S10-00007776",
        "receive_date": "2018-03-21T10:48:48",
        "order_date": "2018-03-21T10:48:48",
        "price_total": "44.1000",
        "items_qty": "2.0000",
        "responsible": "Чаюн Наталья Николаевна",
        "commodity_credit_days": 0,
        "products": [
            {
                "url": "https://api.datawiz.io/api/v1/purchase-documents/2018-03-21T10:48:48_44_S10-00007776_568711/products/5986697/",
                "document_product_id": 5986697,
                "product_id": "763530",
                "product_url": "https://api.datawiz.io/api/v1/products/763530/",
                "price_total": "20.1500",
                "qty": "1.0000",
                "price": "20.1500"
            },
            {
                "url": "https://api.datawiz.io/api/v1/purchase-documents/2018-03-21T10:48:48_44_S10-00007776_568711/products/5986696/",
                "document_product_id": 5986696,
                "product_id": "763517",
                "product_url": "https://api.datawiz.io/api/v1/products/763517/",
                "price_total": "23.9500",
                "qty": "1.0000",
                "price": "23.9500"
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
receive_date          строка       нет          Дата получения товара
order_date            строка       да           Дата заказа товара
price_total           число        да           Общая сумма товаров в заказе
items_qty             число        да           Общее количество товара в заказе
responsible           строка       нет          Ответственное лицо
commodity_credit_days число        да           Отсрочка
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


.. class:: POST /api/v1/purchase-documents/

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
receive_date          строка       нет          Дата получения товара
order_date            строка       да           Дата заказа товара
price_total           число        да           Общая сумма товаров в заказе
items_qty             число        да           Общее количество товаров в заказе
responsible           строка       нет          Ответственное лицо
commodity_credit_days число        нет          Отсрочка
products              список       да           Список товаров в заказе
===================== ============ ============ ===============================================

Уникальные поля: **order_date, shop_id, document_number, document_id**

Поля запроса для объекта ``products``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
product_id         строка       да           Идентификатор товара
price_total        число        да           Общая сумма товара
price              число        да           Цена товара
qty                число        да           Количество товара
================== ============ ============ ============================================================

Уникальные поля: **нет**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"shop_id": "44", "products": [{"price": "20.1500", "price_total": "20.1500", "product_id": "763530", "qty": "1.0000"}], "order_date": "2018-03-21T10:48:48", "supplier_id": "17589", "document_number": "S10-00007776", "responsible": "Якоб Фон Петрович", "items_qty": "28.0000", "document_id": "568711", "price_total": "628.2000"}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/purchase-documents/

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
    dw.upload_purchase_doc([{
        'shop_id': 44,
        'order_date': '2018-03-21T10:48:48',
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