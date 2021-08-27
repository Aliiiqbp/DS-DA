from collections import defaultdict

class Node:

    def __init__(self, n):
        self.index = n
        self.cnt = [0, 0]


class Tree:

    def __init__(self, n):
        self.V = [Node(i) for i in range(n)]
        self.E = defaultdict(list)
        self.length = n

    def add_edge(self, x, y):
        self.E[x].append(y)
        self.E[y].append(x)


def BFS(tree, a, flag = 0):
    seen = [False] * tree.length
    temp, out = [a], [a]
    tree.V[a - 1].cnt[flag]= 0
    seen[a-1] = True

    while len(temp) > 0:
        u = temp.pop(0)
        for v in tree.E[u]:
            if not seen[v-1]:
                tree.V[v - 1].cnt[flag] = tree.V[u-1].cnt[flag] + 1
                temp.append(v)
                seen[v-1] = True
                out.append(v)
    return out




n, m, d = map(int, input().split())
arr_m = list(map(int, input().split()))

tree = Tree(n)
for i in range(n - 1):
    x, y = map(int, input().split())
    tree.add_edge(x, y)

first_bfs = BFS(tree, arr_m[0])
# print(first_bfs)
first_bfs.reverse()
a = 0
for i in range(len(first_bfs)):
    if arr_m.__contains__(first_bfs[i]):
        a = first_bfs[i]
        break

second_bfs = BFS(tree, a)
second_bfs.reverse()
b = 0
for i in range(len(second_bfs)):
    if arr_m.__contains__((second_bfs[i])):
        b = second_bfs[i]
        break

BFS(tree, b, 1)

counter = 0
for v in tree.V:
    if v.cnt[0] <= d and v.cnt[1]<= d:
        counter += 1
        # print(v.index)
        # print(v.cnt)
        # print()


print(counter)


