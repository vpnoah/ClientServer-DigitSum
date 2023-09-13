from socket import *

#Prints a server starting notice, then receives the IP address and port from the user
print("Digit Sum Client Started")
theIP = input("Please enter the server IP address (127.0.0.1 is the loopback IP) -->")
serverPort = int(input("Please input the server port --> "))

#receives the digit sum number from the user
inputString = input("Please enter the digit sum number --> ")

#connects to the socket on the server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((theIP,serverPort))

#result will be the number we get back from the server
result = inputString

#while the digit sum process is still going
while True:

    #turns the number to send into a string and sends it to the server
    toSend = str(result)
    print("Sending ", toSend, " to the server")
    clientSocket.send(toSend.encode())

    #gets a number back from the server
    result = int(clientSocket.recv(1024).decode())

    #runs the error process if we get back error code -99
    if result == -99:
        print("Server returned a Not a Number Error, exiting client application")
        clientSocket.close()
        break
    
    #prints the number we get back from the server
    print ("Received digit sum result = ", result)

    #stops the program if the result is a single digit number
    if result < 10:
        print("Server returned a single digit result, Exiting Client Application")
        clientSocket.close()
        break
    