import turtle as t

turt = t.Turtle()

wn = t.Screen()

# turt.forward(100)

# turt.up()
# turt.goto(0, -50)
# turt.down()
# turt.forward(100)


# turt.forward(100)
# turt.left(90)
# turt.forward(50)
# turt.left(90)
# turt.forward(100)
# turt.left(90)
# turt.forward(50)
# turt.left(90)



turt.color('blue')
turt.write('Hello, world!', font=('Arial', 44, 'italic'))  #font - стиль шрифту  
turt.color('red')
turt.write('Hello, world!', font=('Colibri', 44, 'italic'))  #font - стиль шрифту 
turt.color('purple')
turt.write('Hello, world!', font=('Times New Roman', 44, 'italic'))  #font - стиль шрифту 

# user_text = wn.textinput('Enter text', 'Введіть будь-який текст')
# turt.write(user_text, font=('Arial', 44, 'italic'))


wn.mainloop()


# print('hello world 12232342345 &^*&%^&%&^* True')

a = 'hello'
b = "hello"
c = '''hello'''

# print(type(a), type(b) , type(c))

d = "сім'я"
# print(d)

f = '''
sdfsdf
sdfsdfsd

sdfsdf

'''
# print(f)


p = 'python'

# print(p[0])
# print(p[2])
# print(p[4])
# print(p[5])
# print(p[-1])

# #зрізи slice[start(початок зрізу) : end -1 (кінець зрізу -1) : step (крок)]

# print(p[0:3])
# print(p[2:])
# print(p[:3])
# print(p[::2])
# print(p[::-1])

# s = 'Hello! '
# print(s * 5)

#upper() - переводить текст у верхній регістр

txt = 'computer'
# print(txt.upper())

#lower() - переводить все у нижні регістр

txt1 = 'REDEMPTION'
# print(txt1.lower())

#title() - робить кожну першу букву слова великою

w = 'mouse, cat, dog'
# print(w.title())


#format()

name = 'John'
age = 23

output = 'hello my name is {0}. i am {1} years'.format(name, age)
print(output)