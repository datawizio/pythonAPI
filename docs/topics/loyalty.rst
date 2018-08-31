Клиенты программы лояльности
============================

Обязательно к заполнению: **Нет**

.. class:: GET /api/v1/loyalty/


Получить список объектов.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/loyalty/

Пример ответа:

.. code-block:: json

    {
        "count": 189696,
        "next": "https://api.datawiz.io/api/v1/loyalty/?page=2",
        "previous": null,
        "results": [
            {
                "url": "https://api.datawiz.io/api/v1/loyalty/412986/",
                "loyalty_id": "412986",
                "group_id": null,
                "client_birthday": "1986-09-20",
                "first_visit": "2017-03-22T00:00:00",
                "cardno": "5424616902717537",
                "discount": "0.00",
                "client_name": "Давыдов Эмиль Брониславович",
                "is_male": false,
                "age": null,
                "last_visit": "2018-01-29T00:00:00",
                "phone": "063 650 33 19",
                "email": "mzhukov@rambler.ru",
                "address": "ул. Моховая, д. 54"
            },
            {
                "url": "https://api.datawiz.io/api/v1/loyalty/451417/",
                "loyalty_id": "451417",
                "group_id": null,
                "client_birthday": "1988-08-16",
                "first_visit": "2017-09-07T00:00:00",
                "cardno": "501876051290",
                "discount": "0.00",
                "client_name": "тов. Чернов Тихон Вилорович",
                "is_male": false,
                "age": null,
                "last_visit": "2017-09-07T00:00:00",
                "phone": "+38 092 878-57-98",
                "email": "poljakovmilan@hotmail.com",
                "address": "ул. Минская, д. 47"
            },
            {
                "url": "https://api.datawiz.io/api/v1/loyalty/340996/",
                "loyalty_id": "340996",
                "group_id": null,
                "client_birthday": "2011-08-22",
                "first_visit": "2017-06-06T00:00:00",
                "cardno": "6011470970396734",
                "discount": "0.00",
                "client_name": "Поляков Мина Якубович",
                "is_male": false,
                "age": null,
                "last_visit": "2017-06-06T00:00:00",
                "phone": "405 41 05",
                "email": "rozhkovalidija@yandex.ru",
                "address": "ул. Тихая, д. 94"
            }
        ]
    }

.. class:: GET /api/v1/loyalty/(string: loyalty_id)/


Получить объект.

**REST API**

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -H "Authorization: Bearer dG9KDQWe2IGUs9Bun8w71UuCZUKZQX" https://api.datawiz.io/api/v1/loyalty/412986/

Пример ответа:

.. code-block:: json

    {
        "url": "https://api.datawiz.io/api/v1/loyalty/412986/",
        "loyalty_id": "412986",
        "group_id": null,
        "client_birthday": "1986-09-20",
        "first_visit": "2017-03-22T00:00:00",
        "cardno": "5424616902717537",
        "discount": "0.00",
        "client_name": "Давыдов Эмиль Брониславович",
        "is_male": false,
        "age": null,
        "last_visit": "2018-01-29T00:00:00",
        "phone": "063 650 33 19",
        "email": "mzhukov@rambler.ru",
        "address": "ул. Моховая, д. 54"
    }

Поля ответа:

=============== ============ ============ ====================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ====================================
url             строка       да           Ссылка на объект
loyalty_id      строка       да           Идентификатор клиента
group_id        строка       нет          Идентификатор группы
client_birthday строка       нет          Дата рождения
first_visit     строка       нет          Дата первого визита
cardno          строка       да           Номер карты
discount        число        нет          Скидка клиента, %
client_name     строка       да           Имя клиента
is_male         логический   нет          Мужчина
age             число        нет          Возраст
phone           строка       нет          Номер телефона
email           строка       нет          Почта
address         строка       нет          Адресс
=============== ============ ============ ====================================

.. class:: POST /api/v1/loyalty/

**REST API**

Добавить объект.

Поля запроса:

=============== ============ ============ ================================
Поле            Тип          Обязательное Описание
=============== ============ ============ ================================
loyalty_id      строка       да           Идентификатор клиента
group_id        строка       нет          Идентификатор группы
client_birthday строка       нет          Дата рождения
first_visit     строка       нет          Дата первого визита
cardno          строка       да           Номер карты
discount        число        нет          Скидка клиента, %
client_name     строка       да           Имя клиента
is_male         логический   нет          Мужчина
age             число        нет          Возраст
phone           строка       нет          Номер телефона
email           строка       нет          Почта
address         строка       нет          Адресс
=============== ============ ============ ================================

Пример запроса используя полученный ``access_token`` после авторизации:

.. code-block:: bash

    $ curl -d 'loyalty_id=777&client_name=Киселица Василий Васильевич&cardno=9845344534867234' -H "Authorization: Bearer jhMisdKPKo9hXeTuSvqFd2TL7vel62" -X POST https://api.datawiz.io/api/v1/loyalty/

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
    dw.upload_loyalty([{
        'loyalty_id': 777,
        'client_name': 'Киселица Василий Васильевич',
        'cardno': '9845344534867234'
    }])