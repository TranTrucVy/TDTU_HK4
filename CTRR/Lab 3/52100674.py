print("BAI1")
def printa(ex, D, P):
  print(ex)
  print("D is '", D, "'" )
  print("P is '", P, "'")
  print("Formal form: For all x in D, P(x)\n")

def printb(ex, D, P):
  print(ex)
  print("D is '", D, "'" )
  print("P is '", P, "'")
  print("Formal form: Exist x in D such that P(x)\n")

printa("a)", "For all fishes", "need water to survive")
printb("b)", "people", "is left handed")
printb("c)", "employees in the company", "is late to work everyday")
printa("d)", "fishes in this pond", "are Koi fish")
printa("e)", "creatures in the ocean", "can live on land")
printa("d)", "students in class A", "do not pass the test")

print("---------------------------------------------------------------------------------------------")
print("BAI2")
def formalConvert(S):
  D, P = S.split(", ")
  if D.count("For all "):
    D = D.split("For all ")[1]
  elif D.count("Exist "):
    D = D.split("Exist ")[1]
  elif D.count("There is at least one "):
    D = D.split("There is at least one ")[1]
  else: print("Not support this type of D")

  P = P[:-1]
  P = P.split(" ")
  P = P[1:]
  P = ' '.join(P)
  print("D is '", D, "'")
  print("P is '", P, "'")

print("a)")
formalConvert("For all fishes, they need water to survive.") 
print("\nb)")
formalConvert("Exist a person, who is left handed.") 
print("\nc)")
formalConvert("Exist an employee in the company, who is late to work everyday.") 
print("\nd)")
formalConvert("For all fishes in this pond, they are Koi fish.") 
print("\ne)")
formalConvert("There is at least one creature in the ocean, it can live on land.") 

print("---------------------------------------------------------------------------------------------")
print("BAI3")
def printa(ex, D, P, Q):
  print(ex)
  print("D is '", D, "'" )
  print("P is '", P, "'")
  print("Q is '", Q, "'")
  print("Formal form: For all x in D, P(x) then Q(x).\n")

def printb(ex, D, P, Q):
  print(ex)
  print("D is '", D, "'" )
  print("P is '", P, "'")
  print("Q is '", Q, "'")
  print("Formal form: Exist x in D such that P(x) then Q(x).\n")

printa("a)", "people", "is blond", "is westerner")
printb("b)", "people", "has black hair", "is a westerner")
printa("c)", "students", "studies correctly", "has high score")
printa("d)", "mammals", "live in the sea", "are either dolphins or whales")
printa("e)", "birds", "does not have wings and can swim", "is penguins")
printb("f)", "birds", "has wing", "can not fly")

print("---------------------------------------------------------------------------------------------")
print("BAI4")
def formalConvertPQ(S):
  D = P = Q = ''
  if S.count(", ") == 2:
    D, P, Q = S.split(", ")
  else:
    D, P = S.split(", ")
  
  # Xu ly D
  if D.count("For all "):
    D = D.split("For all ")[1]
  elif D.count("Exist "):
    D = D.split("Exist ")[1]
  elif D.count("There is at least one "):
    D = D.split("There is at least one ")[1]
  elif D.count("For every "):
    D = D.split("For every ")[1]
  else: print("Not support this type of D")

  # Xu ly P, Q
  if P.count(" then "): 
    P, Q = P.split(" then ")
    P = ' '.join(P.split(" ")[2:])
    Q = ' '.join(Q[:-1].split(" ")[1:])

  elif P.count(" but "):
    P, Q = P.split(" but ")
    P = ' '.join(P.split(" ")[1:])
  
  elif S.count(", ") == 2:
    P = ' '.join(P.split(" ")[2:])
    Q = ' '.join(Q.split(" ")[1:])

  print("D is '", D, "'")
  print("P is '", P, "'")
  print("Q is '", Q, "'")

print("a)")
formalConvertPQ("For all people, if they are blond then they are westerners.")
print("\nb)")
formalConvertPQ("Exist a person, whose hair is black but is a westerner.")
print("\nc)")
formalConvertPQ("For all students, if they study correctly then they have high score.")
print("\nd)")
formalConvertPQ("For every mammal, if they live in the sea, they are either dolphins or whales.")
print("\ne)")
formalConvertPQ("For every bird, if they don’t have wings and can swim then they are penguins.")
print("\nf)")
formalConvertPQ("Exist a bird, who have wing but can’t fly.")

print("---------------------------------------------------------------------------------------------")
print("BAI5")
def nega(A):
  dic = {"For all ": "Exist ", "Exist ": "For all ", "There is at least one ": "Exist "}
  tobenot = {" is ": " isn't ", " are ": " aren't ", " can ": " can't ", " not ": " "}
  subject_verbs = {" they ": " they don't "}

  for i in dic:
    if i in A:
      A = A.replace(i, dic[i])
      break
  
  c = False
  for i in tobenot:
    if i in A:
      A = A.replace(i, tobenot[i])
      c = True

  if (c):
    print(A)
  else:
    for i in subject_verbs:
      if i in A:
        A = A.replace(i, subject_verbs[i])
    print(A)

  
print("a)")
nega("For all fishes, they need water to survive.")
print("\nb)")
nega("Exist a person, who is left handed")
print("\nc)")
nega("Exist an employee in the company, who is late to work everyday.")
print("\nd)")
nega("For all fishes in this pond, they are Koi fish.")
print("\ne)")
nega("There is at least one creature in the ocean, it can live on land")
