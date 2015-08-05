import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-niki-api',
    version='0.1',
    packages=['niki-api'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A Django implementation of the Niki API.',
    long_description=README,
    url='http://www.niki.nl/',
    author='Haike Zegwaard',
    author_email='h.zegwaard@gmail.com',
    install_requires=[
          'requests',
      ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.7',        
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Rest API',
    ],
)