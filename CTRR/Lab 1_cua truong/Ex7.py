def mSum(A,B):
  if len(A) != len(B) or len(A[0]) != len(B[0]):
    return "Matrix dimension error"
  C = []
  for i in range(len(A)):
    C.append([])
    for j in range(len(A[i])):
      C[i].append(A[i][j] + B[i][j])
  return C

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
print(mSum(A,B))