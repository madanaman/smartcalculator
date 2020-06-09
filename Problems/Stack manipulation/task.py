from collections import deque
inp = int(input())
my_stack = deque()
for i in range(0, inp):
    command = input().split()
    if command[0] == "PUSH":
        my_stack.append(command[1])
    elif command[0] == "POP":
        my_stack.pop()
    else:
        print("Invalid Command")
        continue

while len(my_stack) > 0:
    print(my_stack.pop())
