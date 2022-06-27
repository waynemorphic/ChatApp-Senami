# ChatApp-Senami

# Developer Notes
The application runs on a Redis server, therefofore, run `sudo docker run -p 6379:6379 -d redis:5`. This enables the websocket handshaking and connection through an ASGI server.
