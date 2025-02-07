a = 'sfsfsdfsfs'
b = str()

c = "sdfsdgfdgdfg"

d = 'Тарас Шевченко написав "Кобзар" '
e = "м'яч"
# sdfjsudkfsjdfhsu
'''   gdgdfg
dgdfg
dgdg
dgdg
dfgd'''

# print(a, c)

#КОНКАТЕНАЦІЯ - склеювання рядків.   +

name = 'John'
lastname = 'Marston'
age = 37

# print(name + ' ' + lastname)


# ІНТЕРПОЛЯЦІЯ РЯДКІВ - повторення рядка

# print('-' * 10)
n = ' '
size = 4
# print(f'({n * size}^{n * size}_{n * size}^{n * size})')


# МЕТОДИ РЯДКІВ

# lower() - робить всі букви малими. upper() - всі букви великі. title()- перша буква кожного слова велика. capitalize() - перша буква 1 слова велика

w = 'loreM ipSUM'

print(w.upper())
print(w.lower())
print(w.title())
print(w.capitalize())


# find()

h = 'hello world'

# print(h.find('world'))


# join() - з'єднує елементи в рядок за розподілювачем

words = ['Hello', 'world', 'Welcome', 'to', 'Python']
sent = ' '.join(words)
print(sent)

# split() - розділяє рядок на окремі елементи за розподілювачем
text = "Hello, world! Welcome to Python."
words = text.split()
# print(words)


# replace() - замінює вказані елементи на інші
text = "Hello, world!"
# print(text.replace('o', '!'))


# strip() - прибирає пробіли з початку і кінця рядка

r = ' hohoho '
# print(r)
# print(r.strip())



# СПИСКИ

arr = list()
arr1 = [1,2,3,4, 'sdfsf', True, [1,2,3]]

a = [1, 2, 3, 4, 5]
print(a[0])

#slice - зріз    products[start : end -1 : step]
products = ['eggs', 'coke', 'chips', 'cheese', 'grapes', 'lemon']
# print(products[0:3]) # від початку до 3 елемента
# print(products[:3]) # від початку до 3 елемента
# print(products[:]) # повертає весь список
# print(products[3:]) # від 3 елементу до кінця
# print(products[::2]) # від початку до кінця з кроком 2
# print(products[::-1]) # від початку до кінця обернене


# append() - додає елемент в кінецць списку
t = [1,2,3,4]
# t.append(5)
# print(t)

# insert() - вставити елемент на певну позицію(індекс)

t.insert(2, 'ololo')
# print(t)


# remove() - видаляє елемент зі списку, якщо елемента нема, видає помилку
t.remove(3)
# print(t)

# del 
del t[0]
# print(t)


# sort() - сортує список

i = [6,32,6,87,4,3,5,7]
i.sort()
# print(i)


# copy() - копіює список
x = [1,2,3]
y = x.copy()
# print(x == y)

# len() - довжина списку. кількість елементів в списку

print(len(x))

