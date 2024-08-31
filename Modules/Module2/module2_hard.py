def get_pass():
    n = int(input("Введите число от 3 до 20 "))
    print("Вы ввели число: ", n)
    if (n >= 3) and (n <= 20):
        result = []
        for i in range(1, n):
            for j in range(1, i):
                if j + i == n:
                    result.append(i)
                    result.append(j)
                    return result
    else:
        return f"Вы ввели число {n}. Оно не укладывается в диапазон от 3 до 20"


print(get_pass())
