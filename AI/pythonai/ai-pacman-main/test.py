from problems import *
from searchAgents import *

p = SingleFoodSearchProblem()

p.load_from_file('sample_inputs/pacman_single01.txt')

actions = gbfs(p, manhattan_distances)

print(actions, len(actions))
input()

p.animate(actions)

# myObj = MultiFoodSearchProblem()
# myAgent = MultiFoodSearch()

# myQueen = EightQueenProblem()

# myObj.readMaze("input.txt")

# path, move = myAgent.bfs(myObj)

# myObj.animate(path)

# myQueen.readFile("input02.txt")

# print(myQueen.getHeuristic([2,0]))


# myQueen.hill_climbing_search()

# myQueen.printBoard()

# print(myQueen.getHeuristic([5,7]))
