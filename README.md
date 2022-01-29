# django-bootstrap-breadcrumbs

[![Version](https://img.shields.io/pypi/v/django-bootstrap-breadcrumbs.svg)](https://pypi.python.org/pypi/django-bootstrap-breadcrumbs)

## Documentation

https://django-bootstrap-breadcrumbs.readthedocs.org/en/latest/

## Note

This is a fork of the uncontinued repo [django-bootstrap-breadcrumbs](https://github.com/prymitive/bootstrap-breadcrumbs/blob/master/docs/index.rst) 
by prymitive. The repository tries to keep the functionality uptodate with current 
versions of python and django. Support for python2, python < 3.8 and django < 3.2 was dropped.
if you need to keep lower versions of python or django install the orginal version of prymitive.

##Testing

Plain testing:

```
py.test -v --pycodestyle --cov=django_bootstrap_breadcrumbs
```

Included Dockerfile allows to run tests using python3 from debian jessie.

Test with the most recent django version::

    docker build .

To specify django version to use for testing set the version via DJANGO arg to docker::

    docker build --build-arg DJANGO===3.2.11 .

DJANGO argument will be passed to pip using `pip install Django${DJANGO}`, so you can pass any version string pip accepts (==version, >=version).

To make testing easier there is a Makefile provided which wraps docker commands.

Run tests agains multiple versions of Django set in Makefile::

    make

To run tests against any version run::

    make $VERSION

Example::

    make 1.10.2
