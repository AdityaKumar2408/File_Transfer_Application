import socket

port = 9999  # The Port number which isn't reserved by some internal system
host = "localhost"  # either localhost or IP Address of the system depending on connection router  will be the host


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: This specifies the address family for IPv4. AF_INET
# socket.SOCK_STREAM: This specifies the socket type as TCP (Transmission Control Protocol)

s.bind((host, port))
# server.bind((host, port)) is used to bind the server socket to a specific address and port.

s.listen(1)
# server.listen() listens for incoming connections from client

print("Waiting for connection......")
connection_addr, addr = s.accept()
# server.accept() accepts incoming connections from client

print(addr, "connected")

filename = input(str("enter filename"))
# enter the filename which have to be transmitted
file = open(filename, 'rb')

file_data = file.read(1024)
connection_addr.send(file_data)
# connection_addr.send(file_data) to send the encoded data to client

print("Data has been transmitted successfully to client")