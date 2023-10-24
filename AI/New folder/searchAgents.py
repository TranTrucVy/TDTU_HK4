from problem import *
from fringes import *
import math


def convertMultiToSingle(myObj: MultiFoodSearchProblem):
    newObj = SingleFoodSearchProblem()

    newObj.initState = myObj.initState
    newObj.state = myObj.state
    newObj.Maze = myObj.Maze
    newObj.width = myObj.width
    newObj.height = myObj.height
    return newObj


def convertPathFromNumberToChar(path):

    convertedPath = []

    for i in range(1, len(path)):

        if(path[i] == path[i-1]):
            continue

        if(path[i][0] != path[i - 1][0]):
            if(path[i][0] > path[i-1][0]):
                convertedPath.append('S')
            else:
                convertedPath.append('N')
        else:
            if(path[i][1] > path[i-1][1]):
                convertedPath.append('E')
            else:
                convertedPath.append('W')

    convertedPath.append('Stop')

    return convertedPath

# Bài 2 ------------------------------------------------

# Yêu cầu 2.1
def f1_heuristic(myObj: SingleFoodSearchProblem) -> int:
    currRow, currCol = myObj.state
    goalRow, goalCol = myObj.goal
    return abs(currRow - goalRow) + abs(currCol - goalCol)


def f2_heuristic(myObj: SingleFoodSearchProblem) -> float:
    currRow, currCol = myObj.state
    goalRow, goalCol = myObj.goal
    euclidDistance = math.sqrt(
        abs(currRow - goalRow) ** 2 + abs(currCol - goalCol) ** 2)
    return euclidDistance

# Yêu cầu 2.2
# Tìm đường đi tới goal gần nhất, từ goal đó đi tiếp tới goal gần nhất, đến khi nào hết thì thôi.
# Tính heuristic tới goal gần nhất, goal gần nhất được lưu trong thuộc tính goal


def f3_heuristic(myObj: MultiFoodSearchProblem, goal) -> int:
    currRow, currCol = myObj.state
    goalRow, goalCol = goal[0], goal[1]
    return abs(currRow - goalRow) + abs(currCol - goalCol)

# Yêu cầu 2.3
# Hàm phụ
# Lấy ra heuristic theo yêu cầu


def getHeuristic(myObj: SingleFoodSearchProblem, switcher) -> float:

    if switcher == 1:
        return f1_heuristic(myObj)
    if switcher == 2:
        return f2_heuristic(myObj)
    return 0

# Trả về goal có heuristic nhỏ nhất


def getNearestGoal(myObj: MultiFoodSearchProblem):
    # Remain Goal là những goal chưa được ăn
    remainGoal = [x for x in myObj.goalList if x not in myObj.expandedGoal]

    if(len(remainGoal) == 0):
        return -1

    # Lấy ra khoảng cách vị trí hiện tại đến các goal còn lại
    distances = [f3_heuristic(myObj, x) for x in remainGoal]

    # nextGoal sẽ là goal có khoảng cách nhỏ nhất
    nextGoal = remainGoal[distances.index(min(distances))]

    return nextGoal


