from des import *

print("TEST S_BOX")
test_block = [0, 0, 1, 1, 0, 0]
test_round = 2
test_des = des()
subbed = test_des.compute_s_box(test_block, test_round)
print(f"OUTPUT: {subbed}")

print("\nTEST ENCRYPT:")
key = "12345678"
text = "hello world hiii"
ciphertext = test_des.run(key, text)
print(f"CIPHER: {ciphertext}")
print(f"CIPHER LEN: {len(ciphertext)}")

plaintext = test_des.run(key, ciphertext, action=DECRYPT)
print(f"\nPLAIN: {plaintext}")
print(f"PLAIN LEN: {len(plaintext)}")


#read image, encode, send the encoded image binary file
file = open(r'penguin.jpg',"rb")
data = file.read()
print(len(data))
file.close()
des_key = key
coder = des()

# Split image up into chunks of 8 bytes
encrypted_image = ""
image_chunks = nsplit(data, 8)
i = 0
for chunk in image_chunks:
    # Encrypt the current chunk
    ciphertext = coder.run(des_key, chunk, action=ENCRYPT)
    encrypted_image += ciphertext
    i+=1
print(len(encrypted_image))
encrypted_image = encrypted_image.encode('utf-8')
cipher_chunks = nsplit(encrypted_image, 8) # Split encrypted image into image_chunks
coder = des()
plaintext_image = ""
plain_chunk = ""
for chunk in cipher_chunks:
    plain_chunk = coder.run(des_key, chunk, action=DECRYPT)
    plaintext_image += plain_chunk
print(len(plaintext_image))

file2=open(r'penguin_decrypted_test.jpg',"wb")
file2.write(plaintext_image.encode())
file2.close()
print ('decypting image completed')
