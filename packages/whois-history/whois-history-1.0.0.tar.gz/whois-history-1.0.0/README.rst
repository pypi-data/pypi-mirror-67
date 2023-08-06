========
Overview
========

The client library for
`Whois History API <https://whois-history.whoisxmlapi.com/>`_
in Python language.

The minimum Python version is 3.6.

Installation
============
::

    pip install whoisapi-history

or

::

    git clone https://github.com/whoisxmlapi/whoishistory-py
    pip install -e /path_to_sdist/

or

::

    cd /whoishistory-py
    python setup.py install

or

::

    cd /whoishistory-py
    easy_install .

Examples
========

Full API documentation available `here <https://whois-history.whoisxmlapi.com/api/documentation/making-requests>`_

Create a new client
-------------------

::

    from whoishistory import ApiClient

    client = ApiClient('Your API key')

Make basic requests
-------------------

::

    # Check how many records available. It doesn't deduct credits.
    print(client.preview('whoisxmlapi.com'))

    # Get actual list of records.
    print(client.purchase('whoisxmlapi.com'))


Additional options
-------------------
You can specify search options for these methods.


::

    import datetime

    d = datetime.date(2017, 1, 1)

    print(client.preview('whoisxmlapi.com'),
          sinceDate=d,
          createdDateFrom=d,
          createdDateTo=d,
          updatedDateFrom=d,
          updatedDateTo=d,
          expiredDateFrom=d,
          expiredDateTo=d,
    )


Development
===========

To install dev requirements, you need to run the following commands:

::

    cd /path_to_sdist/
    pip install -e .[dev]

To run unit tests, you may use the following command:

::

    cd /path_to_sdist/
    python -m unittest discover . "*_test.py"

or this one

::

    cd /path_to_sdist/
    tox
