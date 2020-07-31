r1 = float(input(""))
r2 = float(input(""))

a1 = 3.14 * (r1**2)
a2 = 3.14 * (r2**2)

if a1 > a2:
    print("Primeiro circulo")
    
elif a2 > a1:
    print("Segundo circulo")
    
elif a1 == a2:
    print("Iguais")