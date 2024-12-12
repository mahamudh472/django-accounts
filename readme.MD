# Django Accounts App

A reusable Django app for managing user authentication and profiles.

## Features
- User registration
- Login/Logout
- Password reset via email
- User profile management
- Extendable and customizable

## Installation
1. Add the app as a submodule:
   ```bash
   git submodule add https://github.com/mahamudh472/django-accounts.git accounts
Include it in your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    ...
    'accounts',
]
```
Add the app's URLs to your project urls.py:
```python
    from django.urls import include, path

    urlpatterns = [
        ...
        path('accounts/', include('accounts.urls')),
    ]
```
Usage

    Templates for login, registration, and password reset are included by default.
    Override these templates by adding them to your project’s templates/accounts/ directory.

Dependencies

    Django>=3.2
    Python>=3.8

Configuration

Add these settings to customize:

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

License

For more details, refer to the documentation.



