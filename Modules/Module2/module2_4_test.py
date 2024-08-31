numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in range(len(numbers)):
    print(f"i:{i}")
    if numbers[i] != 1:
        if (numbers[i] % i+1) == 0:
            prime.append(numbers[i])
        else:
            not_prime.append(numbers[i])
    else:
        prime.append(numbers[i])
print(prime)
print(not_prime)
