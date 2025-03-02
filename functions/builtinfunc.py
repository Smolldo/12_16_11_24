# map

a = [1,2,3,4,5,6,7]

def square(x):
    return x * x

squared_numbers = list(map(square, a))

# print(squared_numbers)


# filter

even_numbers = list(filter(lambda x: x % 2 == 0, a))
# print(even_numbers)

# reduce
from functools import reduce

def add(x, y):
    return x + y

total = reduce(add, a)
# print(total)


# sorted

b = [6,3,9,1,2,8,6]

sort_nums = sorted(b)
# print(sort_nums)

# sum
suma = sum(b)
# print(suma)

# len
# print(len('gdfgdfghdfkujghdusifghsdfiugh'))

# min max
# print(min(b))
# print(max(b))

c = ['apple', 'cocunut', 'coconut']

# print(max(c))


# all

# True: заповнені рядки, колекції. True
# False: 0, '', [], {}, False, None

d = [1,2,3,4]
# print(all(d))

# any

# e = ['', False, None, 1]
# print(any(e))

grades = [99, 56, 23, 100]

passed = any(map(lambda x: x >= 100, grades))
# print(passed)


# enumerate

words = ['apple', 'banana', 'cherry']

# for i, w in enumerate(words):
#     print(i + 1, w)


# zip
names = ['Alice', 'Bob', 'Charlie', 'John']
ages = [25, 30, 35, 12, 45, 67]

combined = list(zip(names, ages))
# print(combined)

# Напишіть програму, яка приймає список чисел і знаходить найбільше та найменше значення. Використовуйте функції max та min.

def min_max(lst):
    maximum = max(lst)
    minimum = min(lst)
    return maximum, minimum

h = [1,2,3,4,5,6,7,8,9]

print(min_max(h))