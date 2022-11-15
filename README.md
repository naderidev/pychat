# Simple chat room with Python [ Pychat ]
this is a simple chat room application based in python.

## Setting up
### Defineing users
In the first step, you must define your users, the users information is stored in the server/users.json file.
### Host and port
before you run the app, you must set the port and host.
 * in the server side --> server/Server.py:
    ````python
    class Server(Auth, Messenger):
        __host: str = '<Your Host>'
        __port: int = 0000  # Your port
    ...
    ````
 * in the client side --> client/Client.py:
    ````python
    class Client(Messenger):
        __host: str = '<Your Host>'
        __port: int = 0000  # Your port
    ...
    ````
## Running the application
1. copy the server folder into your server.
2. run Server.py
    ````shell
    python3 Server.py
    ````
3. run client/Client.py
    ````shell
    python3 Client.py
    ````
4. done.





