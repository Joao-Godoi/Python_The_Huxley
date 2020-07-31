a = int(input(""))
b = int(input(""))
c = int(input(""))

if a<=b and b<=c:
    print("%i\n%i\n%i" %(a, b, c))

elif a<=c and c<=b:
    print("%i\n%i\n%i" %(a, c, b))

elif b<=a and a<=c:
    print("%i\n%i\n%i" %(b, a, c))

elif b<=c and c<=a:
    print("%i\n%i\n%i" %(b, c, a))

elif c<=a and a<=b:
    print("%i\n%i\n%i" %(c, a, b))

else:
    print("%i\n%i\n%i" %(c, b, a))
