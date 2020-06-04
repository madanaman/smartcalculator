# put your python code here
ip = input().lower().split(" ")
final_dict = {}
for i in ip:
    if final_dict.get(i) is None:
        final_dict[i] = 1
    else:
        final_dict[i] += 1

# print(final_dict)

for i, j in final_dict.items():
    print(i, j)
