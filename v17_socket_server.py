import socket
import sys
import threading
import time
from queue import Queue


num_of_threads = 2
job_num = [1, 2]
queue = Queue()
all_connections = []
all_address = []

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

        print("Binding the Port: " + str(port))

        local_socket.bind((host, port)) # Actually binds the port on the machine, input tuple
        local_socket.listen(10) # Listens to a max of 10 connections before erroring below


    except socket.error as msg:
        print("Binding Error: " + str(msg) + "\n" + "Retrying... Recursion")
        #bind_socket() # using recursion to retry binding -- need a method to break the endless loop

# 3.) Accept connections that you listed for
def socket_accept():
    conn, address = local_socket.accept() # gives object and list
    print(conn)
    print("Connection has been established: |"+ "IP" + address[0] + " | Port " + str(address[1]))
    send_commands(conn) # Send data to the connection (should be get input from client change later)
    conn.close()

# Send commands to client (should be get input from client change later)
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            local_socket.close()
            sys.exit

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response =  str(conn.recv(1024), "utf-8")
            print(client_response)

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
