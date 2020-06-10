from collections import deque
import re

def plusorminus(expr):
    if expr.count("-") % 2 == 0:
        return "+"
    else:
        return "-"

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

def converToPostFix(infix):
    priority_dict = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
    stack = deque()
    nums = deque()
    infix = infix.replace(" ", "")
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
                operator = plusorminus(operator)
            # print("after", operator)
            # print(stack, operator, nums)
            while len(stack) > 0 and priority_dict[operator] <= priority_dict[stack[-1]]:
                operator1 = stack.pop()
                nums.append(operator1)
            stack.append(operator)
    while len(stack) > 0:
        nums.append(stack.pop())

    return nums


def num_or_var(var):
    if re.match(r"^[0-9]+$", var) is not None:
        return int(var)
    else:
        if re.match(r"^[aA-zZ]+$", var) is None:
            print("bad expression1")
        elif var in all_vars:
            return all_vars[var]
        else:
            print("bad expression2")


def evaluate_postfix(pfe):
    evaluation_stack = deque()
    print(pfe)
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
        return evaluation_stack.pop()




all_vars={"a": 10, "b": 20, "c": 30}


ip = "-10"
post_fix_expression = converToPostFix(ip)
print(post_fix_expression)
print(evaluate_postfix(post_fix_expression))
# print(num_or_var("a"))
# print(num_or_var("20"))