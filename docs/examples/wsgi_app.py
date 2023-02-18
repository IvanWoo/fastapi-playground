def app(environ, start_response):
    path_info = environ.get("PATH_INFO")
    match path_info:
        case "/hello" | "/hello/":
            data = b"Hello, World!\n"
            start_response(
                "200 OK",
                [
                    ("Content-Type", "text/plain"),
                    ("Content-Length", str(len(data))),
                ],
            )
            return iter([data])
        case "/goodbye" | "/goodbye/":
            data = b"Goodbye Cruel World!\n"
            start_response(
                "500 Internal Server Error",
                [
                    ("Content-Type", "text/plain"),
                    ("Content-Length", str(len(data))),
                ],
            )
            return iter([data])
        case _:
            data = b"I'm Lost!\n"
            start_response(
                "404 Not Found",
                [
                    ("Content-Type", "text/plain"),
                    ("Content-Length", str(len(data))),
                ],
            )
            return iter([data])
