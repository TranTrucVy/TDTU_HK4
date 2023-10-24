n = eval(input("Nhap n:"))
k = 0
for i in range(1, n+1):
    for j in range(1, (n-i)+1):
        print(end="  ")
        # print(i)
    while k != (2*i-1):
        print("* ", end="")
        k = k + 1
    k = 0
    print()
    