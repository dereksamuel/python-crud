class Car:
  def __init__(self, model: str, mark: str, color: str) -> None:
    self._state : str = "Sleeping, zzz..."
    self._motor : None = None
    self.domain_name : str = ""
    self.model : str = model
    self.color : str = color
    self.mark : str = mark

  def acelerate(self, size: float = 0.0):
    if size >= 20:
      self._motor.reduce_gasolyn(15)
    else:
      self._motor.reduce_gasolyn(1)
    self._state = "In movement"

  def inyect_gasolyn(self, size: float = 0):
    self._motor.set_gasolyn(size)


class Motor:
  def __init__(self, type_motor: str ="gasolina") -> None:
    self._temperature: float = 0.0
    self.type: str = type_motor
    self.gasolyn: float = 0.0

  def set_gasolyn(self, size: float):
    self.gasolyn += size
    return f"Ok the gasolyn total is: {self.gasolyn} latter plus {size}"

  def reduce_gasolyn(self, size: float):
    if (self.gasolyn != 0):
      self.gasolyn -= size

    return f"Ok the gasolyn total is: {self.gasolyn} latter minus {size}"
