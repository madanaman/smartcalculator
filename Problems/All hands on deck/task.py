ref_rank = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
total = 0
for i in range(0, 6):
    total = total + ref_rank.get(input())

print(total / 6)
