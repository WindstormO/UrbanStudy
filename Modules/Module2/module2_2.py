first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
print("Количество равных чисел: ")
if first == second and first == third:
    print(3)
elif first == second:
    print(2)
elif second == third:
    print(2)
else:
    print(0)
