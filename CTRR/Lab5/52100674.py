import math
print("Bai1")
print("1a")
print("If Q then P,and if P then Q")
print("1b")
print("Q and not P")
print("1c")
print("If Q then P")
print("..........................................................")
print("Bai2")
print("2a")
print("If you understand how to solve all the exercises in the book, then you will get a good grade in the midterm exam. And if you get a good grade in the midterm exam, then it means you understand how to solve all the exercises in the book.")
print("2b")
print("You understand how to solve all the exercises in the book if and only if you did not get a good grade in the midterm exam.")
print("2c")
print("You will get a good grade in the midterm exam if and only if you understand how to solve all the exercises in the book.")
print("..........................................................")
print("Bai3")
print("3a")
print("Negation")
print("Q and not P; or not Q and P.")
print("You understand how to solve all the exercises in the book and did not get a good grade in the midterm exam, or you did not understand how to solve all the exercises in the book and got a good grade in the midterm exam.")
print("Converse")
print("If P, then Q.")
print("If you get a good grade in the midterm exam, then you understand how to solve all the exercises in the book.")
print("Contrapositive")
print("If not Q, then not P.")
print("If you do not understand how to solve all the exercises in the book, then you will not get a good grade in the midterm exam.")
print("3b")
print("Negation")
print("P and not Q.")
print("You got a good grade in the midterm exam and understand how to solve all the exercises in the book.")
print("Converse")
print("If not P, then not Q.")
print("If you did not understand how to solve all the exercises in the book, then you did not get a good grade in the midterm exam.")
print("Contrapositive")
print("If Q, then P.")
print("If you understand how to solve all the exercises in the book, then you got a good grade in the midterm exam.")
print("3c")
print("Negation")
print("Q and not P.")
print("You understand how to solve all the exercises in the book, but you did not get a good grade in the midterm exam.")
print("Converse")
print("If P, then Q.")
print("If you got a good grade in the midterm exam, then you understand how to solve all the exercises in the book.")
print("Contrapositive")
print("If not P, then not Q.")
print("If you did not get a good grade in the midterm exam, then you do not understand how to solve all the exercises in the book.")
print("..........................................................")
print("Bai4")
print("4a")
S1 = "q->t"
S2 = "p->t"
S3 = "r->t"
C ="t"
print("%s\n%s\n.%s\n.%s"%(S1 , S2 ,S3 ,C ))
print("4b")
S1="r->~q"
S2="p^r->v"
S3= "r->s"
S4="~s->~v"
C="v"
print ("%s\n%s\n%s\n%s\n.%s"%(S1 , S2 , S3 , S4, C ))
print("..........................................................")
print("Bai6") 
A=[
[2 ,0 ,5 ,0 ,3 ,0],
[3 ,0 ,0 ,0 ,0 ,0],
[0 ,6 ,2 ,0 ,5 ,0],
[3 ,0 ,9 ,0 ,25 ,0],
[0 ,0 ,2 ,4 ,5 ,0],
[0 ,0 ,0 ,0 ,0 ,5]
]

def isOdd(a):
    return a % 2 == 1

def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def isSquare(a):
    return math.isqrt(a) ** 2 == a

def isGreater(a, b):
    return a > b

def isEqual(a, b):
    return a == b

def isAbove(a, b):
    return a[0] < b[0]

def isLeftOf(a, b):
    return a[1] < b[1]

print("6a")
# (a) ∃a ∈ A, ¬isOdd(a) ∧ isP rime(a)
for i in range(len(A)):
    for j in range(len(A[0])):
        if not isOdd(A[i][j]) and isPrime(A[i][j]):
            print("True and value is", A[i][j])
            break
    else:
        continue
    break
else:
    print("False")
    
print("6b")
# (b) ∀a ∈ A, isOdd(a) → isSquare(a)
for i in range(len(A)):
    for j in range(len(A[0])):
        if isOdd(A[i][j]) and not isSquare(A[i][j]):
            print("True")
            break
    else:
        continue
    break
else:
    print("False")
    
print("6c")
# (c) ∀a ∈ A, isOdd(a) → isGreater(a, 2)
for i in range(len(A)):
    for j in range(len(A[0])):
        if isOdd(A[i][j]) and not isGreater(A[i][j], 2):
            print("True")
            break
    else:
        continue
    break
else:
    print("False")
    
print("6d")
# (d) ∃a ∈ A, isP rime(a) → ¬(isGreater(a, 3) ∨ isEqual(a, 3))
for i in range(len(A)):
    for j in range(len(A[0])):
        if isPrime(A[i][j]) and (isGreater(A[i][j], 3) or isEqual(A[i][j], 3)):
            print("True")
            break
    else:
        continue
    break
else:
    print("False")
print("6e")
# (e) ∃a ∈ A, ∀b ∈ A, isLeftOf(a, b)
def cau6e():
    for i in range(len(A)):
        for j in range(len(A[0])):
            a = (i, j)
            is_left_of_all = all(isLeftOf(a, (x, y)) for x in range(len(A)) for y in range(len(A[0])))
            if is_left_of_all:
                return True
    return False
print(cau6e()) 


print("6f")
# ∃a ∈ A, ∀b ∈ A, isGreater(a, b) → ¬isAbove(a, b)
def cau6f():
    for i in range(len(A)):
        for j in range(len(A[0])):
            a = A[i][j]
            is_greater_all = all(isGreater(a, A[x][y]) for x in range(len(A)) for y in range(len(A[0])))
            if is_greater_all:
                not_above_all = all(not isAbove((i, j), (x, y)) for x in range(len(A)) for y in range(len(A[0])) if A[x][y] != a)
                if not_above_all:
                    return True
    return False
print(cau6f()) 


