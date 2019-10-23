import des
import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair, encrypt, decrypt
from des import nsplit
import struct
import time




SERVER_IP    = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 1024
des_key='secret_k'
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
mySocket = socket( AF_INET, SOCK_DGRAM )

# Waits until an acknowledgement is received from the server that bytes were
# received, and thus ready for another transmission
def wait_for_ack(socket):
    # Enter infinite Loop
    while True:
        data, addr = socket.recvfrom(SIZE)
        data = data.decode()
        if data.find('OKAY')!=-1:
            break

#first generate the keypair
#get these two numbers from the excel file
p=1297273
q=1297651
###################################your code goes here#####################################
#generate public and private key from the p and q values
public, private = generate_keypair(p, q)
message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER)) #send key
time.sleep(1)

# Wait for acknowledgement from the server that public key is recieved
#print("Waiting for ACK...")
#wait_for_ack(mySocket)

###################################your code goes here#####################################

#encode the DES key with RSA and save in DES_encoded, the value below is just an example
message_encoded = []
for x in range(len(des_key)):
        message_encoded.append(str(encrypt(private, des_key[x])))
print(f"DES KEY ENCODED: {message_encoded}")
message = ",".join(message_encoded)
message = f"des_key,{message}"
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))


#read image, encode, send the encoded image binary file
file = open(r'penguin.jpg',"rb")
data = file.read()
print(len(data))
file.close()

###################################your code goes here#####################################
#the image is saved in the data parameter, you should encrypt it using des.py
#set cbc to False when performing encryption, you should use the des class
#coder=des.des(), use bytearray to send the encryped image through network
#r_byte is the final value you will send through socket
coder = des.des()

# Split image up into chunks of 8 bytes
encrypted_image = ""
ciphertext = coder.run(des_key, data, action=des.ENCRYPT)
print(ciphertext[0])
print(ciphertext[-1])
print(len(ciphertext))
print(ciphertext[0:10].encode())
time.sleep(1)
mySocket.sendto(encrypted_image[0:10].encode(), (SERVER_IP, PORT_NUMBER))
# while True:
#     mySocket.sendto("TEST MESSAGE".encode('utf-8'), (SERVER_IP, PORT_NUMBER))
#     time.sleep(1)

#r_byte=bytearray()

#send image through socket
#mySocket.sendto(bytes(r_byte),(SERVER_IP,PORT_NUMBER))
print('encrypted image sent!')
