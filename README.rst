newsbeuter-spread
=================

.. image:: https://badge.fury.io/py/newsbeuter-spread.png
    :target: https://badge.fury.io/py/newsbeuter-spread

.. image:: https://travis-ci.org/narfman0/newsbeuter-spread.png?branch=master
    :target: https://travis-ci.org/narfman0/newsbeuter-spread

Web frontend for newsbeuter db. Read and mark as read. Reading will roughly follow::

    sqlite3 -csv ~/.newsbeuter/cache.db "SELECT title, datetime(pubDate, 'unixepoch'), url FROM rss_item WHERE unread = 1 ORDER BY pubDate;"

Installation
------------

Install via pip::

    pip install newsbeuter-spread

Usage
-----

    newsbeuter-spread help

Start the server with::

    $ export FLASK_APP=newsbeuter_spread/app.py
    $ flask run
    * Running on http://127.0.0.1:5000/

Then navigate to the above url!

Development
-----------

Install all the testing requirements::

    pip install -r requirements_test.txt

Run tox to ensure everything works::

    make test

You may also invoke `tox` directly if you wish.

License
-------

Copyright (c) 2017 Jon Robison

See LICENSE for details
