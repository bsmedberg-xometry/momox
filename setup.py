import sys
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

VERSION = '0.0dev0'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except Exception:
    pass


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation :: CPython",
    'Topic :: Database',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


requires = [
    'pymongo>=3.4,<4.0',
]
if sys.version_info[:2] == (2, 7):
    requires.append('ipaddress')

setup(
    name='pymodm',
    version=VERSION,
    author='Benjamin Smedberg, Xometry',
    author_email='bsmedberg@xometry.com',
    license='Apache License, Version 2.0',
    include_package_data=True,
    description='MoMoX is a fast, safe, developer-friendly ODM on top of PyMongo.',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(exclude=['tests', 'tests.*']),
    platforms=['any'],
    classifiers=CLASSIFIERS,
    test_suite='tests',
    install_requires=requires,
    extras_require={'images': 'Pillow'}
)
