print('Exercise 4')
def algorithm(n):
    if n < 2:
        return []
    O = [2]
    i = 3
    while True:
        flag = True
        for j in range(len(O)):
            if i % O[j] == 0:
                flag = False
                break
        if flag:
            O.append(i)
        i += 2
        if i + 2 > n:
            break
    return O
algorithm(10)

print('Exercise 5')
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
gcd(50, 60)

print('Exercise 6')
def lcm(a, b):
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)
    return (a * b) // gcd(a, b)
lcm(50,60)

print('Exercise 7')
def Dec_2_Bin(n):
    k = []
    while (n>0):
        a = int(float(n%2)) 
        k.append(a) 
        n = (n-a)/2
    kq = ""
    k.reverse() 
    for i in k:
        kq += str(i)
    return kq
Dec_2_Bin(6)

print('Exercise 8')
def decimal_to_binary(num):
    k = []

    while (n>0):
        a = int(float(n%2)) # Tinh phan du
        k.append(a) # Day phan du vao danh sach
        n = (n-a)/2 # Tinh phan thuong cho phep tinh tiep theo

    kq = ""

    k.reverse()
    for i in k:
        kq += str(i)

    binary = []
    kq1 =""
    while n > 0 and len(binary) < 32:
        n *= 2
        if n >= 1:
            binary.append(1)
            n -= 1
        else:
            binary.append(0)
        return ''.join(str(x) for x in binary)
    
    return (kq+"."+''.join(str(x) for x in binary))

decimal_to_binary(5.5)





