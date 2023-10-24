import os


class SingleFoodSearchProblem:
    # Constructor
    def __init__(self):

        self.initState = []
        self.state = []
        self.Node = 0
        self.Maze = []
        self.width = 0
        self.height = 0
        self.goal = []
        self.animateMatrix = []
        self.goalList = []

    # Read Maze function (Using matrix)
    # Input : file input.txt
    # Output : None

    # Chạy hàm này sẽ đọc dữ liệu từ file input.txt
    # Lưu bản đồ vào maze , toạ độ ban đầu vào initState, toạ độ đích vào goal

    def readMaze(self, filename):

        if os.path.exists(filename) != True:
            print("This file doesn't exist. Please try again")
            return

        with open(filename) as f:
            data = f.read()

        s = data.split('\n')
        self.height = len(s)
        # lay ra max width
        self.width = max([len(w) for w in s])

        f.close

        for row in range(self.height):
            tmp = []
            for col in range(len(s[row])):
                if s[row][col] == 'P':
                    self.initState = [row, col]
                    self.state = [row, col]
                    tmp.append(" ")
                elif s[row][col] == '.':
                    self.goal = [row, col]
                    tmp.append(" ")
                else:
                    tmp.append(s[row][col])

            self.Maze.append(tmp)

    # Nhập vào vị trí hiện tại , in ra bản đồ

    def printMaze(self, state):
      # print each row of matrix
        for row in range(self.height):
            for col in range(self.width):
                if [row, col] == [state[0], state[1]]:
                    print("P", end="")
                elif [row, col] == [self.goal[0], self.goal[1]]:
                    print(".", end="")
                else:
                    print(self.Maze[row][col], end="")
            print("")

        # Check the result function

    # So sánh toạ độ hiện tại và toạ độ của goal
    # Đúng thì trả về true
    # Sai thì trả về false

    def goalTest(self, state):
        if state[0] == self.goal[0] and state[1] == self.goal[1]:
            return True
        return False

    def getSuccessor(self):

        subArr = []

        # Check Key of state to get the row and column of Maze

        r = self.state[0]
        c = self.state[1]

        if(self.Maze[r-1][c] != '%'):
            subArr.append([r-1, c])

        if(self.Maze[r+1][c] != '%'):
            subArr.append([r+1, c])

        if(self.Maze[r][c+1] != '%'):
            subArr.append([r, c+1])

        if(self.Maze[r][c-1] != '%'):
            subArr.append([r, c-1])

        return subArr

    def pathCost(self, path):
        if(len(path) == 0):
            print("Can't find path.")
            return 0
        return len(path)

    def animate(self, action: list):
        # print each row of matrix
        for i in range(len(action)):
            os.system('cls')

            self.state = action[i]
            self.printMaze(self.state)

            input("**Press Enter to continue**")


class MultiFoodSearchProblem(SingleFoodSearchProblem):
    # Constructor
    def __init__(self):

        SingleFoodSearchProblem.__init__(self)
        # Danh sách các goal
        self.goalList = []
        # Những goal xét
        self.expandedGoal = []
        # Những goal đã đi qua trong phương thức animate
        self.animatedGoal = []

    def readMaze(self, filename):

        if os.path.exists(filename) != True:
            print("This file doesn't exist.Please try again")
            return

        with open(filename) as f:
            data = f.read()

        s = data.split('\n')
        self.height = len(s)

        self.width = max([len(w) for w in s])

        f.close

        for row in range(self.height):
            tmp = []
            for col in range(len(s[row])):
                if s[row][col] == 'P':
                    self.initState = [row, col]
                    self.state = [row, col]
                    tmp.append(" ")
                elif s[row][col] == '.':
                    self.goalList.append([row, col])
                    tmp.append(" ")
                else:
                    tmp.append(s[row][col])

            self.Maze.append(tmp)

        self.goal = self.goalList[0]

    def printMaze(self, state):
      # print each row of matrix
        for row in range(self.height):
            for col in range(self.width):
                if [row, col] == [state[0], state[1]]:
                    print("P", end="")

                    if[row, col] in self.goalList:
                        self.animatedGoal.append([state[0], state[1]])

                elif [row, col] in self.goalList and [row, col] not in self.animatedGoal:
                    print(".", end="")
                else:
                    print(self.Maze[row][col], end="")

            print("")


class EightQueenProblem:
    def __init__(self) -> None:
        self.initPosition = []
        self.currPosition = []

    def readFile(self, filename):

        if os.path.exists(filename) != True:
            print("This file doesn't exist.Please try again")
            return

        with open(filename) as f:
            data = f.read()

        f.close()

        s = data.split('\n')

        s = [x.replace(" ", "") for x in s]

        if(len(s) != 8 or len(s[0]) != 8):
            print("This is not a chess board. Please try again")
            return

        for row in range(8):
            for col in range(8):
                if(s[row][col] == 'Q'):
                    self.initPosition.append([row, col])

        self.currPosition = self.initPosition.copy()

    def printBoard(self):
        for row in range(8):
            for col in range(8):
                if [row, col] in self.currPosition:
                    print('Q ', end="")
                else:
                    print('0 ', end="")
            print("")

    def isAttacking(self, pos1, pos2):
        if(pos1[0] == pos2[0] or pos1[1] == pos2[1]):
            return True

        diffRow = abs(pos1[0] - pos2[0])
        diffCol = abs(pos1[1] - pos2[1])

        if(diffRow == diffCol):
            return True

        sumPos1 = pos1[0] + pos1[1]
        sumPos2 = pos2[0] + pos2[1]

        if(sumPos1 == sumPos2):
            return True

        return False

    def getHeuristic(self, state):

        numberOfAttackingPair = 0

        tempPosition = self.currPosition.copy()

        for s in tempPosition:
            if(state[1] == s[1]):
                s[0], s[1] = state
                break

        for i in tempPosition:
            for j in tempPosition:
                if i[0] == j[0] and i[1] == j[1]:
                    continue

                if(self.isAttacking(i, j) == True):
                    numberOfAttackingPair += 1

        return (numberOfAttackingPair / 2)

    def getSuccessor(self, col):

        returnedList = []

        for i in range(8):
            returnedList.append([i, col])

        # returnedList.reverse()

        return returnedList

    def hill_climbing_search(self):

        for col in range(8):

            child = self.getSuccessor(col)

            h = []

            for c in child:
                h.append(self.getHeuristic(c))

            minH = min(h)

            index = h.index(minH)


            for p in self.currPosition:
                if p[1] == col:
                    p[0] = child[index][0]
                    p[1] = child[index][1]
                    break

