api\_core
========

Introduction
------

api\_core represents a core module used primary in eszone_ API projects providing an authentication, set of exceptions and
a bunch of API views to manage tokens. Token is passed in a request data as a 'authentication.token' key followed by a
value containing uuid4 string representation of a token.

Installation
------

1. Submodule this application into your Django project

   `git submodule add *repository-link*`

2. Append 'api\_core' to INSTALLED_APPS in your Django project settings

3. Route api\_core submodule in a urls.py file in your Django project settings

```python
   url(r'^my-url-auth/', include('api_core.urls')),
```