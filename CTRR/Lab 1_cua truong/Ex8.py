def mProd(A,B):
  if len(A[0]) != len(B):
    return "Matrix dimension error"
  C = []
  for i in range(len(A)):
    C.append([])
    for j in range(len(B[0])):
      C[i].append(0)
      for k in range(len(B)):
        C[i][j] += A[i][k] * B[k][j]
  return C

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
print(mProd(A,B))