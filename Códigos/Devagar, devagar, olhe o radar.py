vm = float(input())
vc = float(input())

if vc <= vm:
    print("0.00")
    print("0")
    
elif vc <= ((0.2 * vm) + vm):
    print("85.13")
    print("4")
    
elif vc > ((0.2 * vm) + vm) and vc < ((0.5 * vm) + vm):
    print("127.69")
    print("5")
    
elif vc > ((0.5 * vm) + vm):
    print("574.62")
    print("7")
    