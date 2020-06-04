def tallest_people(**kwargs):
    max_keys = {}
    max_val = -999999999
    for key, value in kwargs.items():
        if value > max_val:
            max_val = value
            max_keys = {}
            max_keys[key] = value
        elif value == max_val:
            max_keys[key] = value
    for i in sorted(max_keys):
        print(i, ":", max_keys[i])


# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)