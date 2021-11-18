class Geolicalization:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def get_distance(self, other_geo):
    x_diff = (self.x - other_geo.x) ** 2
    y_diff = (self.y - other_geo.y) ** 2
    return int((x_diff + y_diff) ** 0.5)

def main():
  geo_1 = Geolicalization(4, 11)
  geo_2 = Geolicalization(4, 8)

  print(geo_2.get_distance(other_geo = geo_1))
  print(isinstance(geo_1, Geolicalization))
  print(isinstance(geo_2, Geolicalization))

if __name__ == "__main__":
  main()
