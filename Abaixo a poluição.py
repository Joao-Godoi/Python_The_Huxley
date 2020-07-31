entra = []
ent = int()
nm = 0
multa = 0

while ent != 999:
    ent = int(input())
    if ent == 999:
        break

    entra.append(ent)

for x in entra:
    if x > 2:
        nm = nm + 1
        qtd_car = x - 2
        multa += qtd_car * 12.89

print("%.2f" % multa)
print(nm)