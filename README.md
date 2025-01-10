# fastapi-playground

- [fastapi-playground](#fastapi-playground)
  - [setup](#setup)
  - [dev](#dev)
    - [start the app](#start-the-app)
    - [start the worker](#start-the-worker)
    - [start the flower](#start-the-flower)
  - [debug](#debug)
  - [docs](#docs)
  - [test](#test)
    - [unit tests](#unit-tests)
    - [list all url](#list-all-url)
- [external systems](#external-systems)
  - [setup](#setup-1)
    - [namespace](#namespace)
    - [minio](#minio)
    - [redis](#redis)
  - [cleanup](#cleanup)

## setup

```sh
pdm install
```

## dev

### start the app

```sh
pdm run start
```

### start the worker

```sh
pdm run worker
```

### start the flower

```sh
pdm run flower
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

### redis

follow the [bitnami redis chart](https://github.com/bitnami/charts/tree/master/bitnami/redis) to install redis

```sh
helm repo add bitnami https://charts.bitnami.com/bitnami
```

```sh
helm upgrade --install my-redis bitnami/redis -n fastapi-playground -f redis/values.yaml
```

verify the installation

```sh
kubectl exec -it svc/my-redis-master -n fastapi-playground -- redis-cli -h my-redis-master -a password scan 0
```

```sh
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.
1) "0"
2) (empty array)
```

expose to localhost

```sh
kubectl port-forward --namespace fastapi-playground svc/my-redis-master 6379
```

## cleanup

tl;dr: `./scripts/down.sh`

```sh
helm uninstall my-minio -n fastapi-playground
helm uninstall my-redis -n fastapi-playground
kubectl delete namespace fastapi-playground
```
