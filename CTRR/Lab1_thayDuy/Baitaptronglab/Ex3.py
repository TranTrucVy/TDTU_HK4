def sumN(n):
  st=1 if n>0 else -1
  return sum([i for i in range(0,n+st,st)])

print(sumN(2))
print(sumN(-5))