def recursive(arr1, arr2):
    if len(arr1) == 2:
        if arr1[0] > arr2[1]:
            return 1
        else:
            return 0
    if len(arr1) == 1:
        return 0

    mid = len(arr1) // 2
    return recursive(arr1[:mid + 1], arr2[:mid + 1]) + recursive(arr1[mid + 1:], arr2[mid + 1:]) + sorted_list(arr1[:mid + 1], arr2[mid + 1:])


def sorted_list(arr1, arr2):
    j, tmp = 0, 0
    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):
        tmp += j
        while j < len(arr2) and arr1[i] > arr2[j]:
            j += 1
            tmp += 1
    return tmp


n = int(input())
ages = list(map(int, input().split()))
tmp = [1] * (10 ** 5 + 7)
arr1, arr2 = [], []

for i in range(len(ages)):
    arr1.append(tmp[ages[i]])
    tmp[ages[i]] += 1

tmp = [1] * (10 ** 5 + 7)
ages.reverse()
for i in range(len(ages)):
    arr2.append(tmp[ages[i]])
    tmp[ages[i]] += 1
arr2.reverse()

print(recursive(arr1, arr2))
