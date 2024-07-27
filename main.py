

def password(number):
    result = []
    for i in range(1, number):
        for j in range(1,number):
            if number % (i+j) == 0 and i != j:
                num = str(i) + str(j)
                result.append(num)

    for i_p in result:
        for j_p in result:
            if i_p == j_p:
                continue
            elif i_p == j_p[::-1]:
                result.remove(j_p)

    return result

data = [x for x in range(3,21)]


for i in data:

    print(i, password(i))
