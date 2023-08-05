pytest-stub
===========
https://github.com/idlesign/pytest-stub

|release| |lic| |ci| |coverage|

.. |release| image:: https://img.shields.io/pypi/v/pytest-stub.svg
    :target: https://pypi.python.org/pypi/pytest-stub

.. |lic| image:: https://img.shields.io/pypi/l/pytest-stub.svg
    :target: https://pypi.python.org/pypi/pytest-stub

.. |ci| image:: https://img.shields.io/travis/idlesign/pytest-stub/master.svg
    :target: https://travis-ci.org/idlesign/pytest-stub

.. |coverage| image:: https://img.shields.io/coveralls/idlesign/pytest-stub/master.svg
    :target: https://coveralls.io/r/idlesign/pytest-stub


Description
-----------

*Stub packages, modules and attributes.*

This pytest plugin allows you to replace dependencies with stubs.

It can be useful if you want to test some code using a dependency without actually having this dependency,
for example if you're testing your library, which uses some parts of another library.


Requirements
------------

* Python 3.6+
* pytest >= 2.9.0


How to use
----------

You can stub dependencies either with your own custom objects or you may instruct ``pytest-stub``
to generate functions or classes for you. Use ``stub`` fixture in your test functions, like this:

.. code-block:: python

    def test_django_related(stub):

        stub.apply({
            # Replace `call_command` with a generated function.
            'django.core.management.call_command': '[func]',

            # Replace `BaseCommand` with a generated class.
            'django.core.management.base.BaseCommand': '[cls]',

            # Replace `dummy` with generated MagicMock.
            'django.dummy': '[mock]',

            # Replace entire `cv2` module.
            'cv2': '[mock]',

            # Sometimes we need just a persistent (always the same) magic mock.
            'numpy': '[mock_persist]',

            # Stub multiple attributes in the same module with custom objects.
            'django.conf': {
                'settings': object(),
                'some': True,
            },

        })

If we want to replace some dependency with a stub not in a fixture but globally, we can use ``stub_global()`` function
in root ``conftest.py`` (this code will apply patch before tests, so tests will be safe to import code using dependencies).

.. code-block:: python

    from pytest_stub.toolbox import stub_global

    stub_global({
        'cv2': '[mock_persist]',
    })

