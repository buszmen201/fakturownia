# fakturownia

Dodać host w `settings.py`
```
ALLOWED_HOSTS = [
    'buszmen201.pythonanywhere.com'
    ]
```
Ustawić odpowiednio:
```
STATIC_ROOT = '/home/buszmen201/FV_Maker/static'
```

W przypadku chęci właczenia `debug-toolbar`:

```
INTERNAL_IPS = [
   '127.0.0.1',
   'url-jak-w-ALLOWED_HOSTS`,
]
DEBUG = True
``
