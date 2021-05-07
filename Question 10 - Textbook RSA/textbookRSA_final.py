import math
import libnum

mf = [] #This empty list will be populated by the decrypted characters

#This function returns the prime factorization of a number
#Since our number N is the result of the multiplication of two prime numbers
#our list will contain only two numbers that are the P and Q of our RSA
def get_prime_factor(N):
    factors = []
    while N % 2 == 0:
        factors.append(2)
        N = N/2
    for i in range(3, int(math.sqrt(N) + 1), 2):
        if N % i == 0: 
            factors.append(i)
            N = N/i
#This part is not needed in our case since our list is only two items long
#but is included for the function to be able to be used for any number N
    if N > 2:       
        factors.append(int(N))
    return(factors)

#This function initializes the neccesary numbers to use RSA
def get_RSA_keys(factors, e):
    p,q = factors[0], factors[1]
    fi = (p-1)*(q-1)
    n = p*q
    d = libnum.invmod(e,fi)
    return(d, n)

#This function calculates (a^b)%c for the numbers a, b and c
#It is used in the process of decryption
def fast(a, g, n):
    bg = list(bin(g)[2:])
    bg.reverse()
    d = 1
    x = a
    for i in range(0, len(bg)):
        if bg[i] == '1' :
            d = (d*x)%n
        x = (x**2)%n    
    return(d)

#This function decrypts our secret message
def RSA_decrypt(c, d, n):
    for i in range(0,len(c)):
        mt = fast(c[i], d, n)
        mf.append(chr(mt))
    return mf

#--MAIN--#

#The ciphertext
c=[3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,909,9958,792,909,4132,3143,9958,3203,5343,792,3143,4443]

#The user inputs N and e
N = int(input("Please input number N: "))
e = int(input("Please input number e: "))

[d, n] = get_RSA_keys(get_prime_factor(N),e)

mf = RSA_decrypt(c, d, n)

print("Our plaintext is: ")
separator =''
print(separator.join(mf))
            
