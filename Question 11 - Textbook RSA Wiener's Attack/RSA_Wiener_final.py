import libnum
import contfrac
import cmath

mf = [] #This empty list will be populated by the decrypted characters
pq= []
fn = []

#We identify that the provided ciphertext is in base64 encoding, after decoding
#it we get the ciphertext C bellow

C = [47406263192693509,51065178201172223,30260565235128704,82385963334404268,8169156663927929,47406263192693509,178275977336696442,134434295894803806,112111571835512307,119391151761050882,30260565235128704,82385963334404268,134434295894803806,47406263192693509,45815320972560202,174632229312041248,30260565235128704,47406263192693509,119391151761050882,57208077766585306,134434295894803806,47406263192693509,119391151761050882,47406263192693509,112111571835512307,52882851026072507,119391151761050882,57208077766585306,119391151761050882,112111571835512307,8169156663927929,134434295894803806,57208077766585306,47406263192693509,185582105275050932,174632229312041248,134434295894803806,82385963334404268,172565386393443624,106356501893546401,8169156663927929,47406263192693509,10361059720610816,134434295894803806,119391151761050882,172565386393443624,47406263192693509,8169156663927929,52882851026072507,119391151761050882,8169156663927929,47406263192693509,45815320972560202,174632229312041248,30260565235128704,47406263192693509,52882851026072507,119391151761050882,111523408212481879,134434295894803806,47406263192693509,112111571835512307,52882851026072507,119391151761050882,57208077766585306,119391151761050882,112111571835512307,8169156663927929,134434295894803806,57208077766585306]

#We will be using some of the functions from the previous excercise to initialize
#the necessary numbers as well as decrypt our ciphertext

#This function initializes the neccesary numbers to use RSA
def get_RSA_keys(qn, e):
    p,q = qn[0], qn[1]
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

#This function is the core of the Wiener's attack
def W_att(e, N):
    #First we get the convergents
    value = e/N
    convergents = list(contfrac.convergents(value, max_grade=30))
    #Then we calculate the possible φ(Ν) values
    for i in range(1,len(convergents)):
        conv = convergents[i]
        k = conv[0]
        d = conv[1]
        fnt = (e*d-1)//k
        fn.append(fnt)
    #Finally we solve the quadratic equation to find the values of Q and P
    for i in range(0,len(fn)):
        a = 1
        b = -(N - fn[i] + 1)
        c = N
        D = (b**2) - (4*a*c) 
        sol1 = (-b-cmath.sqrt(D))/(2*a)  
        sol2 = (-b+cmath.sqrt(D))/(2*a)
        if (sol1.real).is_integer() and (sol2.real).is_integer() and int((int(sol1.real))*int((sol2.real))) == N :
            pq.append((int(sol1.real),int(sol2.real)))
    return(pq)
            
#!---Main---!

e = int(input("What is e: "))
N = int(input("What is N: "))
#e, N = 50736902528669041, 194749497518847283

qn = W_att(e, N)
[d, n] = get_RSA_keys(qn[0], e)
mf = RSA_decrypt(C, d, N)

print("Our plaintext is: ")
separator =''
print(separator.join(mf))

