# put your python code here
left = int(input())
right = int(input())
total = 0
ip_array = []

for i in range(left, right + 1):
    if i % 3 == 0:
        total = total + i
        ip_array.append(i)

print(total / len(ip_array))
