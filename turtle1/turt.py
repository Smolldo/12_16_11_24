import turtle as t  #імпорт пакета turtle

turt = t.Turtle() # створення екземпляру класу

wn = t.Screen()  # створення вікна / полотна

wn.title('Ростислав')  # title - заголовок. дає ім'я нашому полотну

wn.bgcolor('White') # bgcolor (background color) - колір заднього фону

wn.setup(width=700, height=700) # ширина / висота в пікселях


turt.forward(100)  # черепаха йде вперед

turt.left(90)  # left - поворот вліво на 90 градусів. right - поворот праворуч на ... градусів

turt.forward(100)

turt.right(120)

turt.forward(40)

turt.up()  # up - вгору. відриває ручку від полотна  penup()
turt.forward(100)

turt.down()  # down вниз - опускає ручку на полотно pendown()
turt.forward(100)

turt.reset() # очищує полотно і повертає черепаху на початок координат

# turt.clear() # очищує полотно НЕ повертає черепаху на початок


turt.goto(200, 200) # переміщує в задану точку на полотні  goto(x , y)

turt.backward(500) 










wn.mainloop() # нескінченна робота полотна