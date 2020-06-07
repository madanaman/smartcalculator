import string
import re


def startswith_capital_counter(names):
    counter = 0
    for name in names:
        # ...
        counter += 1 if re.search(r"^[A-Z]+", name) is not None else 0
    return counter

#
# names = ['Aman', 'Preeti', "yash", "usha", "divya"]
# startswith_capital_counter(names)
