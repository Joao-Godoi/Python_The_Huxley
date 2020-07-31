n, d = input().split()
n, d = int(n), int(d)
digito_final_d = []

for x in range(1, n+1):
    ent = int(input())
    u = ent // 1 % 10
    
    if u == d:
        digito_final_d.append(ent)
        
while len(digito_final_d) < 5:
    digito_final_d.append(-1)
        
for x in sorted(digito_final_d):
    print(x)