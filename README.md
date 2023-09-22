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

<details>

<summary>endpoint list</summary>

```sh
[
  {
    "path": "/openapi.json",
    "name": "openapi",
    "methods": [
      "GET",
      "HEAD"
    ]
  },
  {
    "path": "/docs",
    "name": "swagger_ui_html",
    "methods": [
      "GET",
      "HEAD"
    ]
  },
  {
    "path": "/docs/oauth2-redirect",
    "name": "swagger_ui_redirect",
    "methods": [
      "GET",
      "HEAD"
    ]
  },
  {
    "path": "/redoc",
    "name": "redoc_html",
    "methods": [
      "GET",
      "HEAD"
    ]
  },
  {
    "path": "/users/",
    "name": "read_users",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/users/me",
    "name": "read_user_me",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/users/{username}",
    "name": "read_user",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/items/",
    "name": "read_items",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/items/{item_id}",
    "name": "read_item",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/items/{item_id}",
    "name": "update_item",
    "methods": [
      "PUT"
    ]
  },
  {
    "path": "/send-notification/{email}",
    "name": "send_notification",
    "methods": [
      "POST"
    ]
  },
  {
    "path": "/queue",
    "name": "add_item",
    "methods": [
      "POST"
    ]
  },
  {
    "path": "/exceptions/duplicate_name",
    "name": "raise_duplicate_name_error",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/exceptions/invalid_name",
    "name": "raise_invalid_name_error",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/admin/",
    "name": "update_admin",
    "methods": [
      "POST"
    ]
  },
  {
    "path": "/",
    "name": "root",
    "methods": [
      "GET"
    ]
  },
  {
    "path": "/url-list",
    "name": "get_all_urls",
    "methods": [
      "GET"
    ]
  }
]
```

</details>

# external systems

## setup

tl;dr: `./scripts/up.sh`

### namespace

```sh
kubectl create namespace fastapi-playground --dry-run=client -o yaml | kubectl apply -f -
```

### minio

follow the [bitnami minio chart](https://github.com/bitnami/charts/tree/master/bitnami/minio) to install minio

```sh
helm upgrade --install my-minio oci://registry-1.docker.io/bitnamicharts/minio -n fastapi-playground -f minio/values.yaml
```

expose to localhost

```sh
kubectl port-forward --namespace fastapi-playground svc/my-minio 9000
```

## cleanup

tl;dr: `./scripts/down.sh`

```sh
helm uninstall my-minio -n fastapi-playground
kubectl delete namespace fastapi-playground
```
