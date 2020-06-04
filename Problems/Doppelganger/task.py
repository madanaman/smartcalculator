# the object_list has already been defined
# write your code here
# object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
obj_dict = {}
for obj in object_list:
    try:
        if hash(obj) not in obj_dict.keys():
            obj_dict[hash(obj)] = 1
        else:
            obj_dict[hash(obj)] += 1
    except TypeError:
        continue

total_cnt = 0
for h in obj_dict:
    if obj_dict[h] > 1:
        total_cnt += obj_dict[h]

print(total_cnt)
