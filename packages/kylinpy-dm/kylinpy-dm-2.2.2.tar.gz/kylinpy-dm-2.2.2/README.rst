.. image:: https://img.shields.io/pypi/v/kylinpy.svg
   :target: https://pypi.python.org/pypi/kylinpy

Apache Kylin Python Client Library
==================================
Apache Kylin Python Client Library is a python-based Apache Kylin client.

There are two components in Apache Kylin Python Client Library.

* Apache Kylin python command line:

  This component provides a unified command line interface to Apache Kylin.

* Apache Kylin dialect for SQLAlchemy:

  Any application that uses SQLAlchemy can now query Apache Kylin with this Apache Kylin dialect installed.

The two components above are based on Apache Kylin python client.

Installation
------------

The easiest way to install Apache Kylin Python Client Library is to use pip::

    pip install --upgrade kylinpy

Alternatiely, you may install this library from local project path,
You are welcomed to also commit to this library::

    git clone https://github.com/Kyligence/kylinpy.git
    pip install -e kylinpy

Apache Kylin python Command Line
--------------------------------
After installing Apache Kylin Python Client Library you may run kylinpy in terminal::

    kylinpy
    Usage: kylinpy [OPTIONS] COMMAND [ARGS]...

    Options:
      -h, --host TEXT       kylin/kap host name  [required]
      -P, --port INTEGER    kylin/kap port, default: 7070
      -u, --username TEXT   kylin/kap username  [required]
      -p, --password TEXT   kylin/kap password  [required]
      --project TEXT        kylin/kap project  [required]
      --prefix TEXT         kylin/kap RESTful prefix of url, default: /kylin/api
      --debug / --no-debug  show debug infomation
      --api2 / --api1       API version; default is api1; --api1 used by Apache KYLIN;
                        --api2 used by KAP
      --help                Show this message and exit.

    Commands:
      auth           get user auth info
      cube_columns   list cube columns
      cube_desc      show cube description
      cube_names     list cube names
      cube_sql       get sample sql of cube. KAP only
      model_desc     show model description
      projects       list all projects
      query          sql query
      table_columns  list table columns
      table_names    list all table names
      users          list all users. Need admin role. KAP only

You can now query or fetch Apache Kylin information using kylinpy command, below are the command options.
If you haven't yet installed Apache Kylin in your environment, you may refer to this tutorial:
http://kylin.apache.org/docs21/install/index.html

kylinpy command options
^^^^^^^^^^^^^^^^^^^^^^^

============================= =========== ============================================
Command                       Option      Description
============================= =========== ============================================
auth                                      get user auth info
----------------------------- ----------- --------------------------------------------
cube_columns                  --name      list cube columns
----------------------------- ----------- --------------------------------------------
cube_desc                     --name      show cube description
----------------------------- ----------- --------------------------------------------
cube_names                                list cube names
----------------------------- ----------- --------------------------------------------
cube_sql                      --name      get sql of cube
----------------------------- ----------- --------------------------------------------
model_desc                    --name      show model description
----------------------------- ----------- --------------------------------------------
projects                                  list all projects
----------------------------- ----------- --------------------------------------------
query                         --sql       sql query
----------------------------- ----------- --------------------------------------------
table_columns                 --name      list table columns
----------------------------- ----------- --------------------------------------------
table_names                               list all table names
----------------------------- ----------- --------------------------------------------
users                                     list all users, need admin role, KAP only
============================= =========== ============================================

Examples
^^^^^^^^

1. To get all user info from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug auth

2. To get all cube columns from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug cube_columns --name kylin_sales_cube

3. To get cube description of selected cube from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug cube_desc --name kylin_sales_cube

4. To get all cube names from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -u ADMIN -p KYLIN --project learn_kylin --api1 --debug cube_names

5. To get cube SQL of selected cube from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug cube_sql --name kylin_sales_cube

6. To list all projects from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug projects

7. To list all tables column of selected cube from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug table_columns --name KYLIN_SALES

8. To get all table names from kylin::

    kylinpy -h kap.kapdemo.com -u ADMIN -p KYLIN --project learn_kylin --api1 table_names

9. To get the model description of the selected model from Apache Kylin with debug mode::

    kylinpy -h kap.kapdemo.com -P 7070 -u ADMIN -p KYLIN --project learn_kylin --api1 --debug model_desc --name kylin_sales_model


Apache Kylin dialect for SQLAlchemy
-----------------------------------
Any application that uses SQLAlchemy can now query Apache Kylin with this Apache Kylin dialect installed. It is part of the Apache Kylin Python Client Library, so if you already installed this library in the previous step, you are ready to use. 

You may use below template to build DSN to connect Apache Kylin::

    kylin://<username>:<password>@<hostname>:<port>/<project>?version=<v1|v2>&prefix=</kylin/api>

============================= ============================================
DSN Field                         Default Value
============================= ============================================
username
----------------------------- --------------------------------------------
password
----------------------------- --------------------------------------------
hostname
----------------------------- --------------------------------------------
port                               7070
----------------------------- --------------------------------------------
project                            default
----------------------------- --------------------------------------------
version                            v1
----------------------------- --------------------------------------------
prefix                             /kylin/api
============================= ============================================

Test connection with Apache Kylin::

    $ python
    >>> import sqlalchemy as sa
    >>> kylin_engine = sa.create_engine('kylin://username:password@hostname:7070/learn_kylin?version=v1')
    >>> results = kylin_engine.execute('SELECT count(*) FROM KYLIN_SALES')
    >>> [e for e in results]
    [(4953,)]
    >>> kylin_engine.table_names()
    [u'KYLIN_ACCOUNT',
     u'KYLIN_CAL_DT',
     u'KYLIN_CATEGORY_GROUPINGS',
     u'KYLIN_COUNTRY',
     u'KYLIN_SALES',
     u'KYLIN_STREAMING_TABLE']

Now you can configure the DSN in your application to establish the connection with Apache Kylin.

For example, you may install Apache Kylin Python Client Library in your Superset environment and configure connection to Apache Kylin in Superset

.. image:: https://raw.githubusercontent.com/Kyligence/kylinpy/master/docs/picture/superset1.png

then you may be able to query Apache Kylin one table at a time from Superset

.. image:: https://raw.githubusercontent.com/Kyligence/kylinpy/master/docs/picture/superset2.png

you may also be able to query detail data

.. image:: https://raw.githubusercontent.com/Kyligence/kylinpy/master/docs/picture/superset3.png

Alternatively, you may also be able to query multiple tables from Apache Kylin by using SQL Lab in Superset.

.. image:: https://raw.githubusercontent.com/Kyligence/kylinpy/master/docs/picture/superset4.png

