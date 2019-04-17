Поставщики
==========

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/suppliers/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/suppliers/

Пример ответа:

.. code-block:: json

    {
        "count": 33350,
        "next": "https://api.datawiz.io/api/v1/suppliers/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/suppliers/15930/",
                "supplier_id": "15930",
                "name": "Большакова Мария Константиновна",
                "supplier_code": "37431162",
                "phone": "060 290-88-32",
                "commodity_credit_days": 0,
                "address": "к. Сортавала, ул. Хуторская, д. 90, 927594"
            },
            {
                "url": "https://api.datawiz.io/api/v1/suppliers/15932/",
                "supplier_id": "15932",
                "name": "Дементьева Алевтина Юльевна",
                "supplier_code": "36809856",
                "phone": "+38 066 783-24-36",
                "commodity_credit_days": 0,
                "address": "с. Уварово, ул. Серова, д. 20, 713182"
            },
            {
                "url": "https://api.datawiz.io/api/v1/suppliers/15933/",
                "supplier_id": "15933",
                "name": "Виноградов Измаил Трофимович",
                "supplier_code": "38880574",
                "phone": "065 682-09-60",
                "commodity_credit_days": 0,
                "address": "п. Ярославль, ул. Медицинская, д. 45, 218281"
            }
        ]
    }

.. class:: GET /api/v1/suppliers/(string: supplier_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/suppliers/15930/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/suppliers/15930/",
        "supplier_id": "15930",
        "name": "Большакова Мария Константиновна",
        "supplier_code": "37431162",
        "phone": "060 290-88-32",
        "commodity_credit_days": 0,
        "address": "к. Сортавала, ул. Хуторская, д. 90, 927594"
    }

Поля ответа:

====================== ============ ============ ===========================
Поле                   Тип          Обязательное Описание
====================== ============ ============ ===========================
url                    строка       да           Ссылка на объект
supplier_id            строка       да           Идентификатор поставщика
name                   строка       да           Имя поставщика
supplier_code          строка       нет          Код поставщика
phone                  строка       нет          Номер телефона поставщика
commodity_credit_days  число        да           Отсрочка в днях
address                строка       нет          Адресс поставщика
====================== ============ ============ ===========================

.. class:: POST /api/v1/suppliers/

**REST API**

Добавить объект.

Поля запроса:

====================== ============ ============ ===========================
Поле                   Тип          Обязательное Описание
====================== ============ ============ ===========================
supplier_id            строка       да           Идентификатор товара
name                   строка       да           Имя поставщика
supplier_code          строка       нет          Код поставщика
phone                  строка       нет          Номер телефона поставщика
commodity_credit_days  число        нет          Отсрочка в днях
address                строка       нет          Адресс поставщика
====================== ============ ============ ===========================

Уникальные поля: **supplier_id**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'supplier_id=777&name=Шмигельский Роман' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/suppliers/

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
    dw.upload_suppliers([{
        'supplier_id': 777,
        'name': 'Шмигельский Роман'
    }])