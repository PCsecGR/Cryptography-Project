from Crypto.Cipher import Blowfish
from struct import pack
from Crypto.Random import get_random_bytes

avg = []
key = get_random_bytes(16)
bs = Blowfish.block_size
cipher = Blowfish.new(key, Blowfish.MODE_CBC)

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
    print("The difference in bits between messages is:", dif) #Έλεγχος διαφοράς bit
      
    m1 = str(m1).encode()
    m2 = str(m2).encode()
    
    plen1 = bs - len(m1)%bs
    padding1 = [plen1]*plen1
    padding1 = pack('b'*plen1, *padding1)
    
    plen2 = bs - len(m2)%bs
    padding2 = [plen2]*plen2
    padding2 = pack('b'*plen2, *padding2)
    
    mf1 = cipher.iv + cipher.encrypt(m1 + padding1)
    mf2 = cipher.iv + cipher.encrypt(m2 + padding2)

    dif = bincount((int.from_bytes(mf1, byteorder='big')) ^ (int.from_bytes(mf2, byteorder='big')))
    print("The difference in bits between the encrypted messages is:", dif)
    avg.append(dif)

print("The average difference in bits of the encrypted messages is: ", sum(avg)/len(avg))
input("Press Enter to exit...")

