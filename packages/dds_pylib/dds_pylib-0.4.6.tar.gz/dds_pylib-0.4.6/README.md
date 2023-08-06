# dds_pylib

## Diversified Data Python Helper Library

### Setup

[DDS KB](https://help.ddssoft.com/support/diversifieddata/ShowHomePage.do#Solutions/dv/193727000000679004)

### List of available utilities

1. ashell_orm
   1. ash_fields
      1. provides ashell specific Django field types
   2. models_orm
      1. provides model/field introspection needed by ashdevtools to generate ORM code
2. dates
    1. classes
        1. Gregorian()
    2. functions
        1. todays_julian()
        2. gregorian2julian()
        3. julian2gregorian()
3. decorators
    1. annotate
    2. deprecated
    3. memoize
    4. static_vars
    5. timeit
4. pyext
    1. collection
        2. functions
            1. multidim_list()
            2. flatten()
            3. create_multidim_list() - soon to be deprecated for multidim_list()
    2. multi_getattr
    3. nearly_equal
    4. objects
        1. ObjectDict
    5. struct
        1. Struct
5. util
    1. case
        1. camel_to_ashell_case()
        2. camel_to_snake_case()
    2. clear_screen.py
    3. print_pythonpath.py

### PyPi notes

[PyPi docs](http://python-packaging.readthedocs.io/en/latest/minimal.html)

1. to update version number edit root `__init__.py`

create source distribution

```console
python setup.py sdist
```

upload to PyPi

```console
python setup.py sdist upload
```

### Running Tests

Change current directory to library base directory

Run all tests. This will run all the test*.py modules inside the test package.

```console
> python -m unittest discover -v
test_decode (test.test_base.TestBase36) ... ok
test_encode (test.test_base.TestBase36) ... ok
test_gregorian (test.test_dates.TestGregorian) ... ok
test_j2g (test.test_dates.TestJulian2Gregorian) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.011s

OK
```

Limit tests to a specific test module

```console
> python -m unittest test.test_dates
..
----------------------------------------------------------------------
Ran 2 tests in 0.004s

OK
```

Add `-v` switch to makes output more verbose

```console
> python -m unittest -v test.test_dates
test_gregorian (test.test_dates.TestGregorian) ... ok
test_j2g (test.test_dates.TestJulian2Gregorian) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.007s

OK
```

Further limit test to a specific TestCase

```console
> python -m unittest -v test.test_dates.TestGregorian
test_gregorian (test.test_dates.TestGregorian) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.005s

OK
```

Optionally further limit test to a specific TestCase.method

```console
> python -m unittest -v test.test_dates.TestGregorian.test_gregorian
test_gregorian (test.test_dates.TestGregorian) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.004s

OK
```

#### This library should be full tested
