from collections import deque
no_of_recs = int(input())
commands_queue = deque()
students_queue = deque()

for i in range(0, no_of_recs):
    command = input()
    if command.startswith("READY"):
        students_queue.appendleft(command.split(" ")[1])
    elif command.startswith("EXTRA") or command.startswith("PASSED"):
        commands_queue.appendleft(command)

# print(students_queue)
# print(commands_queue)

while len(students_queue) > 0 and len(commands_queue) > 0:
    student = students_queue.pop()
    command = commands_queue.pop()
    if command == 'EXTRA':
        students_queue.appendleft(student)
    elif command == 'PASSED':
        print(student)
