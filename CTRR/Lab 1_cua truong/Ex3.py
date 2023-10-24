def sumN(n):
  step=1 if n>0 else -1
  return sum([i for i in range(0,n+step,step)])

print(sumN(2))
print(sumN(-5))