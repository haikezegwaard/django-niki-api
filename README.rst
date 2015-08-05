=====
Niki API
=====

Niki API is a Python/Django implementation of the Niki.nl REST API
 
Quick start
-----------

1. Add "niki-api" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'niki',
    )

2. Include the polls URLconf in your project urls.py like this::

    url(r'^niki/', include('niki.urls')),
    
3. In your browser, call the Niki API for example by: 
    http://localhost:8000/niki/api?resource=/projects/mine

