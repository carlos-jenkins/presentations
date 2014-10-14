========
confspec
========

*Framework gestor de configuración.*

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Fecha: 10 de Octubre 2014


Agenda
======

- Acerca de ``confspec``.
- Problemática y justificación.
- Características.
- Arquitectura.
- Ejemplos:

  - Básico.
  - Leer y escribir archivos de configuración.
  - Validar semántica de las opciones.
  - Habilitar *writeback*.
  - Agregar *callbacks*.

- Mejoras y trabajo futuro.
- Preguntas.


Acerca de ``confspec``
======================

http://confspec.readthedocs.org/

``confspec`` es un framework y biblioteca Python que permite a una aplicación
manejar sus opciones de configuración fácilmente y con seguridad.

Éste framework permite que se abstraiga los procesos de parseo, importación y
exportación de archivos de configuración así como los procesos de
parseo, casteo, conversión o interpretación y validación semántica de un
opción de configuración.


Problemática y justificación
============================

Se identificó un patrón que se repite constantemente en un gran cantidad de
aplicaciones cuando deben gestionar su configuración:

#. Leer archivo de configuración como string.
#. Parsear formato del archivo (INI, JSON, etc).
#. Iterar sobre las opciones y parsear el tipo de dato manualmente.
#. Verificar si el valor tiene semántico.


Características
===============

- Seguridad de tipo para cada opción de configuración.
- Seguridad semántica para cada opción de configuración.
- Capas de configuración apilables: sistema, entorno, usuario, las necesarias.
- Importación de múltiples archivos de configuración.
- Configuración disponible a nivel global de la aplicación.
- Patrón Observador (*Publisher-Listeners*).
- *Writeback* automático.
- Estado seguro y consistente. Cambio a estado seguro únicamente.
- Múltiples formatos de exportación: JSON, INI y diccionarios Python.


Características (cont.)
=======================

- Tipos de opciones personalizadas. ``confspec`` tiene un conjunto básico:

  - Entero (octal, hexadecimal, decimal), booleano, punto flotante, tiempo,
    fecha, fecha y tiempo, ruta de un sistema de archivos, directorio, archivo,
    clase, color, tipografía y otros. Además colecciones de esos elementos.

- Colección extensiva de funciones de validación.


Arquitectura
============

- ``ConfigOption``: Clase base proveedora de parseo e interpretación. Una lista
  de éstas crea una *especificación*.
- ``ConfigMg``: Administrador de la configuración: importación, exportación,
  notificación, etc.
- ``ConfigProxy``: Clase *proxy* para acceder y cambiar fácilmente la
  configuración.


Ejemplos
========

Para utilizar ``confspec`` se debe:

#. Definir una especificación.
#. Crear una administrador de dicha especificación.
#. Disfrutar la vida. ``confspec`` se va a encargar de todo lo demás.


Básico
======

Crear especificación:

.. code:: pycon

   >>> from confspec import *
   >>> spec = [
   ...     ConfigInt(key='myint', default=1),
   ...     ConfigBoolean(key='myboolean', default=True),
   ... ]
   >>> spec
   [1, True]


Básico (cont.)
==============

Crear manejador:

.. code:: pycon

   >>> confmg = ConfigMg(spec)
   >>> confmg.set('myint', 2)
   >>> confmg.get('myint')
   2
   >>> confmg.get('myboolean')
   True


Básico (cont.)
==============

Crear proxy:

.. code:: pycon

   >>> conf = confmg.get_proxy()
   >>> conf.myint
   2
   >>> conf.myint = 3
   >>> conf.myint
   3
   >>> print(confmg.do_export('ini'))
   [general]
   myboolean = True
   myint = 3


Leer y escribir archivos de configuración
=========================================

.. code:: pycon

   >>> confmg = ConfigMg(
   ...     spec, format='ini', create=False, load=False,
   ...     files=['/etc/myapp/default.ini', '~/.myapp/config.ini']
   ... )
   >>> confmg.load()
   >>> confmg.save()


Validar semántica de las opciones
=================================

.. code:: pycon

   >>> def valid_age(age):
   ...     return age > 1 and age < 110
   ...
   >>> from confspec import *
   >>> spec = [
   ...     ConfigInt(key='age', default=18, validator=valid_age),
   ... ]


Habilitar *writeback*
=====================

.. code:: pycon

   >>> confmg = ConfigMg(
   ...     spec, writeback=True, files=['~/.myapp/config.ini']
   ... )


Agregar *callbacks*
===================

.. code:: pycon

   >>> def mycallback(key, old_value, value):
   ...     print('New value for {}: was {}, now it is {}'.format(
   ...         key, old_value, value
   ...     ))
   ...
   >>> confmg.register_listener(mycallback, 'mydate')
   True
   >>> confmg.enable_notify(True)
   >>> conf.mydate
   datetime.datetime(2014, 9, 30, 17, 40, 20)
   >>> conf.mydate = now()


Mejoras y trabajo futuro
========================

- Agregar un proveedor de formato XML.
- Agregar un proveedor de formato YAML.
- Agregar un proveedor de formato SQLite.
- Agregar un proveedor de formato MySQL / MariaDB.
- Permitir a plugins registrar proveedores de formato y subclases de
  ``ConfigOption``.
- Integración con ``argparse``.


Preguntas
=========

¿Preguntas?

Muchas gracias.

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Web: http://carlos.jenkins.co.cr/
