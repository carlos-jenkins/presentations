==========
Frog Croak
==========

*Monitoreo de la velocidad de Internet en casa o lugar de trabajo.*

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Fecha: 9 de Octubre 2014


Agenda
======

- Problemática.
- Acerca de Frog-Croak.
- Utilización del visualizador.
- Instalación del visualizador.
- Configuración del visualizador.
- Instalación del colector.
- Configuración del tiempo de muestreo.
- Corriendo en máquinas distintas.
- Preguntas.


Problemática
============

- *"Aló? Soporte técnico? El Internet está lento!..."*
- *"Mi proveedor no me está dando lo que estoy pagando..."*
- *"El Internet funciona bien excepto en horas pico..."*


Acerca de Frog-Croak
====================

https://github.com/carlos-jenkins/frog-croak/

Frog Croak es una herramienta que permite a los usuario monitorear y analizar
la velocidad de su conexión a Internet en el tiempo. Lo componen dos elementos:

- **Visualizador**: Permite ver y analizar los datos en el tiempo.
- **Colector**: Permite tomar muestras de la velocidad de internet.

Para un demo en vivo visitar: http://speed.jenkins.co.cr/


Utilización del visualizador
============================




Instalación del visualizador
============================

Se requiere un servidor web:

.. code:: bash

   wget https://github.com/carlos-jenkins/frog-croak/archive/master.zip -O frog-croak.zip
   unzip frog-croak.zip
   mv frog-croak-master/viewer/ [install path]


Configuración del visualizador
==============================

Se configura por medio del archivo ``config.json``:

.. code:: json

    {
        "data": "data.csv",
        "lang" : "en",
        "title": "Internet Speed Test Log",
        "organization": "My Organization",
        "download_contracted": 5.0,
        "download_guaranteed": 0.8,
        "upload_contracted": 1.0,
        "upload_guaranteed": 0.8
    }


Instalación del colector
========================

.. code:: bash

   sudo apt-get install python-pip
   sudo pip install frog-croak

Para tomar una muestra se ejecuta:

.. code:: bash

   $ frog-croak


Configuración del tiempo de muestreo
====================================

Se utiliza cron para programar el tiempo de muestreo:

.. code:: bash

   $ sudo crontab -u www-data -e
    50 * * * * /usr/local/bin/frog-croak --output /var/www/html/speed/data.csv

En el ejemplo anterior se programa para que se tome una muestra cada hora al
minuto 50 y se guarden las muestras en el archivo
``/var/www/html/speed/data.csv``.


Corriendo en máquinas distintas
===============================

El colector y el visualizador es muy normal que se encuentren en máquinas
distintas. Por ejemplo, el colector puede estar instalado en un Raspberry PI
o un BeagleBone Black en la casa o lugar en el cual se quiere monitorear
la velocidad de internet, mientras que el visualizador puede estar en un
servidor web externo, un VPS o en otra localidad física.


Corriendo en máquinas distintas (cont.)
=======================================

Para ello se crea un script que copie el archivo de muestras cada vez que toma
una.

.. code:: bash

    $ cat /home/myuser/speed/speed.sh
    #!/bin/bash
    set -e

    # Env variables
    PATH=/usr/local/bin:/usr/bin:/bin

    cd /home/myuser/speed
    frog-croak --silent
    scp data.csv external:/var/www/html/speed/


Preguntas
=========

¿Preguntas?

Muchas gracias.

:Autor: Carlos Jenkins
:Email: carlos@jenkins.co.cr
:Web: http://carlos.jenkins.co.cr/
