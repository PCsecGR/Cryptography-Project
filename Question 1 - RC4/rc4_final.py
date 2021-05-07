s = list(range(1,256))
k = []      
t2n = []    
c = []     
bf = []     
bd = []    
lf = []     
ld = []     
tf = []    
str1 =''
str2 =''

text = input("Please type in the phrase to be encrypted preferably WITHOUT spaces: ")
for letter in text:
    number = ord(letter)
    t2n.append(number)

key = input("Please type in the encryption key: ")
for letter in key:
    number = ord(letter)
    k.append(number)

for i in range(0, (len(s)-len(k))):
    k.append(k[i])


#Permuation
j = 0
kl = len(k)
sl = len(s)
for i in range(0, 255):
    j = (j + s[i] + k[i % kl])%sl
    s[i], s[j] = s[j], s[i]

#Keystream

i = 0
j = 0
for i in range(i+1, len(t2n)+1):
    j = (j + s[i]) % len(s)
    s[i], s[j] = s[j], s[i]
    t = (s[i] + s[j]) % len(s)
    c.append(s[t])
    
#Encruption

for i in range(0, len(c)):
    bf.append(t2n[i] ^ c[i])
    
for i in range(0, len(bf)):
    lf.append(chr(bf[i]))

print("The encrypted phrase is:")
for ele in lf:  
        str1 += ele

print(str1)

#Decryption
input("Press Enter to continue...")

for i in range(0, len(c)):
    bd.append(bf[i] ^ c[i])
    

for i in range(0, len(bf)):
    ld.append(chr(bd[i]))

print("The decrypted phrase is:")
for ele in ld:  
        str2 += ele

print(str2)

input("Press Enter to exit...")