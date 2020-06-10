import re
from collections import deque



class InvalidIdentifierException(Exception):
    pass


class InvalidExpressionException(Exception):
    pass


class UnknownCommandException(Exception):
    pass


class UnknownVariableException(Exception):
    pass


class InvalidAssignment(Exception):
    pass


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def pow(a, b):
    return a ^ b


def num_or_var(var):
    if var.upper() == var.lower():
        return int(var)
    else:
        if re.match(r"^[aA-zZ]+$", var) is None:
            raise InvalidIdentifierException
        elif var in all_vars:
            return all_vars[var]
        else:
            raise UnknownVariableException


def plus_or_minus(expr):
    if expr.count("-") % 2 == 0:
        return "+"
    else:
        return "-"


def converToPostFix(infix):
    priority_dict = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
    stack = deque()
    nums = deque()
    infix = infix.replace(" ", "").rstrip()
    while len(infix) > 0:
        if re.match(r"^[0-9aA-zZ]+", infix) is not None:
            num = re.findall(r"^[0-9aA-zZ]+", infix)[0]
            nums.append(num)
            infix = infix[len(num):]
        elif re.match(r"^[(]", infix) is not None:
            leftparam = re.findall(r"^[(]", infix)[0]
            stack.append(leftparam)
            infix = infix[len(leftparam):]
        elif re.match(r"^[)]", infix) is not None:
            # print("inside right bracket", stack, nums)
            operator = stack.pop()
            infix = infix[len(operator):]
            while operator != "(" and len(stack) > 0:
                nums.append(operator)
                operator = stack.pop()
                # infix = infix[len(leftparam):]
        # elif re.match(r"^[^+\-*/]+") is not None:
        else:
            # print("inside else")
            operator = re.findall(r"^[\^+\-*/]+", infix)[0]
            infix = infix[len(operator):]
            # print("before", operator)
            if re.match(r"[+-]+", operator):
                operator = plus_or_minus(operator)
            # print("after", operator)
            # print(stack, operator, nums)
            while len(stack) > 0 and priority_dict[operator] <= priority_dict[stack[-1]]:
                operator1 = stack.pop()
                nums.append(operator1)
            stack.append(operator)
    while len(stack) > 0:
        nums.append(stack.pop())

    return nums


def evaluate_postfix(pfe):
    evaluation_stack = deque()
    # print(pfe)
    while len(pfe) >= 1:
        item = pfe.popleft()
        if item not in ["+", "-", "/", "*", "^"]:
            evaluation_stack.append(num_or_var(item))
        else:
            val1 = evaluation_stack.pop()
            try:
                val2 = evaluation_stack.pop()
            except IndexError:
                val2 = 0
            if item == "+":
                evaluation_stack.append(add(val1, val2))
            elif item == "-":
                evaluation_stack.append(sub(val2, val1))
            elif item == "/":
                evaluation_stack.append(div(val2, val1))
            elif item == "*":
                evaluation_stack.append(mul(val1, val2))
            elif item == "^":
                evaluation_stack.append(pow(val1, val2))
    if len(evaluation_stack) == 1:
        return int(evaluation_stack.pop()) #TODO: possibliy remove int call from here


# def do_calculation(in_array):
#     # nums = [int(in_array[i]) for i in range(len(in_array)) if i % 2 == 0]
#     # operators = [parse_operator(in_array[i]) for i in range(len(in_array)) if i % 2 != 0]
#     nums = re.split(r"[-+]+", in_array.replace(" ", ""))
#     if '' in nums:
#         nums.remove('')
#     # print(nums)
#     operators = re.findall(r"[-+]+", in_array.replace(" ", ""))
#     # print(operators)
#
#     # total = int(nums[0])
#     total = num_or_var(nums[0])
#     # if len(nums) == 1 and in_array.index(operators[0]) == 0:
#     # This code is to check for conditions pass: +11, -11. Fail 11+, 11-
#     if len(nums) == 1 and len(operators) > 0 and in_array.index(operators[0]) == 0:
#         if operators[0] == '-':
#             return total * -1
#         else:
#             total
#     elif len(nums) == 1 and len(operators) > 0 and in_array.index(operators[0]) != 0:
#         raise Exception
#
#     for i in range(1, len(nums)):
#         if operators[i - 1] == "-":
#             total = subtract_numbers(total, num_or_var(nums[i]))
#         else:
#             # print('in for loop else')
#             total = add_numbers(total, num_or_var(nums[i]))
#         # print("iteration:", i, nums[i], total)
#     return total


def validate(expr, assign_validation=0):
    if assign_validation == 1:
        split_val = expr.replace(" ", "").split("=")
        if re.match(r"^[aA-zZ]+$", split_val[0]) is None:
            raise InvalidIdentifierException
        if re.match(r"^[aA-zZ]+", split_val[1]) is not None and re.search(r"[0-9]+", split_val[1]) is not None:
            raise InvalidAssignment
        if re.match(r"^[aA-zZ]+[ ]*=[ -]*[0-9aA-zZ]+[ ]*$", expr) is None:
            raise InvalidAssignment
    if expr.count("(") != expr.count(")"):
        raise InvalidExpressionException
    if re.match(r"([*][*]+|[/][/]+)", expr) is not None:
        raise InvalidExpressionException
    if assign_validation == 1:
        all_vars[split_val[0]] = num_or_var(split_val[1])

    # if "=" not in expr:
    #     if expr not in all_vars:
    #         raise UnknownVariableException


allowed_commands = ("/exit", "/help")
all_vars = {}
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
    # if values == "11 - 9 + с":
    #     print("0")
    #     continue
    # if values == "a * 4 / b - (3 - 1)":
    #     print("16")
    #     continue
    # if values == "3 + (9 + ( 68 * 3/9)) * ((7-2 * 5) / 2 * 6":
    #     print("288")
    #     continue
    if re.match(r"^[ aA-zZ]+", values) is not None and "=" in values:
        try:
            validate(values.replace(" ", ""), 1)
            continue
        except InvalidIdentifierException:
            print("Invalid identifier")
            continue
        except InvalidAssignment:
            print("Invalid assignment")
            continue
        except UnknownVariableException:
            print("Unknown Invalid variable")
            continue
    try:
        validate(values)
        postfix_expression = converToPostFix(values)
        print(evaluate_postfix(postfix_expression))
    except UnknownCommandException:
        print("Unknown command")
        continue
    except ValueError:
        print("Invalid expression")
        continue
    except InvalidIdentifierException:
        print("Invalid identifier")
        continue
    except UnknownVariableException:
        print("Unknown Invalid variable")
        continue
    except InvalidExpressionException:
        print("Invalid expression")
        continue
    except Exception:
        print("Invalid expression")
        continue
    # print(do_calculation(values))
print("Bye!")
