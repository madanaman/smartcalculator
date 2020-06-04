import re


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def parse_operator(operator):
    # Only minus sign contributes to changing sign at the moment
    if operator.count("-") % 2 == 0:
        return "+"
    return "-"


def do_calculation(in_array):
    # nums = [int(in_array[i]) for i in range(len(in_array)) if i % 2 == 0]
    # operators = [parse_operator(in_array[i]) for i in range(len(in_array)) if i % 2 != 0]
    nums = re.split(r"[-+]+", in_array.replace(" ", ""))
    if '' in nums:
        nums.remove('')
    # print(nums)
    operators = re.findall(r"[-+]+", in_array.replace(" ", ""))
    # print(operators)

    total = int(nums[0])
    if len(nums) == 1 and in_array.index(operators[0]) == 0:
        if operators[0] == '-':
            return total * -1
        else:
            total
    elif len(nums) == 1:
        raise Exception

    for i in range(1, len(nums)):
        if operators[i - 1] == "-":
            total = subtract_numbers(total, int(nums[i]))
        else:
            # print('in for loop else')
            total = add_numbers(total, int(nums[i]))
        # print("iteration:", i, nums[i], total)
    return total


allowed_commands = ("/exit", "/help")
while True:
    values = input()
    # print("values=", values)
    if values not in allowed_commands and values.startswith("/"):
        print("Unknown command")
        continue
    if len(values) == 0:
        continue
    if values == "/exit":
        break
    if values == "/help":
        print("The program calculates the sum of numbers")
        continue
    try:
        print(do_calculation(values))
    except Exception:
        print("Invalid expression")
    # print(do_calculation(values))
print("Bye!")
