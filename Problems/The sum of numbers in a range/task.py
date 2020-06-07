def range_sum(numbers, a, b):
    counter = 0
    for num in numbers:
        if int(num) in range(int(a), int(b)+1):
            counter += int(num)
    return counter


numbers = input().split()
a = input().split()
print(range_sum(numbers, a[0], a[1]))