x = float(input())
z = float(input())

dh = (((34 - x) ** 2) + ((220 - z) ** 2)) ** 0.5
dk = (((0 - x) ** 2) + ((0 - z) ** 2)) ** 0.5
ds = (((140 - x) ** 2) + ((456 - z) ** 2)) ** 0.5

print("Distancia para Hogsmeade: %.2f" % dh)
print("Distancia para Kakariko: %.2f" % dk)
print("Distancia para Solitude: %.2f" % ds)