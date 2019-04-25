## Make Class Person : Name, Age, Gender
## Make a Colleague Class 
## : Use Class Person + add 
## : Position default: 'manager'

class Person:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

class Colleague(Person):
  def __init__(self, name, age, gender, position="manager"):
    super().__init__(name, age, gender)
    self.position = position

  def colleague_info(self):
    return f"{self.name} is {self.age} years old and a {self.gender}. {self.name}'s position is a {self.position}."

colleague1 = Colleague('Mark', 33, 'male')
colleague2 = Colleague('Jen', 35, 'female', 'director')
print(colleague1.colleague_info())
print(colleague2.colleague_info())