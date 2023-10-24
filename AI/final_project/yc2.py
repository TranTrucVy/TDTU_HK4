import os

dir_path = "/content/sample_data/"

filename = "minimax.txt"

file_path = os.path.join(dir_path, filename)

class Node:
    def __init__(self, identifier="", value=0):
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"({self.identifier}, {self.value})"


class MinimaxDecision:
    def __init__(self):
        self.root = None
        self.terminalStates = {}
        self.successors = {}

    def read(self, filename):
        with open(filename, "r") as f:
            e, l = map(int, f.readline().split())
            for _ in range(e):
                a, b = f.readline().split()
                if a not in self.successors:
                    self.successors[a] = []
                self.successors[a].append(Node(b))
            for _ in range(l):
                a, v = f.readline().split()
                self.terminalStates[a] = int(v)
                if a not in self.successors:
                    self.successors[a] = []

        self.root = Node("n00")

    def print_node(self, node, visited):
        print(node)
        visited.add(node.identifier)
        for successor in self.successors[node.identifier]:
            if successor.identifier not in visited:
                self.print_node(successor, visited)

    def print(self):
        self.print_node(self.root, set())

    def minimax(self, node, maximizingPlayer):
        if node.identifier in self.terminalStates:
            return self.terminalStates[node.identifier]

        if maximizingPlayer:
            bestValue = -float("inf")
            for successor in self.successors[node.identifier]:
                v = self.minimax(successor, False)
                bestValue = max(bestValue, v)
            node.value = bestValue
            return bestValue
        else:
            bestValue = float("inf")
            for successor in self.successors[node.identifier]:
                v = self.minimax(successor, True)
                bestValue = min(bestValue, v)
            node.value = bestValue
            return bestValue

    def run(self):
        self.minimax(self.root, True)


decision = MinimaxDecision()
decision.read(file_path)
decision.run()
decision.print()
