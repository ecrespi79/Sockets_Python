import socket
import sys


# 1.) creating initial socket
def create_socket():
    try:
        global host
        global port
        global local_socket

        host = "127.0.0.1"
        port = 9999
        local_socket = socket.socket() # creates the actual socket assigns to variable

    except socket.error as msg: # monitor for error and then print the message
        print("Socket Creation Error: " + str(msg))

# 2.) Binding the socket and listen for connections

def bind_socket():
    try:
        global host
        global port
        global local_socket

        print(Binding the Port: " + str(port))

        local_socket.bind(host, port) # Actually binds the port on the machine
        local_socket.listen(10) # Listens to a max of 10 connections before erroring below


    except socket.error as msg:
        print("Binding Error: " + str(msg) + "\n" + "Retrying... Recursion")
        bind_socket() # using recursion to retry binding -- need a method to break the endless loop
