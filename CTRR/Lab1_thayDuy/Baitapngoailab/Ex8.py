# n = eval(input("Nhap n:"))

# an = (2 * n) - 2
# for i in range(0, n):
#     for j in range(0, an):
#         print(end=" ")
#     an = an - 1
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")

n = eval(input("Nhap n:"))
i = 1
while i <= n:
    j = i
    while j < n:
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1