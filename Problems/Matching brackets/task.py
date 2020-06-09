# put your python code here
from collections import deque
data = input()
my_stack = deque()
for i in data:
    if i == "(":
        my_stack.append(i)
    elif i == ")":
        try:
            my_stack.pop()
        except IndexError:
            print("ERROR")
            exit()
if len(my_stack) == 0:
    print("OK")
else:
    print("ERROR")
