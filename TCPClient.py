from socket import *
import pancake as p
import randomcake as rc
#server name
serverName = ''
#get server Ip from user
serverName = raw_input("Enter ip:")
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#make a random pancake
sdp = rc.random_pancake()
#print cake before sending it over wire
print "Before Seding"
sdp.print_cake
modified_pancake_string = ''
#container to hold the modified pancake
modified_pancake = p.Pancake()
pancake_string = sdp.to_string()
print "client pancake string"
print pancake_string
#while 1:
clientSocket.send(pancake_string)
modified_pancake_string = clientSocket.recv(1024)
modified_pancake.from_string(modified_pancake_string)
modified_pancake.print_cake()
clientSocket.close()


