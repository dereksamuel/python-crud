class Washer:
  def __init__(self) -> None:
    pass

  def wash(self, temperature = 0):
    self._full_water_tank(temperature)
    self._add_jabon()
    self._wash()
    self._cetrifugar()

  def _full_water_tank(self, temperature):
    print(f"Fulling the water TANK... with the temperature: {temperature}")

  def _add_jabon(self):
    print("Adding jabon")

  def _wash(self):
    print("Washing the clothes")

  def _cetrifugar(self):
    print("Centrifugando the clothes")

if __name__ == "__main__":
  wash = Washer()
  wash.wash(15)