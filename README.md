# ChatApp-Senami

# Developer Notes
1. The application runs on a Redis server, therefore, run `sudo docker run -p 6379:6379 -d redis:5`. This enables the websocket handshaking and connection through an ASGI server.
2. Settings file have been added in .gitignore file for security purposes

