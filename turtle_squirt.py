from turtle import Turtle, Screen, window_height, window_width

window = Screen()
grass_counter = 0

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

turtle.penup()

turtle.goto(0, 0)
turtle.circle(5)

turtle.pendown()

for i in range(1, 12):
  module_result = i % 2
  if module_result == 0:
    turtle.color("black")
    circle = turtle.clone()
    circle.speed(0.5)
    for i_two in range(1, i):
      turtle.color("purple")
      circle.circle(i_two * (i + 2))
  else:
    circle = turtle.clone()
    circle.speed(0.5)
    circle.circle(10 * i)

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

# for i in range(1, 100):
#   grass_counter += i;
#   if (grass_counter >= 10):
#     grass_counter = 0
#   turtle.pendown()
#   module_result = i % 6
#   turtle.color("black")
#   turtle.speed(0.5)
#   turtle.setx(i)
#   turtle.sety((-height / 2) - grass_counter)
#   turtle.sety((-height / 2) + grass_counter)

window.mainloop()
