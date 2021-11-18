class Person:
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

  def go(self):
    print("Walking")


class Ciclista(Person):
  def __init__(self, name, age, email):
    super().__init__(name, age, email)

  def go(self):
    print("I am moving at my cicle")


def main():
  derke = Person("Derke", 19, "dereksamuelrg@gmail.com")
  derke.go()

  ciclista = Ciclista("Dasniel", 16, "dasnieles@gmail.com")
  ciclista.go()


if __name__ == "__main__":
  main()
