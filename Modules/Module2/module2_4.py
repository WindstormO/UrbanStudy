numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []

# Проход цикла по всем элементам списка
for num in range(len(numbers)):
    is_prime = True
    # Проверка на равенство числа единице
    if (numbers[num]) == 1:
        continue
    # Если число не равно 1, нужно проверить, на какие числа оно будет делиться, начиная с 2 и до самого себя
    else:
        for i in range(2, num):
            # Если число делится на что-то без остатка, то оно составное
            if (numbers[num] % i) == 0:
                is_prime = False
                break
    if is_prime:
        prime.append(numbers[num])
    else:
        not_prime.append(numbers[num])


print(f"Простые числа: {prime}")
print(f"Составные числа: {not_prime}")
