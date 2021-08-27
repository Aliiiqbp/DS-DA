import math
class Node:

    def __init__(self, index):
        self.index = index
        self.distance = 0


class Directed_graph:

    def __init__(self, n):
        self.matrix = [[0 for i in range(n)] for i in range(n)]
        self.Vertex = [Node(i) for i in range(n)]

    def add_edge(self, a, b, weight):
        self.matrix[a][b] = weight

    def find_min(self, arr):
        temp = math.inf
        node_temp = Node(0)
        for x in self.Vertex:
            if not arr[x.index]:
                if x.distance < temp:
                    temp = x.distance
                    node_temp = x
        return node_temp

    def dijkstra(self, a):
        for x in self.Vertex:
            if x.index != a:
                x.distance = math.inf

        temp_array = [False] * len(self.Vertex)
        for i in range(len(self.Vertex)):
            min_not_visited = self.find_min(temp_array)
            temp_array[min_not_visited.index] = True

            for j in range(len(self.matrix[min_not_visited.index])):
                if self.matrix[min_not_visited.index][j] > 0 and not temp_array[j] and self.matrix[min_not_visited.index][j] + min_not_visited.distance < self.Vertex[j].distance:
                    self.Vertex[j].distance = self.matrix[min_not_visited.index][j] + min_not_visited.distance



line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
line3 = list(map(int, input().split()))
line4 = list(map(int, input().split()))
a, b = map(int, input().split())

graph = Directed_graph(100)

correct = []
for i in range(3):
    if line1[i] == 1:
        correct.append(i + 1)
    if line2[i] == 1:
        correct.append(i + 4)
    if line3[i] == 1:
        correct.append(i + 7)
if line4[1] == 1:
    correct.append(0)

for x in correct:
    for y in correct:
        if x == 0:
            for i in range(100):
                if i != y:
                    graph.add_edge(i, y, 1)
        elif line4[0] == 1:
            for i in range(100):
                if i != x * 10 + y:
                    graph.add_edge(i, x * 10 + y, 3)

for i in range(100):
    if line1[3] == 1:
        graph.add_edge(i, (i + 1) % 100, 1)
    if line2[3] == 1:
        graph.add_edge(i, (i - 1) % 100, 1)

graph.dijkstra(a)
if graph.Vertex[b].distance != math.inf:
    print(graph.Vertex[b].distance)
else:
    print(-1)
