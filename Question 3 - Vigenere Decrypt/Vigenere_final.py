letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
finalkey = str()
b = str()
c = str()

with open('vigenere.txt', encoding='utf-8-sig') as file:
    text = file.read()
compare = []

n = 2
bigram = [text[i:i+n] for i in range(0, len(text), n)]
n = 3
trigram = [text[i:i+n] for i in range(0, len(text), n)]

bioc = dict((i, bigram.count(i)) for i in bigram)
bioc2 = {k: v for k, v in sorted(bioc.items(), key=lambda item: item[1], reverse = True)}

trioc = dict((i, trigram.count(i)) for i in trigram)
trioc2 = {k: v for k, v in sorted(trioc.items(), key=lambda item: item[1], reverse = True)}


bicomp = list(bioc2.keys())
tricomp = list(trioc2.keys())

#Calculating the occurence of bigrams and trirams

for i in range(5):
    a = bicomp[i]
    bigind = [i for i, x in enumerate(bigram) if x == a]
    dif = [i - j for i, j in zip(bigind[1:], bigind)]
    compare = compare + dif
    
for i in range(5):
    a = tricomp[i]
    trigind = [i for i, x in enumerate(trigram) if x == a]
    dif = [i - j for i, j in zip(trigind[1:], trigind)]
    compare = compare + dif

    
input("Press enter to estimate key probability")

key = 0
leng = 0

for y in range(3, 12):
    print("For y=",y)
    result = list(filter(lambda x: (x % y == 0), compare))        
    print("The occurence is: ",len(result))
    if leng < len(result):
        leng = len(result)
        key = y



print("The key is probably: ",key)

#Finding the key using cryptanalysis based on the presence of the letter E
n = 1
lettertext = [text[i:i+n] for i in range(0, len(text), n)]
firstkey = lettertext[::key]

for i in range(0, key):
    
    tempkey = lettertext[::key]
    probablye = dict((i, tempkey.count(i)) for i in tempkey)
    probablye2 = {k: v for k, v in sorted(probablye.items(), key=lambda item: item[1], reverse = True)}
    lettere = list(probablye2.keys()).pop(0)
    print("We can assume that the letter that has subbed for E is: ",lettere)
    dif = abs(letter.index(lettere) - 4)
    print("The next letter is probably: ", letter[dif])
    finalkey = finalkey + letter[dif]
    lettertext.pop(0)

print("The key is probably: ",finalkey)
input("Press enter to attempt to decrypt the original text")


#Making the key big enough to decrypt the text

text = text.rstrip()

if len(finalkey) <= len(text):
    decryptkey = finalkey * (len(text) // len(finalkey)) + finalkey[:len(text) % len(finalkey)]

for i in range(0, len(text)):
    a = letter.index(text[i]) - letter.index(decryptkey[i])
    if a < 0:
        a = 26 + a
    b = letter[a]
    c += b

print("The decrypted text is: ")
print(c)

