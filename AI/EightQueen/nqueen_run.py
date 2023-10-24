from NQueenSolver import NQueenSolver

try:
    n = int(input("Enter the number of queens: "))
    if n < 1:
        raise ValueError("The number of queens should be greater than or equal to 1.")
except ValueError as e:
    print(f"Error: {e}")

solver = NQueenSolver(n=n)
solver.solve()