# djangocms headless mode

This project is in test mode.

## Installation

- Install the plugin by `pip install django-cms-headless-test`
- rest_framework is a pre-requisite for this. Install it if not already installed using `pip install djangorestframework`

## Setup

Open the settings.py file and add the following:

```python

INSTALLED_APPS = (
    ...
    'django_cms_headless_test',
    'rest_framework',
    ...
)
```
Open the urls.py and add the following line in the url patterns

```python
urlpatterns = [
    ...
    url(r'api/', include('django_cms_headless_test.urls', namespace='headless_api')),
    ...
]
```

## Output

Run the server and go to `/api/pages`. You should be able to see the JSON with the details of all pages along with title, slug, meta-data etc. To see data for specific page, go to `/api/pages/path/<page-path>` (e.g. /api/pages/path/contact-us) to see data related to individual pages 