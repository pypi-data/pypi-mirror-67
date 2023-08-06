# py-vetmanager-api

![Build Status](https://github.com/otis22/PyVetmanagerApi/workflows/Python%20package/badge.svg)

Python library for work with vetmanager api

![Vetmanager](https://vetmanager.ru) - CRM for veterinary business. 

All CRM account has unique domain name, url address may be:

* {$domainName}.vetmanager.ru
* {$domainName}.vetmanager.cloud
* git s...

# Examples

```
# For get full url by domain name
from vetmanager.functions import url

myurl = url('mydomain')
print(full_url)
```

```

# For get auth token
from vetmanager.functions import url
from vetmanager.client import Token, TokenCredentials
try:
    myurl = url('domain_name')
    credentials = TokenCredentials(
        login='login',
        password='password',
        app_name='myapp'
    )
    token = Token(credentials=credentials, url=url)
    print(token)
catch  Exception as err: 
    print(str(err))
```


# For contributor

## Check codestyle

```
flake8 vetmanager --count --show-source --statistics && flake8 tests --count --show-source --statistics
```

## Run tests

```pytest --cov=vetmanager --cov-fail-under 90 tests/```

## For publish package

```
python setup.py sdist
twine upload --skip-existing dist/* -r testpypi
twine upload --skip-existing dist/*
```