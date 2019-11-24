#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [
        (dirpath.replace(package + os.sep, "", 1), filenames)
        for dirpath, dirnames, filenames in os.walk(package)
        if not os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename) for filename in filenames])
    return {package: filepaths}


setup(
    name="django-defender",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description="redis based Django app that locks out users after too "
    "many failed login attempts.",
    long_description="redis based Django app based on speed, that locks out"
    "users after too many failed login attempts.",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="django, cache, security, authentication, throttle, login",
    author="Ken Cochrane",
    url="https://github.com/kencochrane/django-defender",
    author_email="kencochrane@gmail.com",
    license="Apache 2",
    include_package_data=True,
    packages=find_packages(),
    package_data=get_package_data("defender"),
    install_requires=["Django>=1.8,<2.3", "redis>=2.10.3,<3.3"],
    tests_require=[
        "mock",
        "mockredispy>=2.9.0.11,<3.0",
        "coverage",
        "celery",
        "django-redis-cache",
    ],
)
