# EXERCISE 1
def greet(name='jen', time='morning'):
  print(f'Good {time}, {name}')

name = input('Enter your name: ')
time = input('Enter the time of the day: ')

greet(name="shaun")


# EXERCISE 2
def area(radius):
  return 3.142 * radius**2

def vol(area, length):
  print(area * length)

radius = int(input('Enter a radius: '))
length = int(input('Enter a length: '))

vol(area(radius), length)