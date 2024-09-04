def calculate_structure_sum(data_structure):
    sum = 0
    for item in range(len(data_structure)):
        print(type(data_structure[item]))
        if isinstance(data_structure[item], int):
            sum = sum + data_structure[item]
        elif isinstance(data_structure[item], float):
            sum = sum + data_structure[item]
        elif isinstance(data_structure[item], str):
            #for symbol in (data_structure[item]):
            #не понятно, что делать с текстовыми строками
            print("СТРОКА")
        elif isinstance(data_structure[item], list):
            for list_item in range(len(data_structure[item])):
                sum = sum + data_structure[item][list_item]
            print("СПИСОК")
        elif isinstance(data_structure[item], dict):
            for dict_item in data_structure[item]:
                sum = sum+data_structure[item][dict_item]
            print("СЛОВАРЬ")
        elif isinstance(data_structure[item], tuple):
            print("КОРТЕЖ")
    return sum


#входные данные
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

#на выходе должны получить 99
result = calculate_structure_sum(data_structure)
print(result)
