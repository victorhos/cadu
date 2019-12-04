# CADastro Unico - Cadu
# Cadastro único

Challenge Juntos Somos+

## Requirements
* python==3.7

### Development

Install dependencies
```bash
make requirements-dev
```
Run migrates
```bash
make migrate
```
To run app:
```bash
make run
```

### Production
```bash
web: gunicorn -b 0.0.0.0:8000  --pythonpath django cadu.wsgi
```

### Tests

To run tests or coverage, use:
```bash
make tests
make coverage
```

Coverage report
```
Name                                            Stmts   Miss  Cover
-------------------------------------------------------------------
django/cadu/__init__.py                             0      0   100%
django/cadu/customers/__init__.py                   0      0   100%
django/cadu/customers/admin.py                      1      0   100%
django/cadu/customers/apps.py                       3      3     0%
django/cadu/customers/enums.py                      4      0   100%
django/cadu/customers/helpers.py                   17      0   100%
django/cadu/customers/models.py                    53      2    96%
django/cadu/customers/serializers.py               68      2    97%
django/cadu/customers/urls.py                       3      3     0%
django/cadu/customers/views.py                     18      0   100%
django/cadu/enums.py                                6      0   100%
django/cadu/extensions/__init__.py                  0      0   100%
django/cadu/extensions/publisher/__init__.py        0      0   100%
django/cadu/extensions/publisher/client.py         12      3    75%
django/cadu/extensions/publisher/helpers.py         4      0   100%
django/cadu/extensions/publisher/publisher.py      41      2    95%
django/cadu/urls.py                                 5      0   100%
-------------------------------------------------------------------
TOTAL                                             235     15    94%
```

### Load customers base

To load clients to database, run command:
```bash
make load-customers url="https://storage.googleapis.com/juntossomosmais-code-challenge/input-frontend-apps.json"
```