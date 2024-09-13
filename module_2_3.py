my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = -1
while len(my_list) >= 0:
    index = index + 1
    if my_list[index] == 0:
        continue
    elif my_list[index] > 0:
         print(my_list[index])
    else: break
