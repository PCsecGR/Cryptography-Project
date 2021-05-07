def get_base(base):
  while True:  
    try:
        base = int(input("What is the base: "))
    except ValueError:
        print("Please input an integer.")
    else:
        return base
        break

def get_exponent(exponent):
  while True:  
    try:
        exponent = int(input("What is the exponent: "))
    except ValueError:
        print("Please input an integer.")
    else:
        return exponent
        break

def get_modulo(modulo):
  while True:  
    try:
        modulo = int(input("What is the modulo: "))
    except ValueError:
        print("Please input an integer.")
    else:
        return modulo
        break
    
print("Please input the numbers in the order they are called for: ")

a = get_base("")
g = get_exponent("")
n = get_modulo("")

#Converting the exponent integer to binary, storing it into a list and then reversing it to match my target algorithm
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

print(fast(a,g,n))
        