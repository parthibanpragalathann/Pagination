# Learn to Work  Django , DRF and  POSTGRESQL with  multiple model Relationships, Hyperlinked model serializer and pagination.

## Created Database in Postgres
## Created and activate virtual environment

## Installed Packages or Dependencies 

````python 
  pip install django, djangorestframework, psycopg2
````

## Created API for STORE project and app

````python 
django-admin startproject api

django-admin startapp app
````

## Application definition(settings.py)

````python 
INSTALLED_APPS = [
    'app',
    'rest_framework',
]
````
## DB Connections (settings.py)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'STORE',
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## Created models

```doctest
Created app models here.

models -> employes, company and projects
Fields : ForeignKey - FK, ManyToManyField - MM
    
    employes - name
    company - name, emp_name(FK), created_at(date) 
    projects - name, companyname(MM), created_at(date)
```

## Created  Migrations and Run The server
````python 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
````

## Hyperlinkmodel serializer example

```python 
from rest_framework import serializers
from .models import *

class EmployesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employes
        fields = ("id", "url", "name")
```

## Created Views
```python 
# Create Company views here.
class Company_View(viewsets.ModelViewSet):
    queryset = company.objects.order_by("name")
    serializer_class = CompanySerializer
```

## Created Default and Custom DRF Pagination
### Default Pagination
```python 
File - settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': "rest_framework.pagination.PageNumberPagination",
    'PAGE_SIZE': 6
}
```
### Custom Pagination
```python 
class CustomPageNumberPageination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = "count"
    max_page_size = 6
    page_query_param = 'p'
```
## Applications urls

````python API URLS - 
    http://127.0.0.1:8000/api/
    http://127.0.0.1:8000/api/employee/
    http://127.0.0.1:8000/api/company/
    http://127.0.0.1:8000/api/company/?page=2
    http://127.0.0.1:8000/api/project/
    http://127.0.0.1:8000/api/project/?page=2
    http://127.0.0.1:8000/api/company/?page=2
    http://127.0.0.1:8000/api/employee/?count=5
    http://127.0.0.1:8000/api/employee/?limit=2&offset=12
````

```
Result: 

Pagination using  PAGENUMBER
http://127.0.0.1:8000/api/employee/?page=2
    "count": 15,
    "next": "http://127.0.0.1:8000/api/employee/?page=3",
    "previous": "http://127.0.0.1:8000/api/employee/",

Pagination using Limit&Offset
http://127.0.0.1:8000/api/employee/?limit=6&offset=6
    "count": 15,
    "next": "http://127.0.0.1:8000/api/employee/?limit=6&offset=12",
    "previous": "http://127.0.0.1:8000/api/employee/?limit=6",```

Pagination using Customized
http://127.0.0.1:8000/api/employee/?p=2
    "count": 15,
    "next": "http://127.0.0.1:8000/api/employee/?p=3",
    "previous": "http://127.0.0.1:8000/api/employee/",
    
Pagination using Cursor
http://127.0.0.1:8000/api/employee/?cursor=cD02
  "next": "http://127.0.0.1:8000/api/employee/?cursor=cD0xMg%3D%3D",
  "previous": "http://127.0.0.1:8000/api/employee/?cursor=cj0xJnA9Nw%3D%3D",
