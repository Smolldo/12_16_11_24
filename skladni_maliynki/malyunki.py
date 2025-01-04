import turtle
t = turtle.Turtle()
wn = turtle.Screen()

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# for _ in range(2):
#     t.forward(100)
#     t.right(90)
#     t.forward(50)
#     t.right(90)
# t.speed(8)

# for i in range(180):
#     t.forward(2)
#     t.right(2)


# t.circle(200)

# t.speed(0)
# size = 40

# for i in range(-100, 100, size):
#     t.color('green')
#     for j in range(-100, 100, size):
#         t.up()
#         t.goto(i, j)
#         t.down()

#         if i % 60 == 0:
#             t.color('red')
#         if i % 50 == 0:
#             t.color('blue')

#         for _ in range(4):
#             t.forward(size)
#             t.right(90)


# t.shape('circle')
# t.color('red')
# for i in range(0, 360, 30):
#     t.setheading(i)
#     t.stamp()
#     t.forward(70)


t.shape('circle')
t.up()

colors = ['red', 'blue', 'green', 'yellow', 'purple']
t.speed(1)
for i in range(5):
    t.color(colors[i])
    t.goto(i * 20, 0)
    t.stamp()


wn.mainloop()