#We use the following list to compare it with the result of the primality test
oddcomp = [9,15,21,25,27,33,35,39,45,49,51,55,57,63]

# This function calculates d and r for which n - 1 = d * 2^r
def dnr(n):
    r = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        r += 1
    return d, r

#This is the function that aplies a primality test to a number of base "b"
#Then , if it passes the test compares it to our list in order to check if it
#is actually composite
def Pseudoprime(n, b):
    d, s = dnr(n)
    t = pow(b, int(d), n)
    if t == 1:
        return True
    while s > 0:
        if t == n - 1:
            return True
        t, s = pow(t, 2, n), s - 1
    return False

#We create a small list of odd composite numbers to compare with our pseudoprime
oddcomp = [9,15,21,25,27,33,35,39,45,49,51,55,57,63]

for oddcomp in oddcomp:
    if(Pseudoprime(oddcomp, 32)):
        print('The smallest possible fermat pseudoprime with base 32 is: ',oddcomp)
        break