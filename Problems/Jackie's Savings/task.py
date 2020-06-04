def final_deposit_amount(*interest, amount=1000):
    total = 1
    itr = 0
    for val in interest:
        if itr == 0:
            total = amount * ((val / 100) + 1)
        else:
            total = total * ((val / 100) + 1)
        itr += 1
        # print(total)

    return round(total, 2)


# print(final_deposit_amount(5, 7, 4))


