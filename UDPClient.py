from socket import *
serverName = ''
serverPort = 12042
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:	
	message = raw_input('Input lowercase sentence:')
	clientSocket.sendto(message,(serverName, serverPort))
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	print modifiedMessage

clientSocket.close()
	

