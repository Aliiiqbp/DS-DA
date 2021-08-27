###################################################################################################

nq = input()

n = int(nq.split()[0])
q = int(nq.split()[1])

index = [0] * n

outputs = []
numbers = []

###################################################################################################

in_command = 0
out_command = [0] * n


for x in range(q):
    command = input().split()

    if command[0].__contains__("I"):
        if in_command != 0:
            numbers.append(int(command[1]) + numbers[in_command-1])
            in_command += 1
        else:
            numbers.append(int(command[1]))
            in_command += 1

    else:
        i, j = int(command[1]) - 1, int(command[2])
        index[i] += j

        if j != 0:
            if out_command[i] != 0:
                outputs.append(numbers[index[i] - 1] - numbers[index[i] - j - 1])
            elif out_command[i] == 0:
                outputs.append(numbers[index[i] - 1])
                out_command[i] = 1
        else:
            outputs.append(0)
###################################################################################################

for x in outputs:
    print(x)
