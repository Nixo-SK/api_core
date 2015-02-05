api-core
========

Introduction
------

api-core represents core module used primary in eszone_ projects providing authentication and additional functions for
these projects.

Installation
------

1. Submodule this application into your Django project

   `git submodule add *repository-link*`

2. Append 'api_core' to INSTALLED_APPS in your Django project settings

3. Route api_core submodule in urls.py in your Django project settings

```python
   url(r'^my-url/', include('api_core.urls')),
```