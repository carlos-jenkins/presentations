========================
Python AsyncIO and PyZMQ
========================

*Escribir código seguro y escalable fácilmente*

.. image:: images/python.svg

:Autor: Carlos Jenkins, KuraLabs S.R.L
:Email: carlos.jenkins@kuralabs.io
:Fecha: 26 de Julio, 2018


Introduction
============

A partir de Python 3.4* se introdujo `AsyncIO`_, con conjunto de bibliotecas
y mejoras al lenguaje que permiten procesamiento asíncrono*.

Compararemos modelos de concurrencia tradicionales como threading y
multiprocess con el basado en event loops, así como algunos frameworks que nos
ayudarán a crear RESTful APIs rápidamente y de forma segura.

Agenda
======

- ¿Qué es AsyncIO?
- Async/Await.
- Comparación con otros modelos de concurrencia.
- HTTP con AsyncIO.
- Bonus: Validación de Schema.
- Bases de datos con AsyncIO.
- Comunicación entre procesos.
- ProTips.
- Escalando con AsyncIO.
- Preguntas.


¿Qué es AsyncIO?
================

`AsyncIO`_ es un con conjunto de bibliotecas y mejoras al lenguaje que permiten
procesamiento asíncrono*.

Nos concentraremos en Async/Await, que es una forma de escribir código
asíncrono que parece síncrono.

A una función `async` se le conoce como una co-rutina.

.. _AsyncIO: https://docs.python.org/3/library/asyncio.html

Async/Await
===========

.. code:: python3

   async def hello_world():
       await some_future()


Comparación con otros modelos de concurrencia
=============================================

+------------------------+------+--------------------+-----------------------+
| Modelo de Concurrencia | CPUs | Cambio de Contexto | Criterio              |
+========================+======+====================+=======================+
| `Threading`_           | 1    | Python Interpreter | 10ms, 100 byte codes, |
| (In Python)            |      | (`GIL`_, CPython)* | sleep()               |
+------------------------+------+--------------------+-----------------------+
| `Multiprocessing`_     | n    | Kernel Scheduler   | Black Magic           |
|                        |      | (Linux, `CFS`_)*   | (`CFS`_)              |
+------------------------+------+--------------------+-----------------------+
| `AsyncIO`_             | 1    | Event Loop         | await                 |
+------------------------+------+--------------------+-----------------------+

.. _Threading: https://docs.python.org/3/library/threading.html
.. _Multiprocessing: https://docs.python.org/3/library/multiprocessing.html
.. _GIL: https://realpython.com/python-gil/
.. _CFS: https://en.wikipedia.org/wiki/Completely_Fair_Scheduler


Threading
=========

.. image:: images/threading.svg


Multiprocessing
===============

.. image:: images/multiprocessing.svg


Async
=====

.. image:: images/async.svg


HTTP con AsyncIO
================

.. code:: python3

   from aiohttp import web

   app = web.Application(middlewares=middlewares)
   app['conf'] = parse_config(args.conf)
   app.on_startup.append(setup_db)

   app.router.add_get(
       '/voter/name/{name}/{province_filter:\d+}/{page:\d+}',
       handler_name
   )
   web.run_app(app, path=args.path)

.. _AIOHTTP: https://aiohttp.readthedocs.io/


HTTP con AsyncIO (2)
====================

.. code:: python3

   async def handler_name(request):
       web.json_response({'hello': 'world'})


Bonus: Validación de Schema
===========================

Es fácil crear un middleware que valide solicitudes y respuestas basados en un
esquema que valide no sólo el tipo de dato pero la semántica del dato.

`Cerberus`_:

.. code:: python3

   from cerberus import Validator

   validator = Validator(schema)
   validated = validator.validated(data)
   errors = validator.errors

.. _Cerberus: http://docs.python-cerberus.org/

Bonus: Validación de Schema (2)
===============================

.. code:: python3

   SCHEMA_NAME_REQUEST = {
       'name': {
           'required': True,
           'type': 'string',
           'empty': False,
       },
       'province_filter': {
           'required': False,
           'default': 0,
           'type': 'integer',
           'coerce': int,
           'min': 0,
           'max': 8,
       },
       'page': {
           'required': False,
           'default': 0,
           'type': 'integer',
           'coerce': int,
           'min': 0,
           'max': 100,
       },
   }

Bases de datos con AsyncIO
==========================

=============   ========================   ==============
 DBMS            Tipo                       Driver
=============   ========================   ==============
 `MySQL`_        Relational                 `AIOMySQL`_
 `MongoDB`_      Document Oriented          `Motor`_
 `InfluxDB`_     Time Series                `AioInflux`_
=============   ========================   ==============

