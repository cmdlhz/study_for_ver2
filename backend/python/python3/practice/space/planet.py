class Planet:

  # Class level attributes
  shape = 'round'

  @classmethod
  def commons(cls):
    return f'All planets are {cls.shape} because of gravity.'

  @staticmethod
  def spin(speed = '2000 miles per hour'):
    return f'The planet spins and spins at {speed}.'

  # Instance level attributes
  def __init__(self, name, radius, gravity, system):
    self.name = name
    self.radius = radius
    self.gravity = gravity
    self.system = system

  def orbit(self):
    return f'{self.name} is orbiting in the {self.system}.'