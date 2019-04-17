Авторизация
===========

REST API
--------
Для авторизации рекомендуется использовать протокол OAuth 2.0
Он работает по очень простой схеме, которую можно представить в два этапа:

- Авторизация пользователя
- Получение токена для доступа к защищенным ресурсам

Каждая команда REST API должна быть подписана – это значит что она должна иметь информацию при помощи которой REST API аутентифицирует её. В данном случае эту функцию выполняет специальный токен, полученый в процессе авторизации пользователя. Протокол OAuth 2.0 представляет несколько возможностей для получения этого токена, в даном примере мы будем использовать самый простой метод, который предполагает явное указание данных пользователя.

Пример запроса на curl:

.. code-block:: bash

    $ curl -X POST -d "client_id=<client_id>&client_secret=<client_secret>&grant_type=password&username=<your username>&password=<your password>" https://api.datawiz.io/api/o/token/

Пример ответа:

.. code-block:: json

    {
       "access_token":"MRUJl5YsxnABuwagopje1HrTvvmb1M",
       "token_type":"Bearer",
       "expires_in":36000,
       "refresh_token":"AYyg8EPgVUNfshFio3vd7Mo2w6WRnC",
       "scope":"read write"
    }

Python клиент
-------------
Пример авторизации через Python клиент:

.. code-block:: python

    from dwapi.datawiz import DW, Up_DW

    # Объект класса `DW` отвечает за получение данных с сервиса
    dw = DW(API_KEY='<your key>', API_SECRET='<your secret>')

    # Объект класса `Up_DW` отвечает за загрузку данных на сервис
    up_dw = Up_DW(API_KEY='<your key>', API_SECRET='<your secret>')
