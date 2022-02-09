#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='ponparse',
    version='0.1.0',
    description='Python Object Notation Parser',
    author='Michael White',
    author_email='ponparse@mypalmike.com',
    url='https://github.com/mypalmike/ponparse',
    packages=find_packages(include=['ponparse']),
    install_requires=[
        'ply==3.11',
    ],
    classifiers=[
        'Operating System :: POSIX',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Text Processing',
    ],
)
