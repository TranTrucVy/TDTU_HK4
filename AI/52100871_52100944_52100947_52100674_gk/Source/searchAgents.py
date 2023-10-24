from fringes import Queue, PriorityQueue
from problems import SingleFoodSearchProblem, MultiFoodSearchProblem, FoodSearchProblem

def manhattan_distances(state: tuple, problem: SingleFoodSearchProblem) -> float:
    manhattan = lambda c_x, c_y, d_x, d_y : abs(c_x - d_x) + abs(c_y - d_y)
    cur_x, cur_y = state
    all_dots = problem.all_dots

    dot_x, dot_y = all_dots[0]

    return manhattan(cur_x, cur_y, dot_x, dot_y)

def euclidean_distances(state: tuple, problem: SingleFoodSearchProblem) -> float:
    euclidean = lambda c_x, c_y, d_x, d_y : ((c_x - d_x)**2 + (c_y - d_y)**2)**0.5
    cur_x, cur_y = state
    all_dots = problem.all_dots

    dot_x, dot_y = all_dots[0]
    
    return euclidean(cur_x, cur_y, dot_x, dot_y)

def shortest_manhattan_distances_multi(state: tuple, problem : MultiFoodSearchProblem):
    manhattan = lambda c_x, c_y, d_x, d_y : abs(c_x - d_x) + abs(c_y - d_y)
    cur_x, cur_y = state
    all_dots = problem.all_dots

    if len(all_dots) == 0:
        return 0
    elif len(all_dots) == 1:
        dot_x, dot_y = all_dots[0]
        return manhattan(cur_x, cur_y, dot_x, dot_y)
    else:
        dot_x, dot_y = all_dots[0]
        res = manhattan(cur_x, cur_y, dot_x, dot_y)
        for dot in all_dots:
            temp = manhattan(cur_x, cur_y, dot[0], dot[1])
            if res > temp:
                res = temp
        return res

def make_node(state, parent = None, action = None):
    return {
        'state': state,
        'parent': parent,
        'action': action
    }

def solution(node):
    res = []

    while node['parent'] != None:
        res.insert(0, node['action'])
        node = node['parent']

    res.append('Stop')

    return res

def recursive_dfs(node: dict, problem: FoodSearchProblem, explored: list, visited: list) -> list:
    if problem.goal_test(node['state']):
        if isinstance(problem, MultiFoodSearchProblem):
            # Remove a dot we that Pacman ate
            problem.all_dots.remove(node['state'])
            # Call dfs for another problem from the current state to find another node
            temp = dfs(MultiFoodSearchProblem(node['state'], make_node(node['state'], None, None), problem.initial_state, problem.all_dots))
            return solution(node)[:-1] + temp if temp != None else solution(node)
        else:
            return solution(node)
    
    explored.append(node['state'])

    all_actions = problem.getSuccessors(node['state'])

    for action in all_actions:
        state_x, state_y = node['state']
        child = {'state': problem.all_actions[action](state_x, state_y), 'parent': node, 'action': action}
        if not ((child['state'] in explored) or (child['state'] in visited)):
            visited.append(child['state'])
            res = recursive_dfs(child, problem, explored, visited)
            if res != None:
                return res

def dfs(problem: FoodSearchProblem) -> list:

    node = problem.node
    
    return dfs_multi(problem, node)

def dfs_multi(problem: FoodSearchProblem, node: dict) -> list:

    visited = [node['state']]
    explored = []

    return recursive_dfs(node, problem, visited, explored)

