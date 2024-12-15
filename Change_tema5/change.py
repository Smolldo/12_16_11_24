import turtle as t

turt = t.Turtle()

wn = t.Screen()

turt.shape('arrow')  # shape - форма.   turtle, square, circle, triangle, arrow - стріла
turt.color('red')
turt.forward(100)
turt.right(144)

turt.shape('turtle')
turt.color('green')
turt.forward(100)
turt.right(144)

turt.shape('square')
turt.forward(100)
turt.right(144)

turt.shape('circle')
turt.forward(100)
turt.right(144)

turt.shape('triangle')
turt.forward(100)
turt.right(144)

file = r'D:\programming\PYTHON_JUN_12_16_11_24\Change_tema5\elder-scrolls-laat-dovahkiin-facing-dragon-oez8zkxn2wml74ok.gif'
wn.addshape(file)

turt.shape(file)
turt.forward(20)

turt.color('red', 'green')
turt.begin_fill()  # заливання фігури контуром

turt.forward(100)
turt.right(90)
turt.forward(100)
turt.right(90)
turt.forward(100)
turt.right(90)
turt.forward(100)
turt.right(90)

turt.end_fill()

turt.color('blue')
turt.circle(50)

turt.color('red')
turt.circle(60)

turt.color('yellow')
turt.circle(70)

turt.color('green')
turt.circle(80)

turt.speed(5)
turt.color('blue')
turt.circle(50)

turt.color('red')
turt.circle(60)

turt.color('yellow')
turt.circle(70)

turt.color('green')
turt.circle(80)

turt.pensize(100)
turt.forward(100)
turt.penup()
turt.goto(0, 200)
turt.pendown()
turt.right(90)
turt.forward(200)



wn.mainloop()