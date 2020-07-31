n1 = float(input())
n2 = float(input())
n3 = float(input())

med = (n1+n2+n3)/3
cont = 0

if n1 > med:
    cont = cont + 1

if n2 > med:
    cont = cont + 1

if n3 > med:
    cont = cont + 1

print(cont)