immutable_var = tuple([1, 2.0, "Строка", False])
print("Изначальный кортеж: ", immutable_var)
# immutable_var[0] = 2
# print("Кортеж после изменения 1 символа: ", immutable_var)
# Кортежи не поддерживают изменения входящих в них элементов
mutable_list = [1, 2, 3]
print("Изначальный список: ", mutable_list)
mutable_list = [4, 5, 6]
print("Измененный список: ", mutable_list)
