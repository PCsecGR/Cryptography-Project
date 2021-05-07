#import Crypto.Random.random
import random
import math

#Once again we are going to need the fast() function we have created a few questions ago
#This function calculates (a^b)%c for the numbers a, b and c
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

#This function generates a random n-bit number.
def number(n):
    a = random.getrandbits(n)
    #print(a.bit_length())
    return a

#This function is an implementation of fermat's primality test.
#It produces numbers of specific bitlength until it creates one that passes fermat's primality test
def fermat(n):
    while True:
        f = number(n)
        a = random.randint(2, f-1)
        if (math.gcd(a, f) == 1 and fast(a, f - 1, f) == 1):
            return f
#This function is an implementation of Miller-Rabin's primality test.
#It produces numbers of specific bitlength until it creates one that passes Miller-Rabin's primality test
def miller_rabin(n,t):   
    d = n - 1
    r = 0
    while d % 2 == 0:
        d = d // 2
        r += 1

    for rep in range(t):
        #print(rep)
        a = random.randrange(2, n - 1)
        b = fast(a, d, n)
        if b != 1:
            i = 0
            while b != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    b = (b ** 2) % n
    return True

#This function produces a 3000bit safe prime using the Miller-rabin primality test
#We have to take care that a safe prime is a (Sophie-Germain prime * 2 + 1) and not
#Just the number that satisfies the test
def safe_prime(n):
    while(True):
        a = number(n)
        if(miller_rabin(a, 2) and miller_rabin(2*a + 1, 2)):
            return (2*a + 1)

print("How many bits does the prime number you want to create with Fermat's primality test?")
n = int(input())
print()
print(fermat(n))

print()

print("How many bits does the number you want to create with Miller-Rabin's primality test have?")
m = int(input())
print()
n = number(m)
while miller_rabin(n,5) == False:
    n = number(m)
print(n)
 
print()

print("How many bits does the safe prime you want to create have?")
n = int(input())
print()
print(safe_prime(n))

