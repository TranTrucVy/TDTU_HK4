import os

class FoodSearchProblem():
    def load_from_file(self, filename: str) -> None:
        pass
    def getSuccessors(self, cell: tuple) -> list:
        pass
    def goal_test(self, node: tuple) -> bool:
        pass
    def animate(self, actions: list) -> None:
        pass
    # Private method
    def _get_all_dots(self, map: list) -> list:
        pass
    def _getP(self, map: list) -> tuple:
        pass

class SingleFoodSearchProblem(FoodSearchProblem):
    def __init__(self, state = (), node = {'state': (), 'parent': None, 'action': None}, initial_state = [], all_dots = []):
        self.state = state
        self.node = node
        self.initial_state = initial_state
        left = lambda x , y : (x, y - 1)
        right = lambda x , y : (x, y + 1)
        up = lambda x , y : (x - 1, y)
        down = lambda x , y : (x + 1, y)
        self.all_actions = {'N': up, 'S': down, 'W': left, 'E': right}
        self.all_dots = all_dots
    
    def __str__(self) -> str:
        res = ''
        for line in self.initial_state:
            res += ''.join(line) + '\n'
        return res

    def load_from_file(self, filename: str) -> None:
        if os.path.exists(filename):
            with open(filename) as f:
                self.initial_state = [list(line.replace('\n', '')) for line in f]
        
        self.state = self._getP(self.initial_state)
        self.all_dots = self._get_all_dots(self.initial_state)
        self.node['state'] = self.state
        
    def _get_all_dots(self, map: list) -> list:
        res = []
        
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == '.':
                    res.append((i, j))
        return res

    def _getP(self, map: list) -> tuple:
        for i in range(len(map)):
            try:
                return (i, map[i].index('P'))
            except:
                pass
        
        return ()

    def _is_valid(self, cell: tuple) -> bool:
        row , col = cell
        if row < 0 and col < 0:
            return False
        try:
            return self.initial_state[row][col] != '%'
        except:
            return False        

    def getSuccessors(self, cell: tuple) -> list:
        row, col = cell

        all_successors = []

        for action in self.all_actions:
            successor = self.all_actions[action](row, col)
            if self._is_valid(successor):
                all_successors.append(action)
        
        return all_successors

    def goal_test(self, node: tuple) -> bool:
        return self.initial_state[node[0]][node[1]] == '.'
    
    def animate(self, actions: list):
        map = self.initial_state
        os.system('cls')
        print(str(self))
        input()
        cur_r, cur_c = self._getP(map)
        for i in actions:
            if i in self.all_actions.keys():

                new_r, new_c = self.all_actions[i](cur_r, cur_c)
                map[cur_r][cur_c] = ' '
                map[new_r][new_c] = 'P'
                cur_r, cur_c = new_r, new_c
                os.system('cls')
                print(str(SingleFoodSearchProblem(initial_state=map)))
                input()

class MultiFoodSearchProblem(SingleFoodSearchProblem):
    def __init__(self, state=(), node={ 'state': (),'parent': None,'action': None }, initial_state=[], all_dots = []):
        super().__init__(state, node, initial_state)
        self.all_dots = all_dots
    
    def load_from_file(self, filename: str) -> None:
        if os.path.exists(filename):
            with open(filename) as f:
                self.initial_state = [list(line.replace('\n', '')) for line in f]
        
        self.state = self._getP(self.initial_state)
        self.all_dots = self._get_all_dots(self.initial_state)
        self.node['state'] = self.state
    
    def goal_test(self, state) -> bool:
        return state in self.all_dots

# YC3-1
class EightQueenProblem():

    def __init__(self, state = [], n = 8):
        self.state = state
        self.state.sort(key = lambda x: x[1])
        self.number_of_queen = n

    def __str__(self) -> str:
        temp = [['0']*self.number_of_queen for j in range(self.number_of_queen)]

        for x_q, y_q in self.state:
            temp[x_q][y_q] = 'Q'

        res = [' '.join(line) for line in temp]

        return '\n'.join(res)
    
    def print(self) -> None:
        print(str(self))

    # YC3-1 load from file
    def load_from_file(self, filename: str) -> None:
        if os.path.exists(filename):
            with open(filename) as f:
                self.state = [line.rstrip().split() for line in f]
        all_queens = []
        self.number_of_queen = len(self.state)
        for i in range(self.number_of_queen):
            for j in range(self.number_of_queen):
                if self.state[i][j] == 'Q':
                    all_queens.append((i,j))
        self.state = all_queens
        self.state.sort(key = lambda x: x[1])

    def successor_for_col(self, col: int) -> list:
        res = []
        all_qs_except_selected = []
        selected_q = None
        for x_q, y_q in self.state:
            if (y_q == col):
                selected_q = (x_q, y_q)
            else:
                all_qs_except_selected.append((x_q, y_q))
    
        for i in range(8):
            res.append(all_qs_except_selected + [(i, selected_q[1])])
        
        return res

    def best_successor(self):
        for i in range(self.number_of_queen):
            min_successor = self.number_of_queen ** 2
            min_successor_state = []
            successor_i = self.successor_for_col(i)
            for successor in successor_i:
                heuristic = h(EightQueenProblem(successor))
                if ( heuristic <= min_successor):
                    min_successor = heuristic
                    min_successor_state = successor
            self.state = min_successor_state
            self.state.sort(key = lambda x: x[1])
    # YC3-2
    def hill_climbing_search(self):
        p_state = self.state
        while True:
            self.best_successor()
            if (p_state == self.state):
                break
            else:
                p_state = self.state

def attack(queen: tuple, enemy: tuple) -> bool:
    x_q, y_q = queen
    x_e, y_e = enemy

    return False if queen == enemy else abs(x_q - x_e) == abs(y_q - y_e) or (x_e == x_q) or (y_e == y_q)

# YC3-1 h function
def h(state: EightQueenProblem) -> int:
    all_queens = state.state
    res = 0
    for queen in all_queens:
        res += [attack(queen, enemy) for enemy in all_queens].count(True)
    
    return res // 2
