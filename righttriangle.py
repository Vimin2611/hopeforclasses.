n = int(input("How many rows would you like for your pattern ?"))
for i in range(n):
    for j in range(i+1):
        print("*",end = "")
    print()
