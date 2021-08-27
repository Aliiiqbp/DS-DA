###################################################################################################
#Stack
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

walls = input().split(" ")

for i in range(n):

    walls[i] = int(walls[i]) % 2

###################################################################################################
#Stack :)
s = Stack(1000000)

for i in range(n):

    if s.is_empty() == False:
        if walls[i] == s.top():
            s.pop()
        else:
            s.push(walls[i])
    else:
        s.push(walls[i])

###################################################################################################
#OutPut

if s.size() > 1:
    print("NO")
else:
    print("YES")
