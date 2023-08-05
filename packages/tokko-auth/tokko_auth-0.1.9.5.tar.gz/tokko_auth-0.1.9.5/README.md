Authorization
===


__ToC__

+ [Instalación](#install)
+ [Uso](#usage)
    - [**Namespace** requerido, API Level](#api-required-namespace)
    - [**Scopes** requeridos por View|Query|Mutations](#usage)
+ [Configuración](#settings)
    - [Variables de entorno](#environment-vars)
        * [Requeridas](#required)
        * [Opcionales](#optional)
+ [Testing](#testing)
+ [Strange Things](#glossary)
+ [How to contribute](#contributing)


# Install

## Install from PyPi 
```bash
pip install tokko-auth
```

## Install from sources
```bash
# Tokko Permission is required
pip install -e git@github.com:TokkoLabs/authorization.git
```

## Import & Configure dj-plugin
`your-project/settings.py`

```python
# Add app to installed apps
INSTALLED_APPS = [
    'tokko_auth'
]

# Also add declare app's middleware
MIDDLEWARE = [
    # Has request JWT?
    "tokko_auth.middleware.HasJWTMiddleware",
    # JWT has required NAMESPACE?
    "tokko_auth.middleware.NamespaceAuthorizationMiddleware",
    # Fill "request.user" attribute
    "tokko_auth.middleware.UserRecoverMiddleware",
]

# Finally, declare your AUTH0_DOMAIN
AUTH0_DOMAIN = 'my-auth-sub-dns.auth0.com'
```

# Usage

## API required NAMESPACE

`your-project/settings.py`

```python
# API required NAMESPACE
AUTH_API_NAMESPACE = 'my-service-namespace'
```

## View & Mutation required SCOPES

Resticciones de acceso basado en `scopes` para la view `some_ufo_secrets`.

```python
from tokko_auth.decorators import has_permission

# Require todos los scopes
@has_permission('x-files:agent', 'alien:believer', has_all=True)
def some_ufo_secrets(request):
    ...

# Al menos un scope
@has_permission('scully:agent', 'mulder:agent', at_least_one=True)
def some_ufo_secrets(request):
    ...
```

# Settings

## Environment Vars

Esta aplicación observa un conjunto de variables de entorno configurables, las cuales pueden modificar drásticamente su
funcionamiento.

## Required

| Name               | Description                                              | Type    | Default |
|:-------------------|:---------------------------------------------------------|:-------:|:-------:|
| AUTH0_DOMAIN       | Auth0 Domain. Ej: `{my-project}.auth.com`. Si esta variable no esta correctamente configurada, se emitirá un exception `EnvVarNotInitialized` | String | - |

## Optional

| Name                              | Description                                                       | Type    | Default |
|:----------------------------------|:------------------------------------------------------------------|:-------:|:-------:|
| AUTH_FAIL_SAFE_ENABLE             | Remueve errores de validación                                     | Boolean |  False  |
| AUTH_USERINFO_ENABLE              | Agrega **/userinfo** data al `request.user`                       | Boolean |  False  |
| AUTH_API_NAMESPACE                | Scopes requeridos a nivel API, estos se validaran en cada request |   List  |   [ ]   |
| AUTH_BEAUTIFY_ERROR_RESPONSE      | Formatea los errors a JSONResponse, se auto-deshabilita sobre GQL | Boolean |  False  |
| AUTH_FULL_DISABLED                | Desactiva validacion de Auth                                      | Boolean |  False  |
| AUTH_ALLOW_PRODUCTIVE_SHUTDOWN    | Permite desactivar la validacion de Auth en productivo            | Boolean |  False  |
| SAMPLES_ARE_ENABLE                | Agrega `Views, Mutation & Queries de ejemplo`                     | Boolean |  True   |

# Testing

## Local environment

### Unit Test
```bash
python manage.py test authorization.tests.unit
```

### Service Test
```bash
python manage.py test authorization.tests.service
```

## Docker environment

### Unit Test
```bash
# Require: docker-compose up [-d] [--build]
docker-compose exec app bash -c "python manage.py test authorization.tests.unit"
```

### Service Test
```bash
# Require: docker-compose up [-d] [--build]
docker-compose exec app bash -c "python manage.py test authorization.tests.service"
```

# Glossary

+ [OAuth](https://es.wikipedia.org/wiki/OAuth)
+ [Middleware](https://en.wikipedia.org/wiki/Middleware)


# Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to project.