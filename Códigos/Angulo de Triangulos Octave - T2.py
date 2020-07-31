a1 = float(input("Digite o valor do primeiro ângulo:"))
a2 = float(input("Digite o valor do segundo ângulo:"))
a3 = float(input("Digite o valor do terceiro ângulo:"))

if (a1 == 90) or (a2 == 90) or (a3 == 90):
    print("Este e um triangulo retangulo.")
    
elif (a1 > 90) or (a2 > 90) or (a3 > 90):
    print("Este e um triangulo obtusangulo.")
    
elif (a1 < 90) or (a2 < 90) or (a3 < 90):
    print("Este e um triangulo acutangulo.")
    