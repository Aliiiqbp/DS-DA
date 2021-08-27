def fw(arr, des):
    n = len(arr)
    for k in range(n):
        if k not in des:
            for i in range(n):
                for j in range(n):
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


def fw_static(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])


n, q = map(int, input().split())
arr = [[] for j in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    arr[i] = line

des, cmd = [], []
for i in range(q):
    line = input().split()
    if len(line) == 2:
        cmd.append([int(line[1]) - 1])
        des.append(int(line[1]) - 1)
    else:
        cmd.append([int(line[1]) - 1, int(line[2]) - 1])

fw(arr, des)

ans = []
for i in range(q - 1, -1, -1):
    if len(cmd[i]) == 1:
        fw_static(arr, cmd[i][0])
    else:
        ans.append(arr[cmd[i][0]][cmd[i][1]])

for i in range(len(ans) - 1, -1, -1):
    print(ans[i])
