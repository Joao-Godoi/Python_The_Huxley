a = int(input())
b = int(input())
c = int(input())

ent = [a, b, c]
lista = sorted(ent, key=int, reverse=True)
print(lista[0])
print(lista[1])
print(lista[2])