#Вам необходимо написать 3 функции:
#Функция count_calls подсчитывающая вызовы остальных функций.
#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
#Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

x = 0
def count_calls():
    global x
    x += 1


def string_info(my_string="string", my_tuple=()):
    count_calls()
    my_tuple = (len(my_string), my_string.upper(), my_string.lower())
    return my_tuple


def is_contains():
    count_calls()

