from collections import deque
my_queue = deque()
inp = int(input())
for i in range(0, inp):
    comm = input().split()
    if comm[0] == "ENQUEUE":
        my_queue.appendleft(comm[1])
    elif comm[0] == "DEQUEUE":
        my_queue.pop()

while len(my_queue) > 0:
    print(my_queue.pop())
