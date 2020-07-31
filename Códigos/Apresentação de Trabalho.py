ig = int(input("Trabalho aborda Interface Gráfica? (0 - Nao 1 - Sim)"))
ia = int(input("Trabalho aborda Inteligência Artificial? (0 - Nao 1 - Sim)"))
enc = int(input("Trabalho aborda Encapsulamento? (0 - Nao 1 - Sim)"))
iden = int(input("Trabalho aborda Indentação? (0 - Nao 1 - Sim)"))
struc = int(input("Trabalho aborda Structs? (0 - Nao 1 - Sim)"))

if (ig == 1 or ia == 1) and (enc == 1 and iden == 1) and (struc == 1):
    print("Seu trabalho sera avaliado.")
    
else:
    print("Seu trabalho nao sera avaliado, nota 0.")