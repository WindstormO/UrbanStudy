def calculate_structure_sum(*args):
    total_sum = 0
    for arg in args:
        for item in arg:
            print(item)
            if isinstance(item, set):
                print("МНОЖЕСТВО")
            elif isinstance(item, tuple):
                print("КОРТЕЖ")
            elif isinstance(item, dict):
                print("СЛОВАРЬ")
            elif isinstance(item, list):
                for element in item:
                    total_sum += element
            elif isinstance(item, str):
                total_sum += len(item)
            elif isinstance(item, int, float):
                print("ЦЕЛОЕ ЧИСЛО")
                total_sum += item
    return total_sum


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
