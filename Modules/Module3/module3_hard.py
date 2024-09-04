def calculate_structure_sum(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, set):
            total_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, tuple):
            total_sum += calculate_structure_sum(*arg)
        elif isinstance(arg, list):
            total_sum += int(temp)
        elif isinstance(arg, dict):
            total_sum += calculate_structure_sum(*arg.items())
        elif isinstance(arg, str):
            total_sum += len(arg)
        elif isinstance(arg, float):
            total_sum += arg
        elif isinstance(arg, int):
            total_sum += arg
        elif isinstance(arg, none):
            pass
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
