#!/usr/bin/python3

# from https://docs.python.org/3/howto/sockets.html#non-blocking-sockets
# and
# https://docs.python.org/3/library/socket.html#example

# Test with 
# echo "hey" | nc crow 42424

import socket
import threading

# Create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a public host and a well-known port
hostname = socket.gethostname()
print("Listening on interface " + hostname)

# This accepts a tuple...
serversocket.bind((socket.gethostname(), 42424))
print (socket.gethostname())

# Become a server socket
serversocket.listen(5)
connectionNumber = 0

# Function to be run in a seperate thread.
# Takes an active socket and handles input/output messages
def handleConnection(conn, addr, connectionInstance):
    with conn:  # This is a socket! With syntax does not work on Python 2
        print('Connected by', addr)
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break  # No more data from client, break the inner loop
                
                print("Heard from "+str(connectionInstance))
                message = data.decode('UTF-8')
                print(message+"\n")
                
                # Just send a response
                conn.sendall(b'''Message received''')
                if message == "end":
                  break
            except Exception as e:
                print(e)
    print('Connected closed on ', addr)
    conn.close()

# Handles receiving and accepting new TCP clients. 
while True:  # Continuously listen for new clients
    conn, addr = serversocket.accept()
    client_thread = threading.Thread(target=handleConnection, args=(conn, addr, connectionNumber))
    client_thread.start()
    connectionNumber+=1
