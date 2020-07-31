resp = str
velos = []
anos = []

while resp != 'n':
    resp = input()
    resp = resp.lower()
    if resp == 'n':
        break
    
    anos.append(input())
    velos.append(input())
    
print(max(int(ano) for ano in anos))
print(max(int(velo) for velo in velos))
print(sum(velos) / len(velos))