def password(number):
    result = []
    for i in range(1, number):
        for j in range(1,number):
            if number % (i+j) == 0 and i != j:
                num = str(i) + "|" + str(j)
                result.append(num)

    new_result = []
    for m in result:
        new_result.append(m.split("|"))

    for i_p in new_result:
        for j_p in new_result:
            if i_p == j_p:
                continue
            elif i_p == j_p[::-1]:

                new_result.remove(j_p)

    new_list = ""
    for i in new_result:
        new_list +=  ",".join(str(element) for element in i) + " | "


    return(new_list)

data = [x for x in range(3,21)]

for i in data:

    print(f'Для числа {i} подходит пароль: {password(i)}')

