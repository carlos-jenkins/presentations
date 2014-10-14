================
reStructuredText
================

*Lenguaje de marcado para documentación.*

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Fecha: 10 de Octubre 2014


Agenda
======

- Acerca de reST.
- Comparación de Markdown.
- Frameworks.

  - docutils.
  - Sphinx
  - Pelican

- Integración continua.
- Preguntas.


Acerca de reST
==============

Lenguaje de marcado tipo wiki.

- Text plano. Marcado simple.
- **Versionable.**
- Reside junto al código o en su propio repositorio.

Extenso:

   http://docutils.sourceforge.net/docs/user/rst/quickref.html


[reST] Títulos
==============

::

   =======
   Primero
   =======

   Segundo
   =======

   Tercero
   +++++++

   Cuarto
   ------


[reST] Decoradores
==================

+-----------------+-----------------+---------------+
| Enfasis         | ``*emph*``      | *emph*        |
+-----------------+-----------------+---------------+
| Enfasis fuerte  | ``**emph**``    | **emph**      |
+-----------------+-----------------+---------------+
| Literal         | ````literal```` | ``literal``   |
+-----------------+-----------------+---------------+


[reST] Vínculos
===============

+----------------------------------------------+-------------------------------------------+
| ::                                           | Link a Python_.                           |
|                                              |                                           |
|    Link a Python_.                           | .. _Python: http://www.python.org/        |
|                                              |                                           |
|    .. _Python: http://www.python.org/        | Link a `Python <http://www.python.org/>`_ |
|                                              |                                           |
|    Link a `Python <http://www.python.org/>`_ |                                           |
+----------------------------------------------+-------------------------------------------+


[reST] Listas numeradas
=======================

+---------------------------+------------------------+
| ::                        | - Lista no numerada.   |
|                           | - Lista no numerada.   |
|    - Lista no numerada.   |                        |
|    - Lista no numerada.   |   - Sub item.          |
|                           |                        |
|      - Sub item.          |                        |
|                           |                        |
+---------------------------+------------------------+


[reST] Listas no numeradas
==========================

+---------------------------+------------------------+
| ::                        | #. Lista numerada.     |
|                           | #. Lista numerada.     |
|    #. Lista numerada.     |                        |
|    #. Lista numerada.     |    #. Sub item.        |
|                           |                        |
|       #. Sub item.        |                        |
+---------------------------+------------------------+


[reST] Listas definiciones
==========================

+---------------------------+------------------------+
| ::                        | :Campo1: Definición 1. |
|                           | :Campo2: Definición 2. |
|    :Campo1: Definición 1. | :Campo3: Definición 3. |
|    :Campo2: Definición 2. |                        |
|    :Campo3: Definición 3. |                        |
|                           |                        |
+---------------------------+------------------------+


[reST] Tablas
=============

+-----------------------------------------+--------------------------------------+
| ::                                      | +----------+-----------+-----------+ |
|                                         | | Header 1 | Header 2  | Header 3  | |
|    +----------+-----------+-----------+ | +==========+===========+===========+ |
|    | Header 1 | Header 2  | Header 3  | | | row 1    | column 2  | column 3  | |
|    +==========+===========+===========+ | +----------+-----------+-----------+ |
|    | row 1    | column 2  | column 3  | | | row 2    | Multicolumn row.      | |
|    +----------+-----------+-----------+ | +----------+-----------+-----------+ |
|    | row 2    | Multicolumn row.      | | | row 3    | Cells may | - Cells   | |
|    +----------+-----------+-----------+ | +----------+ span      | - contain | |
|    | row 3    | Cells may | - Cells   | | | row 4    | rows      | - blocks. | |
|    +----------+ span      | - contain | | +----------+-----------+-----------+ |
|    | row 4    | rows      | - blocks. | |                                      |
|    +----------+-----------+-----------+ |                                      |
+-----------------------------------------+--------------------------------------+


[reST] Notas al pie
===================

::

   reST [#]_ es un lenguaje de marcado para documentación [*]_.

   .. [#] reStructuredText.
   .. [*] Nota al pie con autosímbolo.

reST [#]_ es un lenguaje de marcado para documentación [*]_.

.. [#] reStructuredText.
.. [*] Nota al pie con autosímbolo.


[reST] Directivas
=================

Mecanismo básico de extensibilidad.

::

   .. directiva:: argumento1, argumento2
      :opcion1: valor
      :opcion2: valor2

      contenido


[reST] Imágenes
===============

::

   .. image:: images/image.jpg

.. image:: images/image.jpg


Comparación con Markdown
========================

+-----------------+------------+-----------+
|                 | Markdown   | reST      |
+=================+============+===========+
| Formato         | HTML       | Muchos    |
+-----------------+------------+-----------+
| Especificación  | No         | Si        |
+-----------------+------------+-----------+
| Características | Limitadas  | Muchas    |
+-----------------+------------+-----------+
| Extensibilidad  | Ninguna    | Integrada |
+-----------------+------------+-----------+


Frameworks
==========

- docutils **(!)**:

  - Sistema base. Todos los demás frameworks se basan sobre éste.

- Sphinx:

  - Especializado en documentación de proyectos.

- Pelican:

  - Especializado en web y blogs.


docutils
========

http://docutils.sourceforge.net/rst.html

- Extensibilidad: directivas.
- Múltiples formatos de salida:

  - HTML (páginas web estáticas).

    - S5 (Estándar web para presentaciones).

  - LaTeX, XeTeX (para publicación, PDF).
  - XML (para post-procesado).
  - ODT (ofimática abierta).
  - MAN (manuales de sistema).


[docutils] Instalación
======================

.. code:: bash

   sudo apt-get install python-docutils


[docutils] Usar
===============

::

   rst2html.py -h
   rst2man.py -h
   rst2odt.py -h
   rst2s5.py -h
   rst2xml.py -h
   rst2latex.py -h
   rst2xetex.py -h

Por ejemplo:

.. code:: bash

   rst2s5.py --theme=small-white --stylesheet=style.css reST.rst reST.html


Sphinx
======

   http://sphinx-doc.org/

- Gestión para múltiples documentos.
- Sistema de plugins y temas web.
- ``autodoc`` para autodocumentación de código Python.


[Sphinx] Instalación
====================

.. code:: bash

   sudo apt-get install python-pip
   sudo pip install sphinx


[Sphinx] Usar
=============

::

   sphinx-quickstart
   sphinx-build


Pelican
=======

   http://getpelican.com/

- Especialización en web y en particular blogs.
- Publish content in multiple languages.
- Atom/RSS feeds.
- Code syntax highlighting.
- Import from WordPress, Dotclear, RSS feeds, and other services.


[Pelican] Instalación
=====================

.. code:: bash

   sudo apt-get install python-pip
   sudo pip install pelican


[Pelican] Usar
==============

::

   pelican-quickstart -h
   pelican-import -h
   pelican


Integración Continua
====================

:docutils: A la medida.
:Sphinx: ReadTheDocs.org https://readthedocs.org/
:Pelican: A la medida [#]_.

.. [#] http://carlos.jenkins.co.cr/2014/09/22/autodeploy-a-github-hosted-pelican-blog/


Preguntas
=========

¿Preguntas?

Muchas gracias.

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Web: http://carlos.jenkins.co.cr/
