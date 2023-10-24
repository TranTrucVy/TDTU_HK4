from itertools import *
#bai1
def lImplies(p,q):
  return not p or q

def lAnd(p,q):
  return p and q

def lOr(p,q):
  return p or q

def lXor(p,q):
  return p != q

def lNot(p):
  return not p  

def lEquivalent(p,q):
  return p == q

p = True
q = False
print("p = ", p)
print("q = ", q)
print("p implies q = ", lImplies(p,q))
print("p and q = ", lAnd(p,q))
print("p or q = ", lOr(p,q))
print("p xor q = ", lXor(p,q))
print("not p = ", lNot(p))
print("p equivalent q = ", lEquivalent(p,q))

#bai2
def lLImplies(P, Q):
  return [not p or q for p, q in zip(P, Q)]

def lLAnd(P, Q):
  return [p and q for p, q in zip(P, Q)]

def lLOr(P, Q):
  return [p or q for p, q in zip(P, Q)]

def lLXor(P, Q):
  return [p != q for p, q in zip(P, Q)]

def lLNot(P):
  return [not p for p in P]

def lLEquivalent(P, Q):
  return [p == q for p, q in zip(P, Q)]

P = [True, True, False, False]
Q = [True, False, True, False]
print("P = ", P)
print("Q = ", Q)
print("P implies Q = ", lLImplies(P, Q))
print("P and Q = ", lLAnd(P, Q))
print("P or Q = ", lLOr(P, Q))
print("P xor Q = ", lLXor(P, Q))
print("not P = ", lLNot(P))
print("P equivalent Q = ", lLEquivalent(P, Q))

#bai3
tr_table=list(product([False,True],repeat=2))
def truth_table():
  print('p','\t', 'q','\t', 'p v q','\t', 'p ∧ q', '\t','¬p v ¬q')
  for p,q in tr_table:
      print(p,'\t', q,'\t', p or q,'\t', p and q,'\t', not p or not q)


#bai4
tr_table2=list(product([False,True],repeat=3))

def truth_table2():
  print('p', '\t', 'q', '\t', 'r', '\t','¬p v (q ∧ r)', '\t', 'r')
  for p,q,r in tr_table2:
        print(p,'\t', q,'\t', r, '\t',not p or (q and r), '\t\t',r)

def truth_table3():
  print('p','\t', 'q','\t', 'r', '\t','(p → q)', '\t','(q → r)','\t', '(p → q) ∧ (q → r)')
  for p,q,r in tr_table2:
        print(p,'\t', q,'\t', r,'\t', not p or q,'\t\t', not q or r,'\t\t', (not p or q) and (not q or r))

def truth_table4():
  print('p','\t', 'q','\t', 'r','\t', '(p v (q ∧ r))','\t', '((p v q) ∧ (p v r))')
  for p,q,r in tr_table2:
        print(p, '\t',q,'\t', r,'\t', p or (q and r), '\t\t',(p or q) and (p or r))

def truth_table5():
  print('p','\t', 'q','\t', 'r','\t', 'p v q', '\t','¬r v t','\t', 'p v q → ¬r v t')
  for p,q,r in tr_table2:
        print(p,'\t', q,'\t', r,'\t', p or q,'\t', not r or True,'\t\t', (p or q) and (not r or True))

table6=list(product([False,True],repeat=4))
def truth_table6():
  print('p','\t', 'q','\t', 'r','\t', 'p v t','\t', 'q', '\t','r','\t', 't','\t', 'p v t → q → (r → t)')
  for p,q,r,t in table6:
          print(p,'\t', q,'\t', r,'\t', p or True,'\t', q,'\t', r,'\t', t,'\t', (p or True) and q and (r or t))

def truth_table7():
  print('p','\t', 'q','\t', 'r','\t', 'p v (q ∧ r)','\t', '((p v q) ∧ (p v r))','\t', 't v ¬t','\t', '(p v (q ∧ r)) ↔ (((p v q) ∧ (p v r)) ∧ (t v ¬t))')
  for p,q,r in tr_table2:
        print(p,'\t', q,'\t', r,'\t', p or (q and r),'\t\t', (p or q) and (p or r),'\t\t\t', True or not True,'\t\t', (p or (q and r)) == (((p or q) and (p or r)) and (True or not True)))

truth_table()
truth_table2()
truth_table3()
truth_table4()
truth_table5()
truth_table6()
truth_table7()


def truth_table():
  print('p', 'q', 'p v q', 'p ∧ q', '¬p v ¬q')
  for p in [True, False]:
    for q in [True, False]:
      print(p, q, p or q, p and q, not p or not q)

def truth_table2():
  print('p', 'q', 'r', '¬p v (q ∧ r)', 'r')
  for p in [True, False]:
    for q in [True, False]:
      for r in [True, False]:
        print(p, q, r, not p or (q and r), r)

def truth_table3():
  print('p', 'q', 'r', '(p → q)', '(q → r)', '(p → q) ∧ (q → r)')
  for p in [True, False]:
    for q in [True, False]:
      for r in [True, False]:
        print(p, q, r, not p or q, not q or r, (not p or q) and (not q or r))

def truth_table4():
  print('p', 'q', 'r', '(p v (q ∧ r))', '((p v q) ∧ (p v r))')
  for p in [True, False]:
    for q in [True, False]:
      for r in [True, False]:
        print(p, q, r, p or (q and r), (p or q) and (p or r))

def truth_table5():
  print('p', 'q', 'r', 'p v q', '¬r v t', 'p v q → ¬r v t')
  for p in [True, False]:
    for q in [True, False]:
      for r in [True, False]:
        print(p, q, r, p or q, not r or True, (p or q) and (not r or True))

def truth_table6():
  print('p', 'q', 'r', 'p v t', 'q', 'r', 't', 'p v t → q → (r → t)')
  for p in [True, False]:
    for q in [True, False]:
      for r in [True, False]:
        for t in [True, False]:
          print(p, q, r, p or True, q, r, t, (p or True) and q and (r or t))

def truth_table7():
  print('p', 'q', 'r', 'p v (q ∧ r)', '((p v q) ∧ (p v r))', 't v ¬t', '(p v (q ∧ r)) ↔ (((p v q) ∧ (p v r)) ∧ (t v ¬t))')
  for p in [True, False]:
    for q in [True, False]:
      for r in [True, False]:
        print(p, q, r, p or (q and r), (p or q) and (p or r), True or not True, (p or (q and r)) == (((p or q) and (p or r)) and (True or not True)))


truth_table()
truth_table2()
truth_table3()
truth_table4()
truth_table5()
truth_table6()
truth_table7()

#bai6
table = list(product([False,True],repeat=3))
for(p,q,r,s) in table:
  prem1 = lImplies(p,r)
  prem2 = lImplies(not p,q)
  prem3 = lImplies(q,s)
  con = lImplies(not r,s)
  if(prem1 and prem2 and prem3):
    print("Valid")
    if not con:
      print("Invalid")
      break
  else:
    print("")
  