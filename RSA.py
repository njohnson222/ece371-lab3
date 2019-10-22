#import math
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
#for more info look here: https://crypto.stackexchange.com/questions/5889/calculating-rsa-private-exponent-when-given-public-exponent-and-the-modulus-fact
#will also be explained in class
def get_d(e, phi):
    ###################################your code goes here#####################################
    d_old = 0;
    r_old = phi
    d_new = 1;
    r_new = e
    while r_new > 0:
        a = r_old // r_new
        (d_old, d_new) = (d_new, d_old - a * d_new)
        (r_old, r_new) = (r_new, r_old - a * r_new)
    return d_old % phi if r_old == 1 else None
    # d = 0.5
    # b = 0
    # # I used the useful link provided, which suggest that d is the reverse modulo of (1 mod z)/ e
    # # I implemented a short algorithm that computes reverse modulo
    # while (d % 1) != 0: # only has to loop b(private key) number times
    #     b = b + 1 # b increments
    #     d = (1-(phi*b))/e # quotient is calculated here
    # return d

def is_prime (num):
    if num > 1:

        # Iterate from 2 to n / 2
       for i in range(2, num//2):
           # If num is divisible by any number between
           # 2 and n / 2, it is not prime
           if (num % i) == 0:
               return False
               break
           else:
               return True

    else:
        return False


def generate_keypair(p, q):
    # if not (is_prime(p) and is_prime(q)):
    #     raise ValueError('Both numbers must be prime.')
    if p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    n = p*q
    phi = (p-1)*(q-1)
    arr = [ 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83] #array of prime numbers
    i = 0
    e = 0
    while (gcd(e,phi) is not 1) or not e < phi: # a while loop to find a good prime number
        e = arr[i]
        i+=1
    d = get_d(e, phi) # inverse modulo for gcd
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    cipher = pow(ord(plaintext), pk[0], pk[1])
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    plain = chr(pow(ciphertext, pk[0], pk[1]))
    return ''.join(plain)

# Test code for RSA
if __name__ == '__main__':
    pk = generate_keypair(31, 11)
    message = "Hello World"
    print(f"MESSAGE: {message}")

    ciphertext = []
    for character in message:
        x = encrypt(pk[0], character)
        ciphertext.append(x)
    print(f"CIPHERTEXT: {ciphertext}")

    plaintext = []
    for character in ciphertext:
        y = decrypt(pk[1], character)
        plaintext.append(y)
        
    plaintext = ''.join(plaintext)
    print(f"PLAINTEXT: {plaintext}")

    #message = ('public_key: %d %d' % (12, 2))
    #print(message[13])
