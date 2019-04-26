# When the entered value is not an integer, show "Please enter an integer between 1 and 9" message and restart the loop.

def multiplication_table():
  try:
    level = int(input('Which multiplication table would you like to print? '))
    if level > 1 and level < 10:
      for num in range(1, 10):
        print(f'{level} * {num} = {level * num}')
    else:
      print('Please enter an integer b/t 1 and 9 !!!!!')
      multiplication_table()
  except ValueError:
    print('Please enter an integer only !!!!!')
    multiplication_table()

multiplication_table()