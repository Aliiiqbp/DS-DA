class Stack:
    def __init__(self, max_size):
        self.max_size = max_size  # Size of stack
        self.S = [0] * max_size  # Stack array
        self.num = 0  # Number of elements in Stack

    def push(self, item):
        if self.num >= self.max_size:
            raise Exception("Stack overflow")
        self.S[self.num] = item
        self.num += 1

    def pop(self):
        if self.num == 0:
            raise Exception("Stack empty")
        self.num -= 1
        return self.S[self.num]

    def top(self):
        if self.num == 0:
            raise Exception("Stack empty")
        return self.S[self.num - 1]

    def size(self):
        return self.num

    def is_full(self):
        return self.num >= self.max_size

    def is_empty(self):
        return self.num == 0

###################################################################################################
#input

n = int(input())
numbers = input().split(" ")

for i in range(n):
    numbers[i] = int(numbers[i])

s = Stack(n + 7)
xor_final = 0

for i in range(n):
    if s.is_empty() == False:

        ###############################
        temp = s.top() ^ numbers[i]
        if temp > xor_final:
            xor_final = temp
        ###############################


        if numbers[i] > s.top():
            s.push(numbers[i])

        elif numbers[i] < s.top():
            while numbers[i] < s.top() & s.is_empty() == False:
                s.pop()
                temp = s.top() ^ numbers[i]
                if temp > xor_final:
                    xor_final = temp
            s.push(numbers[i])

        else:
            continue

    else:
        s.push(numbers[i])


print(xor_final)
