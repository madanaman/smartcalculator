# the list "walks" is already defined
# your code here
# walks = [
#     {"day": "Monday", "distance": 2000},
#     {"day": "Tuesday", "distance": 3000},
#     {"day": "Wednesday", "distance": 3500},
#     {"day": "Thursday", "distance": 2500},
#     {"day": "Friday", "distance": 2500},
#     {"day": "Saturday", "distance": 1000},
#     {"day": "Sunday", "distance": 5600}]

total = 0
for walk in walks:
    total = total + walk.get('distance', 0)

print(total // 7)