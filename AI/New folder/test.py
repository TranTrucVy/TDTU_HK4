from problem import *
from searchAgents import *


myObj = MultiFoodSearchProblem()
myAgent =MultiFoodSearch()

myQueen = EightQueenProblem()


# myObj.readMaze("input.txt")

path, move = myAgent.bfs(myObj)

myObj.animate(path)

myQueen.readFile("input02.txt")

print(myQueen.getHeuristic([2,0]))


myQueen.hill_climbing_search()

myQueen.printBoard()

print(myQueen.getHeuristic([5,7]))



