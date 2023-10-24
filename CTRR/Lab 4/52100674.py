import math
import sympy
from sympy import *
print("Bai2")
#a.∃x ∈ Z, 0 ≤ x ≤ 100, x2 = 152 + 162
print("2a")
for x in range(101):
    if x**2 == 15**2 + 16**2:
        print(f"The given statement is correct when x equals {x}.")
        break
else:
    print("The given statement is incorrect for all values x within the given domain.")
# (b) ∃x ∈ Z, 0 ≤ x ≤ 100, x2 = 122 + 162
print("2b")
for x in range(101):
    if x**2 == 12**2 + 16**2:
        print(f"The given statement is correct when x equals {x}.")
        break
else:
    print("The given statement is incorrect for all values x within the given domain.")
# (c)∃x ∈ Z, −50 ≤ x ≤ 50, x2 ≥ 99x
print("2c")
for x in range(-50, 51):
    if x**2 >= 99*x:
        print(f"The given statement is correct when x equals {x}.")
        break
else:
    print("The given statement is incorrect for all values x within the given domain.")
# ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 6= 0
print("2d")
for x in range(50, 101):
    if x*(x+1)*(x+2) % 6 != 0:
        print(f"The given statement is correct when x equals {x}.")
        break
else:
    print("The given statement is incorrect for all values x within the given domain.")
# (e) 
print("2e")
# for x in range(0,101):
#     if math.sqrt(x) == math.sqrt(x) + math.sqrt(y):
#         print(f"The given statement is correct when x equals {x}.")
#     break
# else:
#     print("The given statement is incorrect for all values x within the given domain.")
print("BAI3")
print("3a")
# for x in range(101):
#     print(x**3 >= x)
for x in range(101):
    if x**3 < x:
        print(f"Found counterexample: x = {x}")
else:
    print("Negated statement is false")
print("3b")
# for x in range(0, 101, 2):
#     print(sympy.isprime(x*3 + 1))   
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

counterexample_found = False

for x in range(2, 101, 2):
    if is_prime(x * 3 + 1) == False:
        counterexample_found = True
        print(f"Found counterexample: x = {x}")
        break

if counterexample_found == False:
    print("Negated statement is false.")
    
print("3c")
def is_prime1(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

counterexample_found1 = False

for x in range(2, 101, 2):
    if is_prime1(x * 5 + 3) == False:
        counterexample_found1 = True
        print(f"Found counterexample: x = {x}")
        break

if counterexample_found == False:
    print("Negated statement is false.")
  
print("3d")
def is_square(n):
    root = int(n ** 0.5)
    return root ** 2 == n

contradiction_found2 = False

for c in range(4, 101, 4):
    for a in range(1, c):
        b = c**2 - a**2
        if is_square(b):
            contradiction_found2 = True
            print(f"Found counterexample: c = {c}, a = {a}, b = {b}")
            break
    if contradiction_found2 == True:
        break

if contradiction_found2 == False:
    print("Negated statement is false")

print("3e")
def is_square1(n):
    root = int(n ** 0.5)
    return root ** 2 == n

counterexample_found3 = False

for c in range(5, 101, 5):
    for a in range(1, c):
        b = c**2 - a**2
        if is_square(b):
            counterexample_found3 = True
            print(f"Found counterexample: c = {c}, a = {a}, b = {b}")
            break
    if counterexample_found3 == True:
        break

if counterexample_found3 == False:
    print("Negated statement is false")
print("3f")
counterexample_found5 = False
for c in range(1, 101):
    if c <= c**2:
        counterexample_found5 = True
        print(f"Found counterexample: c = {c}")
        break
if counterexample_found5 == False:
    print("Negated statement is false")
#bai4
print("BAI4")
print("4a")
suma1=0
for x in range(11):
  for y in range(11):
    suma1 += (x+y)**2

suma2=0
for x in range(11):
  for y in range(11):
    suma2 += (x+2*y)**2

if(suma1>suma2):
    print("true")
else:
  print("false")

print("4b")
sumb = 0
for x in range(11):
  sumb += math.factorial(x)
if(math.factorial(20)<sumb):
  print("true")
else:
  print("false")

print("4c")
sumc=0
for x in range(11):
  sumc += 3*x**2
if(sumc>=10**3):
    print("true")
else:
  print("false")

print("4d")
sumd=0
for x in range(5,11):
  sumd+= 4*x**3 + 6*x**2 + 2*x
if(sumd> 10*4+2*10**3+10*2-5**4-2*5**3-5**2 ):
      print("true")
else:
  print("false")
#bai5
print("BAI5")
print("5a")
print("..................................................")
print('G1 = p -> r')
print('G2= ¬p -> q')
print('G3 =q -> s')
print('G4 = ¬r phu dinh dap an') 
print('G5 =¬s phu dinh dap an')
print('G6 = G1 ^ G4=> ¬p modus tollens')
print('G7 = G6 ^ G2=> q modus ponens ')
print('G8 = G3 ^ G7 => s modus ponens')
print('G9 = G8 ^ G5 => 0')
print("5b")
print("..................................................")
print('G1 = p -> (q → r')
print('G2 = p ∨ s')
print('G3 = t -> q')
print('G4 = ¬s')
print('G5 = ¬r -> ¬t')
print('G6 = G2 ^ G4 => p modus tollens')
print('G7 = G1 ^ G6 => q->r modus ponens')
print("G8 = G3 ^ G6 => t->r tam doan luan")
print("G9 = ¬G8 => ¬t->¬r")
print("5c")
print("..................................................")
print("G1 = p->q")
print("G2 = ¬r v s")
print("G3 = p v r")
print("G4 = ¬(¬q->s)")
print("G5 =¬q tu G4")
print("G6 = ¬s tu G4")
print("G7 = G1 ^ G5 => p -> q ^ ¬q => ¬p  modus ponens")
print("G8 = G2 ^ G6=> ¬r v s ^ ¬s => ¬r modus tollens"  )
print("G9 = G3 ^ G8=> p v r ^ ¬r => p modus tollens" )
print("G10 = G9 ^ G7 => p ^ ¬p = 0")
print("5d")
print("..................................................")
print("G1 = p")
print("G2 = p -> r")
print("G3 = p -> (q ∨ ¬r)")
print("G4 = ¬q ∨ ¬s")
print("G5 = G2^G1 => r modus ponens")
print("G6 = G3 ^ G1 => q ∨ ¬r modus ponens")
print("G7 = G5 ^ G6 => ¬q modus ponens")
print("G8 = G4 ^ G7 => (¬q ∨ ¬s) ^ ¬q = s modus ponens")




