===============================
oss-auth
===============================



.. image:: https://pyup.io/repos/github/timmartin19/houflask/shield.svg
     :target: https://pyup.io/repos/github/timmartin19/houflask/
     :alt: Updates


Basic authentication and authorization application



Documentation
-------------

You will need to install the package dependencies first,
see the Installation section for details.

To build and open the documentation simply run:

.. code-block:: bash

    bin/build-docs

Installation
------------

If you need to install pyenv/virtualenvwrapper you can run the ``bin/setup-osx`` command
Please note that this will modify your bash profile

Assuming you have virtualenv wrapper installed

.. code-block:: bash

    mkvirtualenv oss-auth
    workon oss-auth
    pip install -r requirements_dev.txt
    pip install -e .

Docker
""""""

If you want to use docker for this project

1. Download and install `Docker for Mac <https://docs.docker.com/docker-for-mac/>`_
2. In the root of this repo: ``docker-compose build``
3. ``docker-compose up``
4. Verify the application is running with: ``curl http://localhost:5000/status``

PyCharm
"""""""

To integrate PyCharm with your virtual environment

1. install according to the standard installation instructions
2. In your project settings (shortcut: ``cmd+,``) navigate to ``Project -> Project Interpreter``
3. Select the gear icon in the upper right corner
4. Select ``Add Local``
5. Select ``$HOME/.envs/oss-auth/bin/python3.5`` and click ``OK``
6. Click ``Apply`` and then ``OK``

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `timmartin19/oss-template@flask`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _timmartin19/oss-template@flask: https://github.com/timmartin19/oss-template/tree/flask

