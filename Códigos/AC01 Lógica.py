a = int(input(""))
b = int(input(""))
c = int(input(""))

if a <= b <= c:
    print(a, b, c)
else:
    if a <= c <= b:
        print(a, c, b)
    else:
        if b <= a <= c:
            print(b, a, c)
        else:
            if b <= c <= a:
                print(b, c, a)
            else:
                if c <= a <= b:
                    print(c, a, b)
                else:
                    print(c, b, a)