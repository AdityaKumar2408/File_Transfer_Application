# File_Transfer_Application

This repository contains a simple Python application that enables file transfer between a server and a client using sockets, based on the concepts of network programming and TCP/IP. The application allows you to send files from the server to the client over the network.

**Network Programming and TCP/IP**

Network programming is a branch of software development that focuses on creating applications that communicate over a network. In this project, we use Python's built-in socket module to implement network communication. Sockets provide a way for processes to communicate with each other across a network, enabling data transfer between machines.


**TCP/IP (Transmission Control Protocol/Internet Protocol)**

Transmission Control Protocol/Internet Protocol is the underlying communication protocol used for most internet communications. It is a reliable, connection-oriented protocol that ensures data is delivered accurately and in order. TCP/IP is a core part of internet communication and is widely used in various applications, including web browsing, email, and file transfer.


**Features**
* Simple and lightweight file transfer using sockets and TCP/IP.
* Easy setup and execution.


**Prerequisites**
Before running the file transfer application, make sure you have the following installed:

Python (recommended version 3.x)


**Sending a File from Server to Client**

1. After starting both the server and client scripts, the client will connect to the server automatically.

2. On the server-side, you will be prompted to enter the filename of the file you want to send. Enter the filename along with its extension (e.g., example.txt).

3. The file will be sent from the server to the client using the TCP/IP protocol, ensuring reliable and ordered delivery of data.

4. On the client-side, you will be prompted to enter a name for the received file. Choose a name for the received file, and it will be saved in the same directory as the client.py script.

5. Once the file transfer is complete, both the server and client will display a success message.


**Important Notes**

* The server and client should be on the same network for this example to work correctly. If the server is running on a different machine, modify the host variable in both server.py and client.py accordingly.

* This application demonstrates the fundamental concepts of network programming and TCP/IP, but it is intended for educational and demonstration purposes. For production use, consider adding error handling, security measures, and optimizing the code further.


# License
This code is provided under the MIT License. 
