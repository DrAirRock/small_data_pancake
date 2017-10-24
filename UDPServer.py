from socket import *
serverPort = 12042
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((’’, serverPort))
print "The server is ready to receive"
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	print 'Received from client:' + message 
	print clientAddress
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)

