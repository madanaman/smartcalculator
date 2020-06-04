def func():
    nam, surn = input().split()
    return nam, surn


try:
    name, surname = func()
except ValueError:
    print("You need to enter exactly 2 words. Try again!")
else:
    print(f'Welcome to our party, {name} {surname}')
