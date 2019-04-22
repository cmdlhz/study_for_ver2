def belt_count(dict):
  belts = list(dict.values())
  for belt in set(belts):
    num = belts.count(belt)
    print(f'There are {num} {belt} belts.')

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

belt_count(ninja_belts)