# create your dictionary here
objects_dict = {}
# objects = [{1: "dict", 2: "dict"}, (1, 2, 3), [1,2,3]]
for obj in objects:
    try:
        objects_dict[obj] = hash(obj)
    except TypeError:
        continue

# print(objects_dict)
