Вступление
==========
DatawizAPI - интерфейс для загрузки данных на сервис для анализа данных.

REST API
--------
API разработан используя технологию `REST <https://ru.wikipedia.org/wiki/REST>`_ для простого взаимодействия между клиентом и сервером посредством HTTP-запросов, где необходимые данные передаются в качестве параметров запроса.

Взаимодействовать с REST API можно также посредством браузера, перейдя по `ссылке <https://api.datawiz.io/api-auth/login/?next=/api/v1/>`_.

Python клиент
-------------
Клиент предназначен для высокоуровневого взаимодействия с REST API, не работая напрямую с HTTP-запросами.

Установка Python клиента
~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    pip install -U git+https://github.com/datawizio/pythonAPI.git

Логирование
~~~~~~~~~~~
Для отслеживания стадии загрузки можно передать параметром ``log`` собственный логгер в конструктор классов DW, Up_DW и Auth.

.. code-block:: python

    import logging
    from dwapi.datawiz_upload import Up_DW

    logger = logging.getLogger(__name__)

    dw = Up_DW(API_KEY='test1@mail.com', API_SECRET='1qaz', log=logger)