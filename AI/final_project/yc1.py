import os

class EightQueenSolver():
    def __init__(self) -> None:
        self.n = 4
        self.queens = []
        self.solvable = False

    @staticmethod
    def _can_attack(queen : tuple[int, int], enemy : tuple[int, int]) -> bool:

        [row_queen, col_queen] = queen
        [row_enemy, col_enemy] = enemy

        if row_queen == row_enemy or col_queen == col_enemy:
            return True
        
        if abs(row_queen - row_enemy) == abs(col_queen - col_enemy):
            return True

        return False

    def _isPossible(self, row : int, col : int) -> bool:

        for queen in self.queens:
            if queen == (row, col):
                continue

            if EightQueenSolver._can_attack(queen, (row, col)):
                return False
        
        return True
    
    def __str__(self) -> str:
        res = [["."]*self.n for i in range(self.n)]
        for queen in self.queens:
            res[queen[0]][queen[1]] = "Q"
        
        return "\n".join([" ".join(res[i]) for i in range(len(res))])

    def _solve_recursive(self, row : int):
        os.system('cls')
        print('Press enter to continue...')
        if (row == self.n):
            print("Answer: \n")
            print(str(self))
            self.solvable = True
            input()
        else:
            print("Solving: \n")
            print(str(self))
            input()

        for j in range(self.n):
            if self._isPossible(row, j):
                self.queens.append((row, j))
                self._solve_recursive(row + 1)
                # Uncomment to end when find 1 solution
                # if self.solvable:
                #     return None
            
            try:
                self.queens.remove((row, j))
            except:
                pass

    def solve(self):
        self._solve_recursive(0)
        if not self.solvable:
            os.system('cls')
            print("UNSOLVABLE")
        else:
            print("SOLVABLE")

p = EightQueenSolver()
p.solve()