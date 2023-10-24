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
