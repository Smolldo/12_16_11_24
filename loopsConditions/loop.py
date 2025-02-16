a = 7
b = 9

if a > b:
    print('a > b')



age = 75

# if age < 18:
#     print('nepovnolitniy')
# elif age >= 65:
#     print('pensioner')
# else:
#     print('dorosliy')




# and or not

prava = True
vik = 19

if vik >= 18 and prava:
    print('mozhna')
else:
    print('ne mozhna')



d1 = 'Monday'

if d1 == 'Saturday' or d1 == 'Sunday':
    print('weekend')
else:
    print('weekday')


is_raining = False

if not is_raining:
    print('sonyachna pohoda')



t = 'Hello'

for i in t:
    print(i)



# range(start, end, step)

for i in range(10):
    print('hello world')


l1 = []

for i in range(0, 11, 2):
    l1.append(i)
else:
    print('done')

# print(l1)


words = ["hello", "world", "test", "python", "example"]

for i in words:
    if i == 'test':
        print('znaideno')


a = 0

while a < 5:
    print('hello')
    a+=1


# break continue

l1 = [1,2,3,4,5,6,7,8,9]

for i in l1:
    print(i)
    if i == 5:
        break
else:
    print('done')




# while True:
#     inp = input('Enter SMTH: ')
#     if inp == '0':
#         break
#     else:
#         print(inp)


words = ["hello", "world", "test", "python", "example"]
w = []

for i in words:
    if len(i) < 5:
        continue
    else:
        w.append(i)

print(w)