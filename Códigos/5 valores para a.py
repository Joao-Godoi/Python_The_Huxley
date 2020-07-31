ent = int()
cont = 0

for ent in range(5):
    ent = float(input("Digite um valor:\n"))

    if ent < 0:
        cont += 1
print("Foram digitados %i numeros negativos" % cont)