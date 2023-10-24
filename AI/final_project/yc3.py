from pysat.solvers import Glucose3
#YC3_1
class EightQueenSolver:
    def __init__(self, n=8):
        self.n = n
        self.solver = Glucose3()
        self.variables = []
        # create variables for each position on the board
        for i in range(n):
            for j in range(n):
                variable = f"{i},{j}"
                self.variables.append(variable)
        self.clauses = []

    def add_clauses(self):
        for i in range(self.n):
            clause = []
            for j in range(self.n):
                clause.append(self.variables.index(f"{i},{j}")+1)
            self.clauses.append(clause)
            for k in range(self.n-1):
                for l in range(k+1, self.n):
                    self.clauses.append([-(self.variables.index(f"{i},{k}")+1), -(self.variables.index(f"{i},{l}")+1)])

        for j in range(self.n):
            clause = []
            for i in range(self.n):
                clause.append(self.variables.index(f"{i},{j}")+1)
            self.clauses.append(clause)
            for k in range(self.n-1):
                for l in range(k+1, self.n):
                    self.clauses.append([-(self.variables.index(f"{k},{j}")+1), -(self.variables.index(f"{l},{j}")+1)])

        for i in range(self.n):
            for j in range(self.n):
                for k in range(i+1, self.n):
                    if j + k - i < self.n:
                        self.clauses.append([-(self.variables.index(f"{i},{j}")+1), -(self.variables.index(f"{k},{j+k-i}")+1)])
                    if j - k + i >= 0:
                        self.clauses.append([-(self.variables.index(f"{i},{j}")+1), -(self.variables.index(f"{k},{j-k+i}")+1)])

    def solve(self):
        self.add_clauses()
        for clause in self.clauses:
            self.solver.add_clause(clause)
        if self.solver.solve():
            model = self.solver.get_model()
            for i in range(self.n):
                row = ""
                for j in range(self.n):
                    if self.variables.index(f"{i},{j}")+1 in model:
                        row += "Q "
                    else:
                        row += ". "
                print(row)
        else:
            print("UNSOLVABLE")
            
solver = EightQueenSolver(n=8)
solver.solve()

#YC3_2
class NQueenSolver:
    def __init__(self, n=8):
        self.n = n
        self.solver = Glucose3()
        self.variables = []
        #self.variables = [[f"{i},{j}" for j in range(1, n+1)] for i in range(1, n+1)]
        #self.variables = [[f"{i},{j}" for j in range(0, n)] for i in range(0, n)]
        # create variables for each position on the board
        for i in range(n):
            for j in range(n):
                variable = f"{i},{j}"
                self.variables.append(variable)
        self.clauses = []

    def add_clauses(self):
        # Create clauses for rows
        for i in range(self.n):
            clause = []
            for j in range(self.n):
                #self.variables.index(variable)+1
                #clause.append(self.variables[i][j])
                clause.append(self.variables.index(f"{i},{j}")+1)
            self.clauses.append(clause)
            for k in range(self.n-1):
                for l in range(k+1, self.n):
                    #self.clauses.append([f"-{self.variables[i][k]}", f"-{self.variables[i][l]}"])
                    #self.clauses.append([-(self.variables[i][k].index+1), -(self.variables[i][l].index+1)])
                    self.clauses.append([-(self.variables.index(f"{i},{k}")+1), -(self.variables.index(f"{i},{l}")+1)])

        # Create clauses for columns
        for j in range(self.n):
            clause = []
            for i in range(self.n):
                #clause.append(self.variables[i][j])
                clause.append(self.variables.index(f"{i},{j}")+1)
            self.clauses.append(clause)
            for k in range(self.n-1):
                for l in range(k+1, self.n):
                    #self.clauses.append([f"-{self.variables[k][j]}", f"-{self.variables[l][j]}"])
                    self.clauses.append([-(self.variables.index(f"{k},{j}")+1), -(self.variables.index(f"{l},{j}")+1)])

        # Create clauses for diagonals
        for i in range(self.n):
            for j in range(self.n):
                for k in range(i+1, self.n):
                    if j + k - i < self.n:
                        #self.clauses.append([f"-{self.variables[i][j]}", f"-{self.variables[k][j+k-i]}"])
                        self.clauses.append([-(self.variables.index(f"{i},{j}")+1), -(self.variables.index(f"{k},{j+k-i}")+1)])
                    if j - k + i >= 0:
                        #self.clauses.append([f"-{self.variables[i][j]}", f"-{self.variables[k][j-k+i]}"])
                        self.clauses.append([-(self.variables.index(f"{i},{j}")+1), -(self.variables.index(f"{k},{j-k+i}")+1)])

    def solve(self):
        self.add_clauses()
        for clause in self.clauses:
            self.solver.add_clause(clause)
        if self.solver.solve():
            model = self.solver.get_model()
            for i in range(self.n):
                row = ""
                for j in range(self.n):
                    #if f"{i+1},{j+1}" in model:
                    if self.variables.index(f"{i},{j}")+1 in model:
                        row += "Q "
                    else:
                        row += ". "
                print(row)
        else:
            print("UNSOLVABLE")
try:
    n = int(input("Enter the number of queens: "))
    if n < 1:
        raise ValueError("The number of queens should be greater than or equal to 1.")
except ValueError as e:
    print(f"Error: {e}")
    
solver = NQueenSolver(n=n)
solver.solve()