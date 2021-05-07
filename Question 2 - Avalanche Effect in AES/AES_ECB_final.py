from Crypto.Cipher import AES       #Περιέχει την AES
from Crypto.Util.Padding import pad #Μας δίνει τη δυνατότhta Pad για να φτάσουμε το size του block
from Crypto.Random import get_random_bytes

avg = []
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)

import random

sysrandom = random.SystemRandom()   #Κρυπτογραφική τυχαιότητα

def bincount(n):                   #Function για την εξακρίβωση διαφοράς ενός bit
    return bin(n).count("1")

rep = int(input("How many pairs?")) #Δημιουργία ζευγών μηνυμάτων
        
for i in range(1, rep+1):
    
    print("For the messages in pair number",i)
    m1 = sysrandom.getrandbits(64)

    mt = sysrandom.randint(0, 64)

    m2 = m1 ^ (1 << mt)

    dif = bincount(m1 ^ m2)
    print("The difference in bits between the unencrypted messages is:", dif) #Έλεγχος διαφοράς bit
      
    m1 = str(m1).encode()
    m2 = str(m2).encode()
    
    mf1 = cipher.encrypt(pad(m1,AES.block_size))
    mf2 = cipher.encrypt(pad(m2,AES.block_size))

    dif = bincount((int.from_bytes(mf1, byteorder='big')) ^ (int.from_bytes(mf2, byteorder='big')))
    print("The difference in bits between the encrypted messages is:", dif)
    avg.append(dif)

print("The average difference in bits of the encrypted messages is: ", sum(avg)/len(avg))
input("Press Enter to exit...")