def ucs(problem : FoodSearchProblem) -> list:
    node = problem.node
    
    if (problem.goal_test(node['state'])):
        return ['Stop']
    
    if (isinstance(problem, MultiFoodSearchProblem) and len(problem.all_dots) == 0):
        return ['Stop']
    
    q = PriorityQueue()
    q.enqueue((0, node))
    explored = []
    visited = [node['state']]

    while not q.empty():
        weight, node = q.dequeue()
        explored.append(node['state'])

        all_actions = problem.getSuccessors(node['state'])

        for action in all_actions:
            state_x, state_y = node['state']
            child = {'state': problem.all_actions[action](state_x, state_y), 'parent': node, 'action': action}
            if not ((child['state'] in explored) or (child['state'] in visited)):
                visited.append(child['state'])
                
                if isinstance(problem, MultiFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        node = make_node(child['state'], None, None)
                        # Remove a dot we that Pacman ate
                        problem.all_dots.remove(child['state'])
                        return solution(child)[:-1] + ucs(MultiFoodSearchProblem(child['state'], node, problem.initial_state, problem.all_dots))
                    else:
                        q.enqueue((weight,child))
                elif isinstance(problem, SingleFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        return solution(child)
                    else:
                        q.enqueue((weight, child))
        
    return None

def bfs(problem : FoodSearchProblem) -> list:

    node = problem.node
    # return if state is goal
    if (isinstance(problem, MultiFoodSearchProblem) and len(problem.all_dots) == 0):
        return ['Stop']
    
    if (problem.goal_test(node['state'])):
        return ['Stop']
    
    # Make queue with the first node
    q = Queue()
    q.enqueue(node)
    explored = []
    visited = [node['state']]

    while not q.empty():
        node = q.dequeue()
        explored.append(node['state'])

        all_actions = problem.getSuccessors(node['state'])

        for action in all_actions:
            state_x, state_y = node['state']
            child = make_node(problem.all_actions[action](state_x, state_y), node, action)
            if not ((child['state'] in explored) or (child['state'] in visited)):
                visited.append(child['state'])
                
                if isinstance(problem, MultiFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        node = make_node(child['state'], None, None)
                        # Remove a dot we that Pacman ate
                        problem.all_dots.remove(child['state'])
                        # Call bfs for another problem from the current state to find another node
                        return solution(child)[:-1] + bfs(MultiFoodSearchProblem(child['state'], node, problem.initial_state, problem.all_dots))
                    else:
                        q.enqueue(child)
                elif isinstance(problem, SingleFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        return solution(child)
                    else:
                        q.enqueue(child)
        
    return None

def astar(problem : FoodSearchProblem, fn_heuristic) -> list:
    node = problem.node
    
    if (problem.goal_test(node['state'])):
        return ['Stop']
    
    if (isinstance(problem, MultiFoodSearchProblem) and len(problem.all_dots) == 0):
        return ['Stop']
    
    q = PriorityQueue()
    q.enqueue((fn_heuristic(node['state'], problem), node))
    explored = []
    visited = [node['state']]

    while not q.empty():
        weight, node = q.dequeue()
        explored.append(node['state'])

        all_actions = problem.getSuccessors(node['state'])

        for action in all_actions:
            state_x, state_y = node['state']
            child = {'state': problem.all_actions[action](state_x, state_y), 'parent': node, 'action': action}
            if not ((child['state'] in explored) or (child['state'] in visited)):
                visited.append(child['state'])
                
                if isinstance(problem, MultiFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        node = make_node(child['state'], None, None)
                        # Remove a dot we that Pacman ate
                        problem.all_dots.remove(child['state'])
                        return solution(child)[:-1] + astar(MultiFoodSearchProblem(child['state'], node, problem.initial_state, problem.all_dots), fn_heuristic)
                    else:
                        q.enqueue((fn_heuristic(child['state'], problem) + weight - fn_heuristic(node['state'], problem) + 1, child))
                elif isinstance(problem, SingleFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        return solution(child)
                    else:
                        q.enqueue((fn_heuristic(child['state'], problem) + weight - fn_heuristic(node['state'], problem) + 1, child))
        
    return None

def gbfs(problem : FoodSearchProblem, fn_heuristic) -> list:
    node = problem.node
    
    if (problem.goal_test(node['state'])):
        return ['Stop']
    
    if (isinstance(problem, MultiFoodSearchProblem) and len(problem.all_dots) == 0):
        return ['Stop']
    
    q = PriorityQueue()
    q.enqueue((fn_heuristic(node['state'], problem), node))
    explored = []
    visited = [node['state']]

    while not q.empty():
        weight, node = q.dequeue()
        explored.append(node['state'])

        all_actions = problem.getSuccessors(node['state'])

        for action in all_actions:
            state_x, state_y = node['state']
            child = {'state': problem.all_actions[action](state_x, state_y), 'parent': node, 'action': action}
            if not ((child['state'] in explored) or (child['state'] in visited)):
                visited.append(child['state'])
                
                if isinstance(problem, MultiFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        node = make_node(child['state'], None, None)
                        # Remove a dot we that Pacman ate
                        problem.all_dots.remove(child['state'])
                        return solution(child)[:-1] + astar(MultiFoodSearchProblem(child['state'], node, problem.initial_state, problem.all_dots), fn_heuristic)
                    else:
                        q.enqueue((fn_heuristic(child['state'], problem), child))
                elif isinstance(problem, SingleFoodSearchProblem):
                    if problem.goal_test(child['state']):
                        return solution(child)
                    else:
                        q.enqueue((fn_heuristic(child['state'], problem), child))
        
    return None

p = MultiFoodSearchProblem()

p.load_from_file('./sample_inputs/pacman_multi01.txt')

actions = gbfs(p, manhattan_distances)

print(actions, len(actions))
input()

p.animate(actions)