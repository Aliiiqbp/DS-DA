def get_sub(r, graph):
    childs = graph[r]
    if len(childs) == 0:
        return [As[r], 0]

    OE = [float("-inf"), 0]
    for c in childs:
        newOE = [0,0]
        cOE = get_sub(c, graph)
        newOE[0] = max(cOE[0] + OE[1], cOE[1] + OE[0])
        newOE[1] = max(cOE[0] + OE[0], cOE[1] + OE[1])
        OE = newOE

    ans = [0, 0]
    ans[0] = max(As[r] + OE[1], OE[0])
    ans[1] = OE[1]
    return ans


n, As = int(input()), []
graph = [[] for i in range(n)]
line = list(map(int, input().split()))
As.append(line[1])

for i in range(1, n):
    line = list(map(int, input().split()))
    graph[line[0] - 1].append(i)
    As.append(line[1])

ans = get_sub(0, graph)
print(max(ans[0], ans[1]))
