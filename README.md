<h1>rest_admin_project</h1>

<h2>Table of content</h2>

- [Description](#description)
- [Install](#install)
- [Usage](#usage)
- [To Do](#to-do)

## Description ##

**Program allow to perform API different requests**


- **/api/v1/users/** - represent end-point for:
    - creating user
    - list all users

- **/api/v1/users/<pk:int>/** - end-point for:
    - PATCH user information
    - DELETE user

- **/api/v1/token/** - log-in

- **/api/v1/token/refresh/** - getting refresh token

- **/api/v1/weather/** - log-in

- **/api/v1/check-memory/** - log-in

## Install ##
**To install the app run in terminal:**

```
docker-compose up
```

## Usage ##
**To work with API go to the documentation page:**

http://localhost:8000/swagger/

At the page all the end-points shown.

## To Do ##

- [] add doc-strings and annotations through out the project
- [] refactor structure of the project (e.g. app folder for all apps)
- [] add tests
