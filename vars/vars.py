name = 'John'
age = 25

#конкатенація
print('I am ', name, 'dfsdfsd') #виведення тексту і зміних через коми

print('My name is ' + name) # конкатенація (склеювання рядків)

# print('My name is ' + name + ' I am ' + age) - не можна конкатенувати числа і рядки. Можна тільки рядок до рядка

print(f'My name is {name}. I am {age}.')



# abs() - модуль числа

myAge = 25
frAge = 30

diff = abs(myAge - frAge)
print(diff)


n1 = 3
n2 = 45
n3 = 12

average = (n1 + n2 + n3) / 3
print(average)

# None - нічого, ніщо
#Числа (numeric type)
#Boolean - підтип цілих чисел
#Рядки

#числа - цілі(1, 2, 45, 987, 111) int() , дробові(2.5, 7.67) float(), комплексні(3j * 4) complex
#рядки str()
# True, False  bool()

a = 12

b = str(a) # перетворює тип даних до рядка
print(b)
print(type(b))

c = '23'
d = int(c) # перетворює все в цілі числа
print(d)


e = 'Ololo'
f = bool(e) # перетворює в булеве значення
print(f)



g = 'John'
# t = int(g)
# print(t)

l1 = [1,2,3,4,5]
l2 = str(l1)
print(l2)




# // - ділення націло
#   % - остача від ділення
# ** - піднесення до степеня

print(13 / 7)
print(13 // 7)


print(13 % 7)

print(18 % 7)


# 2 ** 3 = 2 * 2 * 2 = 8
# 3 ** 4 = 3 * 3 * 3 * 3 = 81
print(3 ** 4) 



#округлення

a = 13 / 7
print(a)
print(round(a))


import math

b = 13 / 7
c = math.ceil(b) #примусово округлює в більшу сторону
d = math.floor(b) # примусово округлює в меншу сторону

print(c)
print(d)


num1 = 6
num2 = 4
num = num1 + num2
print(num)
num = num1 - num2
print(num)
num = num1 * num2
print(num)

print(9**0.5)