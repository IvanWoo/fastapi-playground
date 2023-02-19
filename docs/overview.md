# Python

## WSGI(Web Server Gateway Interface)

specs

- [PEP 333](https://peps.python.org/pep-0333)

parameters

- environ: A dictionary that contains information about the current request and the environment variables provided by the web server.
- start_response: A function that will be used to initiate sending an HTTP response back to the client.

example

```py
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Greetings universe']
```

[wsgi_app.py](./examples/python/wsgi_app.py)

```sh
pdm run gunicorn docs.examples.python.wsgi_app:app --reload
```

### libraries

let's verify the interface in the wild

#### [gunicorn](https://github.com/benoitc/gunicorn)

> 'Green Unicorn' is a WSGI HTTP Server

[traceback](https://github.com/benoitc/gunicorn/blob/792edf6d9aabcbfb84e76be1d722ac49c32dc027/gunicorn/workers/base_async.py#L108)

```py
        respiter = self.wsgi(environ, resp.start_response)
```

#### [flask]()

> a framework for building web applications

[trackback](https://github.com/benoitc/gunicorn/blob/792edf6d9aabcbfb84e76be1d722ac49c32dc027/gunicorn/workers/base_async.py#L108)

```py
        return self.wsgi_app(environ, start_response)
```

## ASGI(Asynchronous Server Gateway Interface)

parameters

- scope: A dictionary with information about the current request, akin to _environ_ in WSGI, but with a slightly different naming convention for the details.
- send: An async callable (function) that lets the application send messages back to the client.
- receive: An async callable that lets the application receive messages from the client.

example

```py
async def app(scope, receive, send):
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })
```

[asgi_app.py](./examples/python/asgi_app.py)

```sh
pdm run uvicorn docs.examples.python.asgi_app:app --reload
```

### libraries

let's verify the interface in the wild

#### [uvicorn](https://github.com/encode/uvicorn)

> an ASGI web server

[trackback](https://github.com/encode/uvicorn/blob/1e354230ffc983b0a374757a7bd3efc369b5a217/uvicorn/lifespan/on.py#L79-L86)

```py
    async def main(self) -> None:
        try:
            app = self.config.loaded_app
            scope: LifespanScope = {
                "type": "lifespan",
                "asgi": {"version": self.config.asgi_version, "spec_version": "2.0"},
            }
            await app(scope, self.receive, self.send)
```

#### [hypercorn](https://github.com/pgjones/hypercorn)

> an ASGI and WSGI Server

[trackback](https://github.com/pgjones/hypercorn/blob/8ae17ca68204d9718389fb3649ca0ed6ba851906/src/hypercorn/typing.py#L205-L212)

ASGI interface typing

```py
ASGIFramework = Callable[
    [
        Scope,
        ASGIReceiveCallable,
        ASGISendCallable,
    ],
    Awaitable[None],
]
```

#### [starlette](https://github.com/encode/starlette)

> an ASGI framework

[trackback](https://github.com/encode/starlette/blob/fc480890fe1f1e421746de303c6f8da1323e5626/starlette/applications.py#L114-L118)

```py
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        scope["app"] = self
        if self.middleware_stack is None:
            self.middleware_stack = self.build_middleware_stack()
        await self.middleware_stack(scope, receive, send)
```

#### [fastapi](https://github.com/tiangolo/fastapi)

> a framework based on [starlette](https://github.com/encode/starlette)

[trackback](https://github.com/tiangolo/fastapi/blob/f6f39d8714d8d5a7dd1ddc2a78f13ecfbe29d7d3/fastapi/applications.py#L268C15-L271)

```py
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if self.root_path:
            scope["root_path"] = self.root_path
        await super().__call__(scope, receive, send)
```

# Ruby

## [Rack](https://github.com/rack/rack)

> A modular Ruby web server interface

specs

- [rack/SPEC.rdoc](https://github.com/rack/rack/blob/main/SPEC.rdoc)

parameters

- environment: adopted from [PEP 333](https://peps.python.org/pep-0333)

return

- [status, headers, body]

examples

[app.rb](./examples/ruby/app.rb)

```sh
rbenv install
bundle install
RACK_ENV=develoyment bundle exec rackup docs/examples/ruby/config.ru
```

# references

- [ASGI explained: The future of Python web development](https://www.infoworld.com/article/3658336/asgi-explained-the-future-of-python-web-development.html)
- [Getting Started with Rack](https://gist.github.com/markbates/4240848)
- [Writing a small web service with Ruby, Rack, and functional programming](https://levelup.gitconnected.com/writing-a-small-web-service-with-ruby-rack-and-functional-programming-a16f802a19c0)
