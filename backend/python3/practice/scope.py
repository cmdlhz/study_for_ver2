my_name = 'scott'

def print_name():
  global my_name
  my_name = 'jen'
  print('Name inside of the function is', my_name)

print_name()
print('Name outside of the function is', my_name)