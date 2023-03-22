<h1>rest_admin_project</h1>

<h2>Table of content</h2>

- [Description](#description)
- [Install](#install)
- [Usage](#usage)
- [To Do](#to-do)

## Description ##

**Program allow to perform different API requests**


- **/api/v1/users/** - represent end-point for:
    - creating user
    - list all users

- **/api/v1/users/<pk:int>/** - end-point for:
    - PATCH - partly change user information
    - DELETE user

- **/api/v1/token/** - log-in

- **/api/v1/token/refresh/** - get refresh token

- **/api/v1/weather/** - check weather by payload
    - {"city": "city_name", "date": "YYYY-MM-DD"}

- **/api/v1/check-memory/** - request memory information from daemon

## Install ##
**To install the app run in terminal:**

```
docker-compose up
```

## Usage ##
**Project usage as a client more visualy shown at documentation page:**

http://localhost:8000/swagger/

## To Do ##

- [] add doc-strings and annotations through out the project
- [] refactor structure of the project (e.g. app folder for all apps)
- [] add tests
