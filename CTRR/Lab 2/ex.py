from itertools import *

table1=list(product([False,True],repeat=3))
def truth_table7():
  print('p', 'q', 'r', 'p v (q ∧ r)', '((p v q) ∧ (p v r))', 't v ¬t', '(p v (q ∧ r)) ↔ (((p v q) ∧ (p v r)) ∧ (t v ¬t))')
  for p,q,r in table1:
    print(p, q, r, p or (q and r), (p or q) and (p or r), True or not True, (p or (q and r)) == (((p or q) and (p or r)) and (True or not True)))
truth_table7()