# fastapi-playground

## setup

```sh
pdm install
```

## dev

```sh
pdm run start
```

## debug

start and debug from `app/__main__.py`

![start and debug from `app/__main__.py`](./assets/debug_entry.png)

## docs

start the app then visit `http://localhost:8000/docs` or `http://localhost:8000/redoc`

## test

### unit tests

```sh
pdm run test
```

### list all url

```sh
./tests/url-list.sh | jq
```

```sh
[
  {
    "path": "/openapi.json",
    "name": "openapi"
  },
  {
    "path": "/docs",
    "name": "swagger_ui_html"
  },
  {
    "path": "/docs/oauth2-redirect",
    "name": "swagger_ui_redirect"
  },
  {
    "path": "/redoc",
    "name": "redoc_html"
  },
  {
    "path": "/users/",
    "name": "read_users"
  },
  {
    "path": "/users/me",
    "name": "read_user_me"
  },
  {
    "path": "/users/{username}",
    "name": "read_user"
  },
  {
    "path": "/items/",
    "name": "read_items"
  },
  {
    "path": "/items/{item_id}",
    "name": "read_item"
  },
  {
    "path": "/items/{item_id}",
    "name": "update_item"
  },
  {
    "path": "/send-notification/{email}",
    "name": "send_notification"
  },
  {
    "path": "/queue",
    "name": "add_item"
  },
  {
    "path": "/exceptions/duplicate_name",
    "name": "raise_duplicate_name_error"
  },
  {
    "path": "/exceptions/invalid_name",
    "name": "raise_invalid_name_error"
  },
  {
    "path": "/admin/",
    "name": "update_admin"
  },
  {
    "path": "/",
    "name": "root"
  },
  {
    "path": "/url-list",
    "name": "get_all_urls"
  }
]
```
