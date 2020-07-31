l = float(input())

perimetro = l * 6
area = (3 * (l*l) * (3 ** (1/2))) / 2

print("Lado do hexagono: %.1f metros," % l)
print("Area: %.15f metros quadrados," % area)
print("Perimetro: %.1f metros." % perimetro)