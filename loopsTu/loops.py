text = 'apple'

# for i in text:
#     print(i)


#range(start, end, step) - проміжок

# for i in range(1, 11):
#     print("Hello, World!")

# for i in range(1, 21, 2):
#     print(i)


# while умова:
    # print('aaa)

# benzin = 10

# while benzin:
#     print(f'mashina mae {benzin} litriv. vona ide')
#     benzin -= 1


# a = 0

# while a < 20:
#     print(a)
#     a+=1


# while True:
#     inp = input('Enter smth: ')

#     if inp == '0':
#         break


import turtle

t = turtle.Turtle()
wn = turtle.Screen()

# t.speed(1)

# for i in range(4):
#     t.forward(100)
#     t.right(90)

t.setco
while True:
    speed = input("Введіть швидкість черепашки (низька, середня, висока) або 'зупинити' для завершення: ")
    if speed.lower() == 'низька':
        t.speed(1)
    elif speed.lower() == 'середня':
        t.speed(5)
    elif speed.lower() == 'висока':
        t.speed(10)
    elif speed.lower() == 'зупинити':
        break
    else:
        print("Невідома команда")

    t.forward(100)
    t.right(90)


wn.mainloop()