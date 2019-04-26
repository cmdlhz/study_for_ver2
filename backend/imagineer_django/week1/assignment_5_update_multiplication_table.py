# When the entered value is not an integer, show "Please enter an integer between 1 and 9" message and restart the loop.

level = int(input('Which multiplication table would you like to print? '))

while type(level) is int:
  try:
    if level > 0 and level < 10:
      for num in range(1,10):
        print(f'{level} * {num} = {level * num}')
  except ValueError:
    print('Please enter an integer b/t 1 and 9.')
    continue
  else:
    break