n = int(input())
cont = 0
idade = []
nome = []
sexo = []
estado = []
amg = []
fotos = []

while cont != n:
    idade.append(input())
    nome.append(input())
    #fotos = int(input())
    cont += 1
    
print(int(idade), nome)