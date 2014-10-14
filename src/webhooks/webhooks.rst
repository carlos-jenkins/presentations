===============
GitHub WebHooks
===============

*Acciones personalizadas al hacer PUSH a un repositorio.*

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Fecha: 9 de Octubre 2014


Agenda
======

- Acerca de GitHub.
- Acerca de GitHub WebHooks.
- Utilizando ``python-github-webhooks``.

  - Instalación.
  - Configurar Apache para GitHub webhooks.
  - [Opcional] Creación de llaves SSH.
  - Creación de un script personalizado.
  - Configuración del repositorio.
  - Probar mi hook.

- Preguntas.


Acerca de GitHub
================

https://github.com/

Sitio web para hosteo y gestión de proyectos de código abierto utilizando
el sistema de control de versiones Git. Es utilizado por mucho proyectos
de Software Libre, incluyendo el kernel Linux.

.. image:: images/github.png


Acerca de GitHub WebHooks
=========================

https://developer.github.com/webhooks/

Cada repositorio GitHub tiene la opción de comunicarse con un servidor web
cada vez que se hace PUSH a un repositorio. Estos "WebHooks" se pueden utilizar
para, por ejemplo:

- Actualizar un issue tracker.
- Lanzar un trabajo de Integración Continua.
- Actualizar un espejo de backup.
- Publicar al servidor de producción.


Acerca de ``python-github-webhooks``
====================================

Simple aplicación Python WSGI para manejar webhooks de GitHub.

    https://github.com/carlos-jenkins/python-github-webhooks

Requiere ser instalada en un servidor web con IP pública. Esta aplicación
permite ejecutar scripts en el directorio ``hooks`` utilizando el siguiente
order:

::

    hooks/{event}-{name}-{branch}
    hooks/{event}-{name}
    hooks/{event}
    hooks/all


Instalación
===========

.. code:: bash

    git clone git@github.com:carlos-jenkins/python-github-webhooks.git
    cd python-github-webhooks

Dependencias:

.. code:: bash

   sudo pip install -r requirements.txt


Configurar ``python-github-webhooks``
=====================================

Cambiar ``config.json``:

.. code:: json

    {
        "github_ips_only": false,
        "enforce_secret": "",
        "return_scripts_info": true
    }


Configurar Apache
=================

Agregar al sitio virtual una directiva ``WSGIScriptAlias``.

.. code:: apache

   <VirtualHost *:80>
       ServerAdmin you@my.site.com
       ServerName  my.site.com
       DocumentRoot /var/www/site.com/my/htdocs/

       # Handle GitHub webhook
       <Directory "/var/www/site.com/my/python-github-webhooks">
           Order deny,allow
           Allow from all
       </Directory>
       WSGIScriptAlias /webhooks /var/www/site.com/my/python-github-webhooks/webhooks.py

   </VirtualHost>


[Opcional] Crear llaves SSH
===========================

Éste paso es opcional. Es necesario si se quiere que los hooks puedan obtener
el repositorio vía SSH o bien si se quiere que puedan hacer push. Se puede
omitir si se obtiene el repositorio por HTTPS.

.. code:: bash

   sudo mkdir /var/www/.ssh
   sudo chown -R www-data:www-data /var/www/.ssh/
   sudo -H -u www-data ssh-keygen -t rsa
   cat /var/www/.ssh/id_rsa.pub

Y agregar dicha llave a:

    https://github.com/settings/ssh


Configurar repositorio
======================

A este punto se puede agregar el webhook en el repositorio:

    https://github.com/usuario/repositorio/settings/hooks

Y agregar como link el URL:

::

   http://mi.sitio.com/webhooks


Probar mi hook
==============

Vamos a utilizar el API REST de GitHub.

https://developer.github.com/v3/

.. code:: bash

   curl --user "youruser" https://api.github.com/repos/youruser/my.site.com/hooks

Tomar nota del "test_url".

.. code:: bash

   curl --user "youruser" -i -X POST [TEST_URL]

Cualquier error debe aparecer en los logs de Apache:

.. code:: bash

   sudo tail -f /var/log/apache2/error.log


Ejemplos
========

Auto-publicar un blog reST:

    http://carlos.jenkins.co.cr/2014/09/22/autodeploy-a-github-hosted-pelican-blog/


Preguntas
=========

¿Preguntas?

Muchas gracias.

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Web: http://carlos.jenkins.co.cr/
