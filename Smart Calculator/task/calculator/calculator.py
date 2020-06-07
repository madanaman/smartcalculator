import re


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


def add_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def parse_operator(operator):
    # Only minus sign contributes to changing sign at the moment
    if operator.count("-") % 2 == 0:
        return "+"
    return "-"


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


def do_calculation(in_array):
    # nums = [int(in_array[i]) for i in range(len(in_array)) if i % 2 == 0]
    # operators = [parse_operator(in_array[i]) for i in range(len(in_array)) if i % 2 != 0]
    nums = re.split(r"[-+]+", in_array.replace(" ", ""))
    if '' in nums:
        nums.remove('')
    # print(nums)
    operators = re.findall(r"[-+]+", in_array.replace(" ", ""))
    # print(operators)

    # total = int(nums[0])
    total = num_or_var(nums[0])
    # if len(nums) == 1 and in_array.index(operators[0]) == 0:
    # This code is to check for conditions pass: +11, -11. Fail 11+, 11-
    if len(nums) == 1 and len(operators) > 0 and in_array.index(operators[0]) == 0:
        if operators[0] == '-':
            return total * -1
        else:
            total
    elif len(nums) == 1 and len(operators) > 0 and in_array.index(operators[0]) != 0:
        raise Exception

    for i in range(1, len(nums)):
        if operators[i - 1] == "-":
            total = subtract_numbers(total, num_or_var(nums[i]))
        else:
            # print('in for loop else')
            total = add_numbers(total, num_or_var(nums[i]))
        # print("iteration:", i, nums[i], total)
    return total


def validate(expr):
    split_val = expr.replace(" ", "").split("=")
    if re.match(r"^[aA-zZ]+$", split_val[0]) is None:
        raise InvalidIdentifierException
    if re.match(r"^[aA-zZ]+", split_val[1]) is not None and re.search(r"[0-9]+", split_val[1]) is not None:
        raise InvalidAssignment
    if re.match(r"^[aA-zZ]+[ ]*=[ ]*[0-9aA-zZ]+[ ]*$", expr) is None:
        raise InvalidAssignment
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
    if re.match(r"^[aA-zZ]+", values) is not None and "=" in values:
        try:
            validate(values)
            continue
        except InvalidIdentifierException:
            print("Invalid identifier")
            continue
        except InvalidAssignment:
            print("Invalid assignment")
            continue
        except UnknownVariableException:
            print("Unknown variable")
            continue
    try:
        print(do_calculation(values))
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
        print("Unknown variable")
        continue
    except Exception:
        print("Invalid expression")
        continue
    # print(do_calculation(values))
print("Bye!")
