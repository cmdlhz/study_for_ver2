level = input('Which multiplication table would you like to print? ')
for num in range(1,10):
  result = num * int(level)
  print(f'{level} * {num} = {result}')