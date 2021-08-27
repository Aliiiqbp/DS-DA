def binary(arr, x, l, r):
    if l == r - 1:
        return l

    mid = (l + r) // 2
    if arr[mid] < x:
        return binary(arr, x, mid, r)
    else:
        return binary(arr, x, l, mid)


n, q = map(int, input().split())
l = [None] * n
r = [None] * n

for i in range(n):
    l[i], r[i] = map(int, input().split())

count_from_start = [r[0] - l[0] + 1]
for i in range(1, n):
    count_from_start.append(count_from_start[i - 1] + r[i] - l[i] + 1)

ans = []
for i in range(q):
    asked = int(input())
    index = binary(count_from_start, asked, 0, n)
    if asked > count_from_start[0]:
        print(l[index + 1] + asked - count_from_start[index] - 1)
    else:
        print(l[0] + asked - 1)
