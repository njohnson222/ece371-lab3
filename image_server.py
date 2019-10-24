from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
import RSA
import des
from des import nsplit

SERVER_IP   = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 8192

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (SERVER_IP, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
des_key=''
public = ()
while True:
        (data,addr) = mySocket.recvfrom(SIZE)
        data = data.decode()
        if data.find('public_key')!=-1: #client has sent their public key\
            ###################################your code goes here#####################################
            #retrieve public key and private key from the received message (message is a string!)
            key = data.split()
            public_key_e = int(key[1])
            public_key_n = int(key[2])
            public = (public_key_e, public_key_n)
            print ('public key is : %d, %d'%(public_key_e,public_key_n))

        elif data.find('des_key')!=-1: #client has sent their DES key
            ###################################your code goes here####################

            # Decrypt DES KEY
            ciphertext = data.split(",")[1:]
            des_key = ""
            for num in ciphertext:
                des_key += RSA.decrypt(public, int(num))

            # Receive encrypted image bytes from the client
            (data,addr) = mySocket.recvfrom(SIZE)

            # Decrypt the picture data
            coder = des.des()
            rr_byte = bytearray()
            rr_byte = coder.run(des_key, data, action=des.DECRYPT)

            #decrypt the image
            ###################################your code goes here####################
            #the received encoded image is in data
            #perform des decryption using des.py
            #write to file to make sure it is okay
            file2 = open(r'penguin_decrypted.jpg',"wb")
            file2.write(bytes(rr_byte, "ISO-8859-1"))
            file2.close()
            print('decypting image completed')
            break
        else:
            continue
                #python2: print data ,
