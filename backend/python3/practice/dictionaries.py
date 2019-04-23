# cars = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(list(cars.keys()))

def ninja_intro(dict):
  for key, val in dict.items():
    print(f'I am {key} and I am a {val} belt.')

ninja_belts = {}

while True:
  ninja_name = input('Enter a ninja name: ')
  ninja_belt = input('Enter a belt\'s color: ')
  ninja_belts[ninja_name] = ninja_belt

  another = input('Add another? (y/n)')
  if another == 'y':
    continue
  else:
    break

ninja_intro(ninja_belts)