sal = float(input())

if sal < 1000:
    salf = sal + (sal * 0.3)
    print("%.2f" % salf)
    
elif 1000 < sal < 2000:
    salf = sal + (sal * 0.1)
    print("%.2f" % salf)
    
elif sal > 2000:
    print("%.2f" % sal)