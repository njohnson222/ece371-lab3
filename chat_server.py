from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( 'DE1_SoC' )
#hostName = gethostbyname( 'DESKTOP-A30LB1P' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key=''
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data=data.decode()
        if data.find('public_key')!=-1: #client has sent their public key\
            ###################################your code goes here#####################################
            #retrieve public key and private key from the received message (message is a string!)
            key = data.split()
            public_key_e = int(key[1])
            public_key_n = int(key[2])
            public = (public_key_e, public_key_n)
            print ('public key is : %d, %d'%(public_key_e,public_key_n))
        else:
            cipher=int(data)
            ###################################your code goes here#####################################
            #data_decoded is the decoded character based on the received cipher, calculate it using functions in RSA.py
            data_decoded = decrypt(public, cipher)
            print (data_decoded)
                #python2: print data
sys.ext()
#What could I be doing wrong?

