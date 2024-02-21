#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2013 by Łukasz Mierzwa
    :contact: l.mierzwa@gmail.com
"""


from setuptools import setup, find_packages


setup(
    name='django-bootstrap-breadcrumbs2',
    version='1.0.0',
    url='https://github.com/nad2000/bootstrap-breadcrumbs',
    original_url='https://github.com/christianwgd/bootstrap-breadcrumbs',
    license='MIT',
    description='Django breadcrumbs for Bootstrap 2, 3, 4, or 5',
    long_description='Django template tags used to generate breadcrumbs html '
                     'using bootstrap css classes or custom template',
    author='Łukasz Mierzwa, Christian Wiegand',
    author_email='christianwgd@gmail.com',
    maintainer='Christian Wiegand',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'django'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    zip_safe=False,
    include_package_data=True,
    python_requires='>=3.7',
)
