dias = int(input())
km = int(input())

if km > 100:
    km_extra = km - 100
    total = (dias * 90) + (km_extra * 12)
    print("%.2f" %total)
else:
    total = (dias * 90)
    print("%.2f" %total)