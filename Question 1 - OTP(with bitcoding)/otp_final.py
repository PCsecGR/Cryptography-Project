#Added [space] in the end of the letter list
letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",".","!","?","(",")","-"," "]
number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
bit = []       #The empty bit table
str1 =''       #Temporary string
encrypt =[]    #The encrypted text in bits after xOr
decrypt =[]    #The decrypted text in bits after x0r
tempotp =[]
otp = []       #The OTP in bits
ind =[]        #The text to be encrypted in bits
encrypttxt =[] #The encrypted text in a letter list
strencrypt ='' #The encrypted text
decrypttxt =[] #The decrypted text in a letter list
strdecrypt ='' #The decrypted text

#Create the bit table
for i in range(0, 32):
    bit.append(bin(i))
#print(bit)

#str1 = '{0:b}'.format(int(bit[23], 2) ^ int(bit[8], 2))
#print(str1)

#Get the text to be encrypted
text = input("Please type in the phrase to be encrypted WITHOUT spaces and using UPPER CASE letters: ")

t = list(text)

#print(t)

#Turn the text into bits according to the table
for i in range(0,len(text)):
    index = letter.index(t[i])
    ind.append(bin(index)) 

#print(ind)

#Create a random OTP
import random

for i in range(0, len(t)):
    n = random.randint(0,31)
    tempotp.append(n)
    index = number.index(tempotp[i])
    #print(index)
    otp.append(bit[index])
    

#print(otp)            

#xOr the text with the OTP
for i in range(0, len(text)):
    #str1 = '{0:b}'.format(int(ind[i], 2) ^ int(otp[i], 2))
    str1 = bin(int(ind[i], 2) ^ int(otp[i], 2))
    encrypt.append(str1)
    #print(i)
    #print(str1) 
    #print(encrypt)

#Print the encrypted phrase
for i in range(0,len(text)):
    index = bit.index(encrypt[i])
    encrypttxt.append(letter[index])

print("The encrypted phrase is:")
for ele in encrypttxt:  
        strencrypt += ele

print(strencrypt)

input("Press Enter to continue...")

#xOr the encrypted text with the OTP
for i in range(0, len(text)):
    #str1 = '{0:b}'.format(int(ind[i], 2) ^ int(otp[i], 2))
    str1 = bin(int(encrypt[i], 2) ^ int(otp[i], 2))
    decrypt.append(str1)

#Print the decrypted phrase
for i in range(0,len(text)):
    index = bit.index(decrypt[i])
    decrypttxt.append(letter[index])

print("The decrypted phrase is:")
for ele in decrypttxt:  
        strdecrypt += ele

print(strdecrypt)

input("Press Enter to exit...")
