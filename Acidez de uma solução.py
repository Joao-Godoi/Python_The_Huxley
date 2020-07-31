ph = float(input("Digite o pH da solucao:\n"))

if 7 > ph > 0:
    print("Solucao acida")

elif ph > 7:
    print("Solucao basica")

elif ph == 7:
    print("Solucao neutra")

else:
    print("Valor do pH deve estar entre 0 e 14")
