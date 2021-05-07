import random

#For this exercise we have created a different version of Miller-Rabin
#This function accepts
def miller_rabin(n, k):


    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


test = int(input("How many tests: "))
prime = 0
notprime = 0

for test in range(test):
    x = random.randint(1, 10**5)
    z = abs(x**2 + x - 1354363)
    #print(miller_rabin(z, 5))
    if (miller_rabin(z, 5)) == True:
        prime += 1
    else:
        notprime +=1

#print(notprime, prime)
print("This polynomial produces primes with: ",(prime/(notprime+prime))*100,"% success.")