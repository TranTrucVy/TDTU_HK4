def ithCombine(p,q):
  return "if " + p + ", then " + q

def panqCombine(p,q):
  return p + " and not " + q

def npoqCombine(p,q):
  return "not " + p + ", or " + q

p = "it sunny"
q = "I go camping"
print(ithCombine(p,q))
print(panqCombine(p,q))
print(npoqCombine(p,q))