class SingleFoodSearch:

    def bfs(self, myObj: SingleFoodSearchProblem) -> list:

        queue = Queue()
        queue.enqueue(myObj.initState)

        cp_dict = dict()
        cp_dict[myObj.initState[0], myObj.initState[1]] = None

        path = []

        while queue.isEmpty() == False:

            myObj.state = queue.dequeue()

            if myObj.goalTest(myObj.state):
                path.append(myObj.state)
                break

            child = myObj.getSuccessor()

            for s in child:
                if (s[0], s[1]) not in cp_dict:
                    cp_dict[s[0], s[1]] = myObj.state
                    queue.enqueue(s)

        move = []

        if len(path) != 0:
            curr = path[0]
            while(curr != myObj.initState):
                curr = cp_dict[curr[0], curr[1]]
                path.insert(0, curr)

            path.reverse

            move = convertPathFromNumberToChar(path)

        return path, move
    
    def dfs(self, myObj: SingleFoodSearchProblem) -> list:
    
        stack = Stack()
        stack.push(myObj.initState)
        path = []
        cp_dict = dict()
        cp_dict[myObj.initState[0], myObj.initState[1]] = None
        
        while stack.isEmpty() == False:
            
            myObj.state = stack.pop()
            
            if myObj.goalTest(myObj.state):
                move = []
                path.append(myObj.state)
                if len(path) != 0:
                    curr = path[0]
                    while(curr != myObj.initState):
                        curr = cp_dict[curr[0], curr[1]]
                        path.insert(0, curr)

                    move = convertPathFromNumberToChar(path)

                return path, move

            child = myObj.getSuccessor()

            for s in child:
                if (s[0], s[1]) not in cp_dict:
                    cp_dict[s[0], s[1]] = myObj.state
                    stack.push(s)
        return None
    #fixed
    def ucs(self, myObj: SingleFoodSearchProblem) -> list: 
        path = []
        queue = PriorityQueue_1()
        cost_so_far={(myObj.initState[0], myObj.initState[1]):0}
        queue.push(myObj.initState, cost_so_far[(myObj.initState[0], myObj.initState[1])])
        cp_dict = dict()
        cp_dict[myObj.initState[0], myObj.initState[1]] = None

        while queue.isEmpty() == False:

            myObj.state = queue.pop()

            if myObj.goalTest(myObj.state):
                path.append(myObj.state)
                break

            child = myObj.getSuccessor()

            for s in child:
                new_cost = cost_so_far[(myObj.state[0], myObj.state[1])] + 1
                if (s[0], s[1]) not in cost_so_far or new_cost < cost_so_far[(s[0],s[1])]:
                    cost_so_far[s[0],s[1]] = new_cost
                    priority = new_cost
                    queue.push(s,priority)
                    cp_dict[s[0], s[1]] = myObj.state

        move = []
        
        if len(path) != 0:
            curr = path[0]
            while(curr != myObj.initState):
                curr = cp_dict[curr[0], curr[1]]
                path.insert(0, curr)

            path.reverse
            move = convertPathFromNumberToChar(path)

        return path, move
    
    def astar(self, myObj: SingleFoodSearchProblem, fn_heuristic):

        # Dùng để xác định loại heuristic để dùng.
        # Nếu switcher = 0 , tức là loại heuristic không tồn tại.
        switcher = 0

        if fn_heuristic == 'f1_heuristic':
            switcher = 1
        elif fn_heuristic == 'f2_heuristic':
            switcher = 2
        else:
            print("Don't have this kind of heuristic. Please try again.")
            return [], []

        # PriorityQueue (PQ) dùng để lấy ra chi phí nhỏ nhất .
        # PQ khi enqueue sẽ tự động sắp xếp theo thứ từ chi phí từ nhỏ đến lớn
        # Chi phí được tính toán theo công thức A* : heuristic tại vị trí đó + số node cha của state hiện tại
        myPQ = PriorityQueue()

        path = []

        # Dùng để truy xuất đến cha của state hiện tại.
        # Với key là node con, value là node cha.
        # parent của node bắt đầu là None
        cp_dict = dict()

        # Số node cha của node hiện tại
        # Key là toạ độ, value là số node cha.
        totalWeight_dict = dict()

        initRow = myObj.state[0]
        initCol = myObj.state[1]

        cp_dict[initRow, initCol] = None
        totalWeight_dict[initRow, initCol] = 0

        # Thiết lập giá trị bắt đầu cho PQ trước khi đi vào vòng while
        initCost = getHeuristic(myObj, switcher)
        myPQ.enqueue([initCost, myObj.state])

        while(myPQ.isEmpty() == False):

            currNode = myPQ.dequeue()

            myObj.state = currNode[1]
            currRow = myObj.state[0]
            currCol = myObj.state[1]

            if myObj.goalTest(myObj.state):
                path.append(myObj.state)
                break

            child = myObj.getSuccessor()

            for s in child:
                if (s[0], s[1]) not in cp_dict:
                    cp_dict[s[0], s[1]] = myObj.state

                    currTW = totalWeight_dict[currRow, currCol]

                    totalWeight_dict[s[0], s[1]] = currTW + 1

                    tempObj = SingleFoodSearchProblem()

                    tempObj.state = [s[0], s[1]]
                    tempObj.goal = myObj.goal

                    cost = currTW + 1 + getHeuristic(tempObj, switcher)

                    myPQ.enqueue([cost, tempObj.state])

        move = []

        if len(path) != 0:
            curr = path[0]

            # Trường hợp initState == goal
            # => len(cp_dict) == 1 (cp_dict[initRow, initCol] = None)
            # => Vòng lặp While Không thể duyệt cp_dict => Lỗi
            if len(cp_dict) == 1:
                move = convertPathFromNumberToChar(path)
                return path, move

            while(curr != myObj.initState):
                curr = cp_dict[curr[0], curr[1]]
                path.insert(0, curr)

            path.reverse

            move = convertPathFromNumberToChar(path)

        return path, move

    def gbfs(self, myObj: SingleFoodSearchProblem, fn_heuristic) -> list:
        f_switch = 0
        if fn_heuristic == 'f1_heuristic':
            f_switch = 1
        elif fn_heuristic == "f2_heuristic":
            f_switch = 2
        else:
            print("Don't have", fn_heuristic, "Please choose another one")
            return [], []

        myPQ = PriorityQueue()
        path = []
        move = []
        parent_dict = dict()

        myPQ.enqueue([getHeuristic(myObj, f_switch), myObj.state])
        parent_dict[myObj.state[0], myObj.state[1]] = None

        while(myPQ.isEmpty() != True):
            currNode = myPQ.dequeue()
            myObj.state = currNode[1]

            if myObj.goalTest(myObj.state):
                path.append(myObj.state)
                break

            child = myObj.getSuccessor()
            for successor in child:
                if (successor[0], successor[1]) not in parent_dict:
                    parent_dict[successor[0], successor[1]] = myObj.state

                    tempObj = SingleFoodSearchProblem()
                    tempObj.state = (successor[0], successor[1])
                    tempObj.goal = myObj.goal
                    myPQ.enqueue(
                        [getHeuristic(tempObj, f_switch), tempObj.state])

        if len(path) != 0:
            curr = path[0]

            # Trường hợp initState == goal
            # len(parent_dict) == 1
            if len(parent_dict) <= 1:
                move = convertPathFromNumberToChar(path)
                return path, move

            while(curr != myObj.initState):
                curr = parent_dict[curr[0], curr[1]]
                path.insert(0, curr)

            path.reverse
            move = convertPathFromNumberToChar(path)

        return path, move


