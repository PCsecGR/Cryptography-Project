import Crypto.Util.number 
from Crypto.Random import get_random_bytes 
import Crypto
import libnum

#This function initializes the neccesary numbers to use RSA and CRT
#More specifically
#It randomly generates our two prime numbers p,q
#It manually initializes our e = 65537
#It calculates the modulus inverse for d
#It calculates the modulus inverse for dp ,dq, qinv used in CRT

def get_RSA_keys(bits):
    p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    e = 65537
    n = p*q
    fi = (p-1)*(q-1)
    d = libnum.invmod(e,fi)
    dp = libnum.invmod(e,p-1)
    dq = libnum.invmod(e,q-1)
    qinv = libnum.invmod(q,p)
    return [p, q, e, d, n, dp, dq, qinv]

#This function encrypts our secret message 
def RSA_encrypt(m, e, n):
    return pow(m, e, n)

#This function decrypts our secret message using CRT
def RSA_decrypt(c, dp, dq, qinv, p, q):
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    h = pow(qinv * (m1 -m2), 1, p)
    return m2 + h * q

#--MAIN--#

#Bits used when generating p and q
bits = int(input("How many bits would you like to use for encrypting?"))
[p, q, e, d, n, dp, dq, qinv] = get_RSA_keys(bits)

#Message to be encrypted
m = int(input("Which number would you like to encrypt?"))

#Encryption
c = RSA_encrypt(m, e, n)
print("Your encrypted message is: ", c)

#Decryption
m = RSA_decrypt(c, dp, dq, qinv, p, q)
print('Your decrypted message is: ', m)