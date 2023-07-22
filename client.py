import socket

port = 9999  # The Port number which isn't reserved by some internal system
host = "localhost"  # either localhost or IP Address of the system depending on connection router  will be the host


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET: This specifies the address family for IPv4. AF_INET
# socket.SOCK_STREAM: This specifies the socket type as TCP (Transmission Control Protocol)

s.connect((host, port))
# server.bind((host, port)) is used to connect the server socket to a specific address and port.

print("client connected to ser")

filename = input(str("enter what name You want for the receiving file"))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
# close the connection
print("file received successfully")