# Yếu cầu 2.4 , 2.5

class MultiFoodSearch:

    def bfs(self, myObj: MultiFoodSearchProblem):

        myAgent = SingleFoodSearch()

        totalPath = []

        while(len(myObj.expandedGoal) != len(myObj.goalList)):

            tempObj = convertMultiToSingle(myObj)

            remainGoal = [
                x for x in myObj.goalList if x not in myObj.expandedGoal]

            tempObj.goal = remainGoal[0]

            path, move = myAgent.bfs(tempObj)

            totalPath += path

            passedGoal = [x for x in remainGoal if x in path]

            myObj.expandedGoal += passedGoal

            myObj.initState = remainGoal[0]

        move = convertPathFromNumberToChar(totalPath)

        return totalPath, move

    def dfs(self, myObj: MultiFoodSearchProblem):

        myAgent = SingleFoodSearch()

        totalPath = []

        while(len(myObj.expandedGoal) != len(myObj.goalList)):

            tempObj = convertMultiToSingle(myObj)

            remainGoal = [
                x for x in myObj.goalList if x not in myObj.expandedGoal]

            tempObj.goal = remainGoal[0]

            path, move = myAgent.dfs(tempObj)

            totalPath += path

            passedGoal = [x for x in remainGoal if x in path]

            myObj.expandedGoal += passedGoal

            myObj.initState = remainGoal[0]

        move = convertPathFromNumberToChar(totalPath)

        return totalPath, move

    def ucs(self, myObj: MultiFoodSearchProblem):

        myAgent = SingleFoodSearch()

        totalPath = []

        while(len(myObj.expandedGoal) != len(myObj.goalList)):

            tempObj = convertMultiToSingle(myObj)

            remainGoal = [
                x for x in myObj.goalList if x not in myObj.expandedGoal]

            tempObj.goal = remainGoal[0]

            path, move = myAgent.ucs(tempObj)

            totalPath += path

            passedGoal = [x for x in remainGoal if x in path]

            myObj.expandedGoal += passedGoal

            myObj.initState = remainGoal[0]

        move = convertPathFromNumberToChar(totalPath)

        return totalPath, move

    def astar(self, myObj: MultiFoodSearchProblem):
        # Gọi hàm astar từ singleFoodSearch

        # Remain Goal là những goal chưa được ăn

        nextGoal = getNearestGoal(myObj)

        myAgent = SingleFoodSearch()

        totalPath = []

        while(nextGoal != -1):

            tempObj = convertMultiToSingle(myObj)

            tempObj.goal = nextGoal
            tempObj.initState = myObj.state

            path, move = myAgent.astar(tempObj, "f1_heuristic")

            #
            remain = [x for x in myObj.goalList if x not in myObj.expandedGoal]

            passedGoal = [x for x in remain if x in path]

            myObj.expandedGoal += passedGoal

            totalPath += path

            myObj.state = nextGoal

            nextGoal = getNearestGoal(myObj)

        move = convertPathFromNumberToChar(totalPath)

        return totalPath, move

    def gbfs(self, myObj: MultiFoodSearchProblem, fn_heuristic):

        if fn_heuristic != 'f1_heuristic' and fn_heuristic != "f2_heuristic":
            return [], []

        nextGoal = getNearestGoal(myObj)

        myAgent = SingleFoodSearch()

        totalPath = []

        while(nextGoal != -1):

            tempObj = convertMultiToSingle(myObj)

            tempObj.goal = nextGoal
            tempObj.initState = myObj.state

            path, move = myAgent.gbfs(tempObj, fn_heuristic)

            #
            remain = [x for x in myObj.goalList if x not in myObj.expandedGoal]

            passedGoal = [x for x in remain if x in path]

            myObj.expandedGoal += passedGoal

            totalPath += path

            myObj.state = nextGoal

            nextGoal = getNearestGoal(myObj)

        move = convertPathFromNumberToChar(totalPath)

        return totalPath, move
