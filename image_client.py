import des
import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair, encrypt, decrypt
from des import nsplit
import struct

SERVER_IP   = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 1024
des_key='secret_k'
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
mySocket = socket( AF_INET, SOCK_DGRAM )

#first generate the keypair
#get these two numbers from the excel file
p=1297447
q=1297973

###################################your code goes here#####################################
#generate public and private key from the p and q values
public, private = generate_keypair(p, q)
message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER)) #send key

###################################your code goes here#####################################
# Encrypt and send the DES key using RSA
message_encoded = []
for x in range(len(des_key)):
        message_encoded.append(str(encrypt(private, des_key[x])))
message = ",".join(message_encoded)
message = "des_key," + message
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))


#read image, encode, send the encoded image binary file
file = open(r'penguin.jpg',"rb")
data = file.read()
file.close()

###################################your code goes here#####################################
#the image is saved in the data parameter, you should encrypt it using des.py
#set cbc to False when performing encryption, you should use the des class
#coder=des.des(), use bytearray to send the encryped image through network
#r_byte is the final value you will send through socket

coder = des.des()
r_byte = coder.run(des_key, data, action=des.ENCRYPT)
mySocket.sendto(bytes(r_byte, 'ISO-8859-1'), (SERVER_IP, PORT_NUMBER))
print('encrypted image sent!')
