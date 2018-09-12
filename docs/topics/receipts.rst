Чеки
====

Обязательно к заполнению: **Да**

.. class:: GET /api/v1/receipts/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/receipts/

Пример ответа:

.. code-block:: json

    {
        "count": 15182303,
        "next": "https://api.datawiz.io/api/v1/receipts/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T14:11:36_351_7555405/",
                "shop_id": "34",
                "shop_url": "https://api.datawiz.io/api/v1/shops/34/",
                "terminal_id": "351",
                "terminal_url": "https://api.datawiz.io/api/v1/terminals/351/",
                "order_id": "7555405",
                "date_open": "2017-07-05T14:11:21",
                "date": "2017-07-05T14:11:36",
                "cashier_id": "24",
                "cashier_url": "https://api.datawiz.io/api/v1/cashiers/24/",
                "contractor_id": null,
                "contractor_url": null,
                "loyalty_id": null,
                "loyalty_url": null,
                "markers": [],
                "bulk": false,
                "refund": false,
                "cartitems": [
                    {
                        "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T14:11:36_351_7555405/cartitems/196.0/",
                        "order_no": "196.0",
                        "product_id": "48620",
                        "product_url": "https://api.datawiz.io/api/v1/products/48620/",
                        "base_price": "23.9500",
                        "price": "23.8610",
                        "qty": "1.0000",
                        "discount": "0.0000",
                        "total_price": "23.8610",
                        "original_price": "21.3600",
                        "margin_price_total": "2.5010"
                    }
                ]
            },
            {
                "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T15:29:32_352_7580087/",
                "shop_id": "34",
                "shop_url": "https://api.datawiz.io/api/v1/shops/34/",
                "terminal_id": "352",
                "terminal_url": "https://api.datawiz.io/api/v1/terminals/352/",
                "order_id": "7580087",
                "date_open": "2017-07-05T15:29:25",
                "date": "2017-07-05T15:29:32",
                "cashier_id": "23",
                "cashier_url": "https://api.datawiz.io/api/v1/cashiers/23/",
                "contractor_id": null,
                "contractor_url": null,
                "loyalty_id": "234",
                "loyalty_url": "https://api.datawiz.io/api/v1/loyalty/234/",
                "markers": [],
                "bulk": false,
                "refund": false,
                "cartitems": [
                    {
                        "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T15:29:32_352_7580087/cartitems/2194.0/",
                        "order_no": "2194.0",
                        "product_id": "11636",
                        "product_url": "https://api.datawiz.io/api/v1/products/11636/",
                        "base_price": "8.7900",
                        "price": "8.1960",
                        "qty": "1.0000",
                        "discount": "0.0000",
                        "total_price": "8.1960",
                        "original_price": "7.6200",
                        "margin_price_total": "0.5760"
                    },
                    {
                        "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T15:29:32_352_7580087/cartitems/2193.0/",
                        "order_no": "2193.0",
                        "product_id": "81429",
                        "product_url": "https://api.datawiz.io/api/v1/products/81429/",
                        "base_price": "13.7200",
                        "price": "12.4014",
                        "qty": "1.0000",
                        "discount": "0.0000",
                        "total_price": "12.4014",
                        "original_price": "12.4800",
                        "margin_price_total": "-0.0786"
                    }
                ]
            }
        ]
    }

.. class:: GET /api/v1/receipts/(string: shop_id)_(string: date)_(string: terminal_id)_(string: order_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/receipts/34_2017-07-05T14:11:36_351_7555405/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T14:11:36_351_7555405/",
        "shop_id": "34",
        "shop_url": "https://api.datawiz.io/api/v1/shops/34/",
        "terminal_id": "351",
        "terminal_url": "https://api.datawiz.io/api/v1/terminals/351/",
        "order_id": "7555405",
        "date_open": "2017-07-05T14:11:36",
        "date": "2017-07-05T14:11:36",
        "cashier_id": "24",
        "cashier_url": "https://api.datawiz.io/api/v1/cashiers/24/",
        "contractor_id": null,
        "contractor_url": null,
        "loyalty_id": null,
        "loyalty_url": null,
        "markers": [],
        "bulk": false,
        "refund": false,
        "cartitems": [
            {
                "url": "https://api.datawiz.io/api/v1/receipts/34_2017-07-05T14:11:36_351_7555405/cartitems/196.0/",
                "order_no": "196.0",
                "product_id": "48620",
                "product_url": "https://api.datawiz.io/api/v1/products/48620/",
                "base_price": "23.9500",
                "price": "23.8610",
                "qty": "1.0000",
                "discount": "0.0000",
                "total_price": "23.8610",
                "original_price": "21.3600",
                "margin_price_total": "2.5010"
            }
        ]
    }


