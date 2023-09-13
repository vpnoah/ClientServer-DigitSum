from socket import *

#starts the server on port 4556 and listens for connections
serverPort = 4556
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('DigitSum Server has Started')
print('Listening on Port 4556')

#this method returns the sum of each digit in a number
def doDigitSum(inputNum):
    sum = 0
    for x in range(len(inputNum)):
        sum+=int(inputNum[x])
    return sum

#accepts a connection from a client
connectionSocket, addr = serverSocket.accept()

#runs until we break the loop
while True:

    #receives inout from the client and prints it out
    theInput = connectionSocket.recv(1024).decode()
    print("Received ", theInput, " from the client")

    #tracks the number that we will be returning
    toReturn = 0

    #we will try to do a digitSum on the input 
    try:
        toReturn = str(doDigitSum(theInput))
        print("Sending Digit Sum Result: ", toReturn)
    except:
        #on an error, sets the return value to error code -99
        toReturn = str(-99)
        print("Sending error code -99")
    
    #send back either our result, or the error code
    connectionSocket.send(toReturn.encode())

    #if we sent back the error code, close the server application
    if int(toReturn) == -99:
        print("Client did not send a number, closing server application")
        connectionSocket.close()
        break
    
    #if we sent back a single digit number, close the server application
    if int(toReturn) < 10:
        print("Digit Sum is a single digit, closing server application")
        connectionSocket.close()
        break
    