from turtle import Turtle, Screen, window_height, window_width

window = Screen()
window.bgcolor("black")
grass_counter = -15

width = -window_width()
height = window_height()

turtle = Turtle()
square = Turtle()

turtle.penup()
turtle.color("red")
turtle.position()
turtle.speed(0)

square.position()
square.setx(-5)

for i in range(1, height):
  module_result = i % 6
  if (module_result == 0):
    turtle.color("gray")
    turtle.speed(0.5)
    turtle.setx(-window_width() / 2)
    turtle.setx(window_width() / 2)
    turtle.sety((height / 2) - i)
    turtle.pendown()

# for i in range(1, height):
#   module_result = i % 6
#   if (module_result == 0):
#     turtle.color("gray")
#     turtle.speed(0.5)
#     turtle.sety(-window_height() / 2)
#     turtle.sety(window_height() / 2)
#     turtle.setx((height / 2) - i)
#     turtle.pendown()

turtle.penup()

turtle.goto(0, 0)
turtle.circle(5)

turtle.pendown()
turtle.color("white")
square.color("white");

for i in range(1, 12):
  module_result = i % 2
  if module_result == 0:
    turtle.speed(0.5)
    for i_two in range(1, i):
      turtle.circle(i_two * (i + 2))
  else:
    turtle.speed(0.5)
    turtle.circle(10 * i)

for i in range(0, 4):
  square.forward(10)
  square.right(90)

square.sety(5)
square.sety(-5)
square.setx(-5)

for i in range(0, 11):
  module_result = i % 2
  if (module_result == 0):
    square.sety(-5)
    square.sety(5)
    square.setx(i - 5)

turtle.penup()
turtle.sety(-height / 2)
turtle.sety((-height / 2) + 200)

for i in range(1, 100):
  grass_counter = i
  turtle.setx((width / 2) + i)
  turtle.pendown()
  turtle.speed(0.5)
  turtle.sety((-height / 2))
  turtle.sety((-height / 2) + (i + 200))

turtle.penup()

for i in range(1, 100):
  turtle.setx((width / 2) + i + 99)
  turtle.pendown()
  turtle.speed(0.5)
  turtle.sety((-height / 2))
  turtle.sety((-height / 2) + i)

turtle.penup()
turtle.setx((width / 2) + 251)

for i in range(1, 200):
  turtle.setx((width / 2) + i + 250)
  turtle.pendown()
  turtle.speed(0.5)
  turtle.sety((-height / 2))
  turtle.sety((-height / 2) + 200)

turtle.penup()
turtle.setx((width / 2) + 301)

for i in range(1, 100):
  grass_counter = i
  turtle.setx((width / 2) + i + 300)
  turtle.pendown()
  turtle.speed(0.5)
  turtle.sety((-height / 2))
  turtle.sety((-height / 2) + (i + 200))

turtle.penup()
turtle.setx((-width / 2) - 30)

for i in range(1, 100):
  grass_counter = i
  turtle.setx((-width / 2) - i - 30)
  turtle.pendown()
  turtle.speed(0.5)
  turtle.sety((-height / 2))
  turtle.sety((-height / 2) + (i + 200))

window.mainloop()
