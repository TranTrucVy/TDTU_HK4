from itertools import *

table=list(product([False,True],repeat=3))
print('p', 'q', 'r', 'p ≡ ¬(¬p)')
for p,q,r in table:
  print(p, q, r, (not p or not (not p)))

table=list(product([False,True],repeat=3))
print('p', 'q', 'r', '¬(¬q ∧ p) ∧ (q v p) ≡ q')
for p,q,r in table:
  print(p, q, r, (not (not q and p) and (q or p)) == q)

table=list(product([False,True],repeat=3))
print('p', 'q', 'r', '¬(p v q) ≡ (¬p v ¬q)')
for p,q,r in table:
  print(p, q, r, (not (p or q)) == (not p or not q))

table=list(product([False,True],repeat=3))
print('p', 'q', 'r', '(p v q) → r ≡ (p → r) ∧ (q → r)')
for p,q,r in table:
  print(p, q, r, (p or q) or r == (p or r) and (q or r))

table=list(product([False,True],repeat=3))
print('p', 'q', 'r', '¬(p ∧ q) ≡ (¬p ∧ ¬q)')
for p,q,r in table:
  print(p, q, r, (not (p and q)) == (not p and not q))

