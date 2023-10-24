from fringes import *
from problems import *


def bfs(problem):
    fringe = Queue()
    fringe.push((problem.getStartState(), []))
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.pop()
        if node not in visited:
            visited.add(node)
            successors = reversed(problem.getSuccessors(node))
            for child, action, cost in successors:
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.delete_elements(fringe.size())
                fringe.push((node, []))
                if problem.getNumFood() == 0:
                    return temp
    return []


def dfs(problem):
    fringe = Stack()
    fringe.push((problem.getStartState(), []))
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.pop()
        if node not in visited:
            visited.add(node)
            successors = reversed(problem.getSuccessors(node))
            for child, action, cost in successors:
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.delete_elements(fringe.size())
                fringe.push((node, []))
                if problem.getNumFood() == 0:
                    return temp
    return []

def ucs(problem):
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.get()
        if node not in visited:
            visited.add(node)
            for child, action, cost in problem.getSuccessors(node):
                x,y=child
                if problem.isValidMove(x,y) and child not in visited:
                    fringe.push((child, actions + [action]), problem.getCostOfActions(actions + [action]))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.clear_priority_queue()
                fringe.push((node, []), 0)
                if problem.getNumFood() == 0:
                    return temp
    return []

def manhattanHeuristic(state, problem):
    if isinstance(problem, MultiFoodSearchProblem):
        food = problem.goalState
        x_f, y_f = food[0]
    else:
        x_f, y_f = problem.goalState
    x, y = state
    return abs(x-x_f) + abs(y-y_f)

def euclideanHeuristic(state, problem):
    if isinstance(problem, MultiFoodSearchProblem):
        food = problem.goalState
        x_f, y_f = food[0]
    else:
        x_f, y_f = problem.goalState
    x, y = state
    return ((x-x_f)**2 + (y-y_f)**2)**0.5


def foodHeristic(state, problem):
    def getDistance(x1, y1, x2, y2):
        return ((x1-x2)**2 + (y1-y2)**2)**0.5
    x,y=state
    if isinstance(problem,SingleFoodSearchProblem):
        x_f,y_f=problem.goalState
        return getDistance(x,y,x_f,y_f)
    else:
        return min([getDistance(x,y,x_f,y_f) for x_f,y_f in problem.goalState])

def astar(problem, fn_heuristic):
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.get()
        if node not in visited:
            visited.add(node)
            for child, action, cost in problem.getSuccessors(node):
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]),
                    problem.getCostOfActions(actions + [action]) + fn_heuristic(child, problem))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.clear_priority_queue()
                fringe.push((node, []), 0)
                if problem.getNumFood() == 0:
                    return temp
    return []

def gbfs(problem, fn_heuristic):
    fringe = PriorityQueue()
    fringe.push((problem.getStartState(), []), 0)
    visited = set()
    temp = []
    while not fringe.is_empty():
        node, actions = fringe.get()
        if node not in visited:
            visited.add(node)
            for child, action, cost in problem.getSuccessors(node):
                x, y = child
                if problem.isValidMove(x, y) and child not in visited:
                    fringe.push((child, actions + [action]), fn_heuristic(child, problem))
        if problem.isGoalState(node):
            if isinstance(problem, SingleFoodSearchProblem):
                return actions
            else:
                temp += actions
                problem.goalState.remove(node)
                visited.clear()
                fringe.clear_priority_queue()
                fringe.push((node, []), 0)
                if problem.getNumFood() == 0:
                    return temp

    return []