.. _Motor: https://motor.readthedocs.io/
.. _MongoDB: https://www.mongodb.com/
.. _AIOMySQL: http://aiomysql.readthedocs.io/
.. _MySQL: https://www.mysql.com/
.. _AioInflux: https://github.com/plugaai/aioinflux
.. _InfluxDB: https://www.influxdata.com/

Comunicación entre procesos
===========================

**PyZMQ**: Super-sockets. Multiple topologies, buffered, async.

.. code:: python3

   from zmq.asyncio import Context
   from zmq import PUSH

   async def setup(app):
       mysocket = Context.instance().socket(PUSH)
       mysocket.connect(app['conf']['mysocket']['path'])
       app['mysocket'] = mysocket

   # ...
   app['conf'] = parse_config(args.conf)
   app.on_startup.append(setup)

.. _PyZMQ: https://pyzmq.readthedocs.io/

Comunicación entre procesos (2)
===============================

**PUSH**:

.. code:: python3

   from umsgpack import packb

   mysocket = request.app['mysocket']
   data = {
       'time': time(),
   }
   await mysocket.send(packb(data))


Comunicación entre procesos (3)
===============================

**PULL**:

.. code:: python3

   from asyncio import get_event_loop

   loop = get_event_loop()
   try:
       loop.run_until_complete(consume(path))
   finally:
       loop.close()


Comunicación entre procesos (4)
===============================

.. code:: python3

   from zmq import PULL
   from umsgpack import unpackb

   async def consume(path):
       mysocket = Context.instance().socket(PULL)
       socket.bind(path)

       while KEEP_RUNNING:
           events = await mysocket.poll()
           for _ in range(events):
               frame = await mysocket.recv(copy=False)
               print(unpackb(frame))
       socket.close()


ProTips
=======

- Usar el event loop ultra-rápido `uvloop`_.
- Usar el (de)serializador ultra-rápido `ujson`_.
- Cambiar el nombre del proceso `setproctitle`_.
- Usar un formato de serialización rápido y eficiente para la comunicación
  entre procesos como `msgpack`_ (or `bson`_).
- Crear un esquema para solicitudes (requests) y respuestas
  (responses). Tomar en cuenta headers, body, query params.
  Loggear como grave si la validación del esquema de respuesta falla.

.. _uvloop: http://uvloop.readthedocs.io/
.. _ujson: https://pypi.org/project/ujson/
.. _setproctitle: https://pypi.org/project/setproctitle/
.. _msgpack: https://github.com/vsergeev/u-msgpack-python
.. _bson: https://github.com/py-bson/bson


Escalando con AsyncIO
=====================

`Supervisor`_: Gestión de procesos.

.. code:: text

   [program:myapp]
   numprocs = NUM_CPUS
   numprocs_start = 1

   ; Unix socket paths are specified by command line.
   command=myapp -vvv \
     --path=/var/run/myapp/myapp_%(process_num)s.sock \
     --conf=/etc/myapp/myapp.toml

.. _Supervisor: http://supervisord.org/


Escalando con AsyncIO (2)
=========================

**NGINX**: ``/etc/nginx/sites-available/myapp``

.. code:: text

   upstream myapp {
       # fail_timeout=0 means we always retry an upstream even
       # if it failed to return a good HTTP response

       # Unix domain servers
       server unix:/var/run/myapp/myapp_1.sock fail_timeout=0;
       server unix:/var/run/myapp/myapp_2.sock fail_timeout=0;
       server unix:/var/run/myapp/myapp_3.sock fail_timeout=0;
       server unix:/var/run/myapp/myapp_4.sock fail_timeout=0;
   }


Escalando con AsyncIO (3)
=========================

**NGINX**: ``/etc/nginx/sites-available/myapp``

.. code:: text

   server {
       listen 80;
       # ...

       location / {
           proxy_set_header Host $http_host;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_redirect off;
           proxy_buffering off;
           proxy_pass http://myapp;
       }
   }

Escalando con AsyncIO (4)
=========================

Nuestros resultados:

- Respuestas por debajo de los 10ms con lookup en base de datos.
- 160 000 consultas en 24 horas.
  1.85 requests por segundo.
  Pico de 30 requests por segundo.
- 16 CPU cores / 300GB RAM VPS, máximo de carga de ~25%.
  16 instancias.
  1 base de datos read only.
  1 base de datos write time series "drop and run".


¿Preguntas?
===========

Muchas gracias.

https://carlos.jenkins.co.cr/presentations/asyncio_pyzmq

:Autor: Carlos Jenkins, KuraLabs S.R.L
:Email: carlos.jenkins@kuralabs.io
:Web: https://kuralabs.io/
