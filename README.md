# Calculator-with-GUI-using-sockets
A scientific calculator with client and server with GUI implemented using sockets.
A TCP connection is established between the client and server. We have one client and one server. 
The server is started first and is ready to take equations to be calculate from client. 
The client is implemented using tkinter which is a python module for Graphical User Interphase (GUI). 
The user types the equation at the client side which is sent to the server through socket. 
The calculations are done in the server and result is sent back to client. The result is displayed at the client side.
On the client side python client.py 'host' 'port no'.
On the server side python server.py 'port no'.
