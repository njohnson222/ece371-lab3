

import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt

SERVER_IP    = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
p=1297447
q=1297973
###################################your code goes here#####################################
#generate public and private key from the p and q values
public, private = generate_keypair(p, q)

message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
while True:
        message=input()
        message.join('\n')
        ###################################your code goes here#####################################
        #message is a string input received from the user, encrypt it with RSA character by character and save in message_encoded
        #message encoded is a list of integer ciphertext values in string format e.g. ['23131','352135','54213513']
        message_encoded = []
        for x in range(len(message)):
                message_encoded.append(encrypt(private, message[x]))
        [mySocket.sendto(str(code).encode(),(SERVER_IP,PORT_NUMBER)) for code in message_encoded]
sys.exit()
