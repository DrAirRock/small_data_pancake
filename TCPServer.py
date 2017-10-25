from socket import *
import pancake as p


#holder for the client Small data pancake 
client_sdp = p.Pancake()
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
connectionSocket, addr = serverSocket.accept()
#while 1:
pancake_string = connectionSocket.recv(1024)
print "RECIVED FROM CLINET"
print pancake_string
client_sdp.from_string(pancake_string)
client_sdp.set_val(0,0,0,5000)
client_sdp.set_val(0,0,1,5000)
modified_pancake = client_sdp.to_string()
connectionSocket.send(modified_pancake)
connectionSocket.close()

