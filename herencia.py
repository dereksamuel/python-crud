class Rectangle:
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return self.base * self.height


class Square(Rectangle):
  def __init__(self, side = 0):
    super().__init__(side, side) # Reference of other class


def main():
  rectangle = Rectangle(base = 3, height = 4)
  print(rectangle.area())

  square = Square(side = 5)
  print(square.area())

if __name__ == "__main__":
  main()
