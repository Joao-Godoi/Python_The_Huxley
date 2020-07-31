n = int(input())
list1 = []
list2 = []

ent = input().split(" ")
list1.extend(ent)
ent2 = input().split(" ")
list2.extend(ent2)
    
if ('0' in list1) == True:
    print("1")
else:
    print("0")
    
print(list1)
print(list2)