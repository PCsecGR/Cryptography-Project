cipher = 'i!))aiszwykqnfcyc!?secnncvch' #Our Cipher
letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".","!","?","(",")","-"] #A list containing all the characters from our table
bitlist = [] #A list containing all the bit values from our table
cipherbinary = [] #A list containing all the characters of our cipher turned into bits
keystreamlist = [] #A temporary list of the characters of the Keystream One by One
decryptedbits = [] #A list of the characters of the decrypted message in bit form
messagelist = [] #The decrypted message in list form

cipherlist = list(cipher) #Our Cipher turned into a list of single characters

#This creates a list of all the bit values from 00000 to 11111

for i in range(0, 32):
    bitlist.append(bin(i)[2:]) 

#This transforms our list of characters from the cipher into a list of bits from our bitlist

for i in range(0,len(cipher)):
    index = letter.index(cipherlist[i])
    cipherbinary.append(bitlist[index])

#This part calculates our KEY from the known encryption ab : ENC(ab) = .s

#Here we transform the characters into bits from the table

ab = bitlist[0] + bitlist[1]

sdot = bitlist[26] + bitlist[18]

#Here we apply the xor between the characters to get the reverse key since the way lfsr
#works is that the first pass is the reverse of the key we use for the encryption

keyreverse = (bin(int(sdot,2) ^ int(ab,2)).zfill(10)[2:])
key = list(keyreverse)
key.reverse()

print("Our key is: ", str().join(key))

#This part calculates the whole keystream from the initial key we found in the last part
#Using the bitshifts we took from our feedback function.

for i in range(0, len(cipher*5)):  #Cipher times 5 because each cipher char is 5bits long
    a = len(key)-1
    xor = int(key[a]) ^ int(key[a-1])
    xor2 = xor ^ int(key[a-3])
    xor3 = xor2 ^ int(key[a-4])
    key.insert(0,xor3)
    keystreamlist.append(key.pop())

#This part touches up the keystream to turn it into 5bit parts in order to xor with the 5bit cipher characters
s = [str(int) for int in keystreamlist]
keystreamwhole = ''.join(s)
n=5
keystreamfinal = [keystreamwhole[i:i+n] for i in range(0, len(keystreamwhole), n)]

#This part decrypts the message into a list of characters in bit form

for i in range(0, len(cipherbinary)):
    cipher = cipherbinary[i]
    keystr = keystreamfinal[i]
    translate = (bin(int(cipher,2) ^ int(keystr,2))[2:])
    decryptedbits.append(translate)

#This part translates the decrypted message from bits to letters merges them and prints the result

for i in range(0,len(decryptedbits)):
    index = bitlist.index(decryptedbits[i])
    messagelist.append(letter[index])


print("Our decrypted message is: ",str().join(messagelist))