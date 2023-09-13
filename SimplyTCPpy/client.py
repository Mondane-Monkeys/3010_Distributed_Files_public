import socket

# Create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port to connect to
server_address = (socket.gethostname(), 42424)

# Connect to the server
clientsocket.connect(server_address)

while True:
    # Get user input for the message
    message = input("Enter a message (type 'end' to exit): ")
    
    # Send the message to the server
    clientsocket.sendall(message.encode('UTF-8'))
    
    if message == "end":
        break  # Exit the loop if the user enters "end"

    # Receive and print the server's response
    data = clientsocket.recv(1024)
    print("Received:", data.decode('UTF-8'))

# Close the client socket
clientsocket.close()
