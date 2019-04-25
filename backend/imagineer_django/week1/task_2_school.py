class School:

  def __init__(self, name, year, address):
    self.name = name
    self.year = year
    self.address = address

  def sentence(self):
    return f"{self.name} University was established in {self.year}. It's located in {self.address}."

school1 = School('Seoul', '1950', 'Seoul, Korea')
school2 = School('Korea', '1970', 'Incheon, Korea')
school3 = School('Busan', '1966', 'Busan, Korea')

print(school1.sentence())
print(school2.sentence())
print(school3.sentence())