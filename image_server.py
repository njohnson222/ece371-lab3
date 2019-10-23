from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
import RSA
import des
import time

SERVER_IP    = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 8192

def send_ack(socket):
    socket.sendto("OKAY".encode(),(SERVER_IP,PORT_NUMBER)) #send key

#hostName = gethostbyname( '192.168.1.3' )
hostName = gethostbyname( 'localhost' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key=''
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
            send_ack(mySocket) # Indicate that we're ready for another chunk

        elif data.find('des_key')!=-1: #client has sent their DES key
            ###################################your code goes here####################
            #read the next 8 bytes for the DES key by running (data,addr) = mySocket.recvfrom(SIZE) 8 times and then decrypting with RSA
            des_key = data

            # Decrypt DES KEY
            cipher_key = data.split(",")[1:]
            des_key = ""
            for num in cipher_key:
                des_key += RSA.decrypt(public, int(num))
            print(f"DECRYPTED KEY: {des_key}")

            #now we will receive the image from the client
            (data,addr) = mySocket.recvfrom(SIZE)
            #decrypt the image
            ###################################your code goes here####################
            #the received encoded image is in data
            #perform des decryption using des.py
            #coder=des.des()
            data = des.decrypt(des_key, data)
            #the final output should be saved in a byte array called rr_byte
            rr_byte=bytearray()
            #write to file to make sure it is okay
            file2=open(r'penguin_decrypted.jpg',"wb")
            file2.write(bytes(rr_byte))
            file2.close()
            print ('decypting image completed')
            break
        else:
            continue
                #python2: print data ,
