from socket import *
serverName = ''
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)	
clientSocket.connect((serverName,serverPort))

while 1:
	sentence = raw_input('Input lowercase sentence:')
	clientSocket.send(sentence)	
	modifiedSentence = clientSocket.recv(1024)
	print 'From Server:', modifiedSentence
  
clientSocket.close()

