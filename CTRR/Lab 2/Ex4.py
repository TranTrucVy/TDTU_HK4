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