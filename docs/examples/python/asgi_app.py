async def app(scope, receive, send):
    path_info = scope.get("path")
    match path_info:
        case "/hello" | "/hello/":
            data = b"Hello, World!\n"
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )

            await send(
                {
                    "type": "http.response.body",
                    "body": data,
                }
            )
        case "/goodbye" | "/goodbye/":
            data = b"Goodbye Cruel World!\n"
            await send(
                {
                    "type": "http.response.start",
                    "status": 500,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )

            await send(
                {
                    "type": "http.response.body",
                    "body": data,
                }
            )
        case _:
            data = b"I'm Lost!\n"
            await send(
                {
                    "type": "http.response.start",
                    "status": 404,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )

            await send(
                {
                    "type": "http.response.body",
                    "body": data,
                }
            )
