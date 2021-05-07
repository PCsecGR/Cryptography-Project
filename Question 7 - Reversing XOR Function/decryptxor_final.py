from random import randint
from bitstring import BitArray

number = [] #The number to be encrypted
t = []

#The only way we found to create 16 bit numbers that were able to be used in 
#bitwise operations was to use BitArray

#Here we create our 16bit number and transform it into a BitArray

for i in range (15):
    t.append(randint(0,1))

b = BitArray(t)

#This function was given from the exercise and its the encryption algorithm
def encrypt(b):
    return b ^ (b << 6) ^ (b << 10) 

#This function was found by trial and error on papper  and takes as an input 
#our encrypted message and decrypts it back to the original
def decrypt(c):
    return c ^ (c << 6 ^ c << 12) ^ (c << 10)

c = encrypt(b)
d = decrypt(c)

print("Our original 16 bit number is: ", b)
print("When encrypted using our function: ", c)
print("When decrypted using our function: ", d)
if b == d:
    print("The decryption was succesfull!")