alt = float(input("Digite a altura da parede: "))
larg = float(input("Digite a largura da parede: "))

area = alt * larg

tinta = area / 2

print("\nÁrea da parede: %.2f m²" %(area))
print("Você precisa de %.2f litros de tinta para pintar sua parede" %(tinta))