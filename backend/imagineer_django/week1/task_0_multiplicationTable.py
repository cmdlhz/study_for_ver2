level = int(input('Which multiplication table would you like to print? '))

if level > 0 and level < 10:
  for num in range(1,10):
    print(f'{level} * {num} = {level * num}')
else:
  print('Please enter a value b/t 1 and 9.')