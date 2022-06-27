## ChatApp-Senami
Senami, short had for Sema Na Mimi in Swahili, is a chat application developed in Django and Javascript that helps users communicate with each other through user specific rooms. It is an extension of an application my friends and I created of the same name but implemented with WSGI (Web Server Gateway Interface). In this version of Senami, I have developed the application with ASGI (Asynchronous Server Gateway Interface), WebSockets and Django Channels.

# Aplication Features
1. User registration
2. User login
3. Access rights into a chat room
4. Send and receive messages
5. Logout

# Technologies
Python3.8 | HTML | CSS | Django | Javascript 

# Bugs
No reported bugs so far. However, if you notice any bugs, contact me through my email, kirimiwayne@gmail.com

# Developer Notes
1. In your Ubuntu terminal, create a directory 
2. Run the command `git clone https://github.com/waynemorphic/ChatApp-Senami.git`
3. Run `cd ChatApp-Senami` to move into the cloned directory
4. Open the source code in your preferred directory. `code .` to run in VSCODE while on the path of the cloned directory.
5. Ensure to install a virtual environment such as virtualenvwrapper to run the application in the virtual environment
6. The application runs on a Redis server, therefore, run `sudo docker run -p 6379:6379 -d redis:5`. This enables the websocket handshaking and connection through an ASGI server.
7. Settings file have been added in .gitignore file for security purposes

# Dependancies
1. pyscopg2
2. django-bootstrap-v5
3. channels-redis
4. channels
5. daphne
6. django-registration

# Senami Version 1 Developers
1. https://github.com/waynemorphic
2. https://github.com/Jeff-Owuor
3. https://github.com/Ngina-G
4. https://github.com/Moni-que

# Senami Version 1 Link
https://senamiapp.herokuapp.com/

# Senami Version 2
I am still figuring out how to deploy a django ASGI application. Therefore, the application has not been staged for production yet.


