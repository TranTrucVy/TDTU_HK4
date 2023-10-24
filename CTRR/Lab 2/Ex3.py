from itertools import *

table=list(product([False,True],repeat=3))
print('p', 'q', 'r', 'p ∧ q → r', 'r → p ∧ q')
for p,q,r in table:
  print(p, q, r, (not p or q) and r, r and (not p or q))
