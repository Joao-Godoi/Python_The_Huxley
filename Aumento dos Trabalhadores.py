sal = float(input())

if sal > 500:
    salf = sal + (sal * 0.1)
    print("%.2f" % salf)
    
elif sal > 300 and < 500:
    salf = sal + (sal * 0.07)
    print("%.2f" % salf)
    
else:
    salf = sal + (sal * 0.05)
    print("%.2f" % salf)