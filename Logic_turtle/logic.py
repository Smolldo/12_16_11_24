# if - якщо, else - інакше, elif - додаткова умова (інакше якщо)  <<<<<< >>>>>>>

# if 2 > 4:
#     print('pravda')
# elif 7 < 9:
#     print("druha pravda")
# else:
#     print('ne pravda')


# age = 99

# if age < 18:
#     print('nepovnolitniy')
# elif age >= 18 and age < 65:
#     print('vi dorosli')
# else:
#     print('pensioner')


# bal = 50

# if bal >= 80:
#     print('ocinka A')
# elif bal >= 70:
#     print('ocinka B')
# elif bal >= 60:
#     print('ocinka C')
# else:
#     print('ne zdav')


# login = 'master1100'

# att = input("Enter login: ")

# if att == login:
#     print('welcome to acaunt')
# else:
#     print('try again')


import turtle

t = turtle.Turtle()
wn = turtle.Screen()

# direct = input('Введіть напрямок (вперед, назад, вліво, вправо): ')

# if direct == 'вперед':
#     t.forward(100)
# elif direct == 'назад':
#     t.backward(100)
# elif direct == 'вліво':
#     t.left(90)
#     t.forward(100)
# elif direct == 'вправо':
#     t.right(90)
#     t.forward(100)
# else:
#     print('Неправильне слово')


# dist = int(input('Введіть відстань: '))

# if dist < 100:
#     t.speed(1)
# elif dist >= 100 and dist < 200:
#     t.speed(5)
# else:
#     t.speed(10)

# t.forward(dist)




color = input('Введіть колір: ')

if color == 'red':
    t.color(color)
    t.forward(100)
elif color == 'yellow':
    t.color(color)
    t.backward(100)
elif color == 'green':
    t.color(color)
    t.forward(100)
elif color == 'purple':
    t.color(color)
    t.forward(100)
else:
    print('Неправильне слово')



wn.mainloop()