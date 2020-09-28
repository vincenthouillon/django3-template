# DJANGO TEMPLATE

Django 3.x template with personalized authentication (login with email).

## NOTE

Added consideration of templates and static folders at the root of the project:

```python
TEMPLATES = [
    {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR / 'templates'],
    ...
    }
]
...
STATICFILES_DIRS = [BASE_DIR / 'static']
```
