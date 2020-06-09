# from collections import deque
# queue = deque()
# queue.append(3)
# queue.append(2)
# queue.append(1)
# print(queue)
reversed_queue = deque()
while len(queue) > 0:
    reversed_queue.append(queue.pop())
#
# print(reversed_queue)