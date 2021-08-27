###################################################################################################

nk = input()

n = int(nk.split()[0])
k = int(nk.split()[1])

arr_a = input().split()
arr_b = input().split()

a = [0] * (n+1)
b = [0] * (n+1)

for i in range(n):
    a[i] = int(arr_a[i])
    b[i] = int(arr_b[i])

sub = [0] * (n+1)

for i in range(n):
    sub[i] = (a[i] > b[i])*(a[i] - b[i]) + (b[i] >= a[i])*(b[i] - a[i])

###################################################################################################

Max = max(sub)
arr_sub = [0] * (Max + 1)

for x in sub:
    arr_sub[x] += 1


while k > 0:

    if arr_sub.__len__() == 1:
        break

    arr_sub[arr_sub.__len__() - 1] -= 1
    arr_sub[arr_sub.__len__() - 2] += 1
    k -= 1

    if arr_sub[arr_sub.__len__() - 1] == 0:
        del arr_sub[arr_sub.__len__() - 1]

##################################################################################################

answer = 0

if k == 0:
    for i in range(arr_sub.__len__()):
        answer += (i * i) * arr_sub[i]
elif k % 2 == 0:
    answer = 0
else:
    answer = 1

answer = answer % ((10 ** 9) + 7)

print(answer)
