numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    flag = False

    for j in numbers:
        if i % j == 0 and i == j:
            flag = True
            break
        elif i % j == 0 and i != j and j != 1:
            break

    if flag:
        print("Число", i, "Простое")
        primes.append(i)
    else:
        print("Число", i, "Сложное")
        not_primes.append(i)


print(primes)
print(not_primes)
