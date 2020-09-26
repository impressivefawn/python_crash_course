# 5-1. Conditional Tests:
squares = [x**2 for x in range(1, 11)]
print('Is 49 in squares? I predict True')
print(49 in squares)

print('\nIs 5 greater than or equal to 10? I don\'t think so.')
print(5 >= 10)

numbers = list(range(1, 21))
# Evaluates to True
print(0 not in numbers)
# Evaluates to True
print(5 in numbers[:5])
# Evaluates to False
print(5 in numbers[1::2])


# 5-2. More Conditional Tests:

# Evaluates to False
print('London' == 'london')

# Evaluates to True
print('London'.lower() == 'london')

# Evaluates to True
print(5 == 5.0)

# Evaluates to False
print(5 == '5')

# Evaluates to True
age = 43
print(age >= 18 and age <= 65)

# Evaluates to True
evens = list(range(2, 101, 2))
print(42 in evens)

is_even = [(item, item % 2 == 0) for item in range(1, 21)]
print(is_even)