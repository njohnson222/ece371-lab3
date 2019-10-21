from des import *

print("TEST S_BOX")
test_block = [0, 0, 1, 1, 0, 0]
test_round = 2
test_des = des()
subbed = test_des.compute_s_box(test_block, test_round)
print(f"OUTPUT: {subbed}")

print("\nTEST ENCRYPT:")
key = "12345678"
text = "hellosir"
ciphertext = test_des.run(key, text)
print(f"CIPHER: {ciphertext}")
print(f"CIPHER LEN: {len(ciphertext)}")

plaintext = test_des.run(key, ciphertext, action=DECRYPT)
print(f"\nPLAIN: {plaintext}")
print(f"PLAIN LEN: {len(plaintext)}")
