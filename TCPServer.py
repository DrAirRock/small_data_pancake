from socket import *
import pancake as p

sdp.pancake()
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
connectionSocket, addr = serverSocket.accept()
while 1:
	 = connectionSocket.recv(1024)
	print 'Message from client: ' + sentence
	print addr
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)

connectionSocket.close()