Поля ответа:

============== ============ ============ ===============================================
Поле           Тип          Обязательное Описание
============== ============ ============ ===============================================
url            строка       да           Ссылка на объект
shop_id        строка       да           Идентификатор магазина
shop_url       строка       да           Ссылка на объект магазина
terminal_id    строка       да           Идентификатор кассы
terminal_url   строка       да           Ссылка на объект кассы
order_id       строка       да           Идентификатор чека
date_open      строка       да           Дата открытия чека
date           строка       да           Дата закрытия чека
cashier_id     строка       нет          Идентификатор кассира
cashier_url    строка       нет          Ссылка на объект кассира
contractor_id  строка       нет          Идентификатор оптовика
contractor_url строка       нет          Ссылка на объект оптовика
loyalty_id     строка       нет          Идентификатор клиента программы лояльности
loyalty_url    строка       нет          Ссылка на объект клиента программы лояльности
markers        список       да           Список меток чеков
bulk           логический   да           Оптовая продажа
refund         логический   да           Возврат
cartitems      список       да           Список позиций в чеке
============== ============ ============ ===============================================

Поля ответа в списке ``cartitems``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
url                строка       да           Идентификатор акции
order_no           число        да           Порядковый номер позиции в чеке
product_id         строка       да           Идентификатор товара
product_url        строка       да           Ссылка на объект товара
base_price         число        да           Цена товара без учета скидки
price              число        да           Реальная цена товара
qty                число        да           Количество товара
discount           число        да           Скидка
total_price        число        да           Общая стоимость позиции
original_price     число        да           Себестоимость товара
margin_price_total число        да           Общая прибыль позиции
================== ============ ============ ============================================================


.. class:: POST /api/v1/receipts/

**REST API**

Добавить объект.

Поля запроса:

============== ============ ============ ===========================================
Поле           Тип          Обязательное Описание
============== ============ ============ ===========================================
shop_url       строка       да           Идентификатор магазина
terminal_id    строка       да           Идентификатор кассы
order_id       строка       да           Идентификатор чека
date_open      строка       нет          Дата открытия чека
date           строка       да           Дата закрытия чека
cashier_id     строка       нет          Идентификатор кассира
contractor_id  строка       нет          Идентификатор оптовика
loyalty_id     строка       нет          Идентификатор клиента программы лояльности
bulk           логический   нет          Оптовая продажа
refund         логический   нет          Возврат
cartitems      список       да           Список позиций в чеке
============== ============ ============ ===========================================

Уникальные поля: **shop_id, date, terminal, order_id**

Поля запроса для объекта ``cartitems``:

================== ============ ============ ============================================================
Поле               Тип          Обязательное Описание
================== ============ ============ ============================================================
order_no           число        да           Порядковый номер позиции в чеке
product_id         строка       да           Идентификатор товара
product_url        строка       да           Ссылка на объект товара
base_price         число        нет          Цена товара без учета скидки
price              число        да           Реальная цена товара
qty                число        да           Количество товара
discount           число        нет          Скидка
total_price        число        да           Общая стоимость позиции
original_price     число        да           Себестоимость товара
margin_price_total число        да           Общая прибыль позиции
================== ============ ============ ============================================================

Уникальные поля: **order_no**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d '{"shop_id": "23", "terminal_id": "358", "order_id": "919501", "date_open": "2017-07-05T19:54:35", "date": "2017-07-05T19:54:39", "cashier_id": "1409", "cartitems": [ {"order_no": "1", "product_id": "48620", "base_price": "22.9900", "price": "24.8477", "qty": "1.0000", "discount": "0.0000", "total_price": "24.8477", "original_price": "21.3600", "margin_price_total": "3.4877"}]}' -H "Content-Type: application/json" -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/receipts/

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
    dw.upload_receipts([{
        "shop_id": "23",
        "terminal_id": "358",
        "order_id": "919501",
        "date_open": "2017-07-05T19:54:35",
        "date": "2017-07-05T19:54:39",
        "cashier_id": "1409",
        "cartitems": [
            {
                "order_no": "1",
                "product_id": "48620",
                "base_price": 22.9900,
                "price": 24.8477,
                "qty": 1.0000,
                "total_price": 24.8477,
                "original_price": 21.3600,
                "margin_price_total": 3.4877
            }
        ]
    }])