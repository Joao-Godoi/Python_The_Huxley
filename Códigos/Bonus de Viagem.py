sal = float(input())

bonus = sal * 0.75

if bonus < 2000:
    print("ARGENTINA")

elif 2000 < bonus < 3000:
    print("ESPANHA")

elif bonus > 3000:
    print("ALEMANHA")