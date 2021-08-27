n = int(input())
path = [0]

for i in range(n - 1):
    arr = list(map(int, input().split()))
    first_one = None

    for j in range(len(path)):
        if arr[path[j]] == 1:
            path = path[:j] + [i + 1] + path[j:]
            break
    else:
        path += [i + 1]

print(n)
for x in path:
    print(x + 1, end=" ")
