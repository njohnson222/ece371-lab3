from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
import RSA
import des
import time
from des import nsplit

SERVER_IP    = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 6800

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

            # Decrypt DES KEY
            ciphertext = data.split(",")[1:]
            des_key = ""
            for num in ciphertext:
                des_key += RSA.decrypt(public, int(num))
            print(f"DECRYPTED KEY: {des_key}")

            time.sleep(3)

            # Receive encrypted image bytes from the client
            (data,addr) = mySocket.recvfrom(SIZE)
            print(len(data))

            cipher_chunks = nsplit(data, 8) # Split encrypted image into image_chunks
            coder = des.des()
            plaintext_image = ""
            plain_chunk = ""
            for chunk in cipher_chunks:
                plain_chunk = coder.run(des_key, plain_chunk, action=des.DECRYPT)
                plaintext_image += plain_chunk
            print(len(plaintext_image))


            #decrypt the image
            ###################################your code goes here####################
            #the received encoded image is in data
            #perform des decryption using des.py
            #   coder=des.des()
            #data = des.decrypt(des_key, data)
            #the final output should be saved in a byte array called rr_byte
            #rr_byte=bytearray()
            #write to file to make sure it is okay
            file2=open(r'penguin_decrypted.jpg',"wb")
            file2.write(plaintext_image.encode())
            file2.close()
            print ('decypting image completed')
            break
        else:
            continue
                #python2: print data ,
