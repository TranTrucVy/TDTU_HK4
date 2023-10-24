print(zip)
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

