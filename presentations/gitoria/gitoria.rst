=======
Gitoría
=======

*Gitoría: Git en la Inventoría.*

:Autor: Ing. Carlos Jenkins, HPE Networking R&D
:Email: carlos@jenkins.co.cr
:Fecha: 17 de Diciembre 2015

.. image:: images/inventoria.png


Agenda
======

- ¿Qué es un Sistema de Control de Versiones? (VCS)
- Acerca de Git, GitHub y GitLab.
- Glosario.
- Configuración básica.
- Flujo básico.
- Branching y rebasing.
- Tagging.
- Herramienta de diff.
- Preguntas.

Sistema de Control de Versiones
===============================

#. ¿Problemática?
#. ¿Soluciones?

Acerca de Git
=============

https://git-scm.com/

Sistema de control de versiones *distribuído* diseñado por Linus Torvals.
Inicia el 7 de Abril de 2005. Utilizado en todo el mundo, en proyectos
grandes y pequeños.

.. image:: images/git.png

Acerca de GitHub
================

https://github.com/

Sitio web para hosteo y gestión de proyectos de código abierto utilizando
el sistema de control de versiones Git. Es de código cerrado. Repositorios
privados son de pago. Es utilizado por mucho proyectos de Software Libre,
incluyendo el kernel Linux. Inicia el 10 de Abril de 2008.

.. image:: images/github.png

Acerca de GitLab
================

https://about.gitlab.com/

Sitio web para hosteo y gestión de proyectos de código abierto utilizando
el sistema de control de versiones Git. Es de código abierto. Se puede instalar
en su propio servidor o usar el servicio de ellos.
Inicia 24 de Octubre de 2011.

.. image:: images/gitlab.png

Glosario
========

:Repository: La carpeta con los archivos del proyecto y la base de datos
 de los cambios.
:Pull: *Jalar* los cambios.
:Push: *Empujar* los cambios.
:Commit: Crear una revisión.
:Branch: Crear una *ramificación* del proyecto.
:Merge: Incorporar o *mezclar* dos ramas.


Configuración básica
====================

#. Instalar y habilitar git.

   ::

       ssh-keygen -t rsa -b 4096 -C "correo@ejemplo.com"
       git config --global user.name "Nombre Persona"
       git config --global user.email correo@ejemplo.com"

#. Crear cuenta en GitHub

   https://github.com/

Flujo básico
============

::

    git clone
    git pull
    git add
    git commit
    git push

Branching y rebasing
====================

::

    git checkout -b xxxx
    git fetch
    git rebase

Tagging
=======

::

    git tag "0.1.0"
    git push --tags
    git tag --list

Herramienta de diff
===================

::

    sudo apt-get install meld
    git config --global diff.tool meld
    git config --global alias.difftree 'difftool --dir-diff'

Preguntas
=========

¿Preguntas?

Muchas gracias.

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Web: http://carlos.jenkins.co.cr/
