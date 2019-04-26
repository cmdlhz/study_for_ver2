# Make the following by using a for loop.
# 00100
# 01110
# 11111
# 01110
# 00100

# https://stackoverflow.com/questions/39548099/printing-simple-diamond-pattern-in-python

# i = 1 | new i = 1 - 3 = -2 | *: 5 - 4 = 1 | 00 + * + 00
# i = 2 | new i = 2 - 3 = -1 | *: 5 - 2 = 3 | 0 + *** + 0
# i = 3 | new i = 3 - 3 = 0  | *: 5 - 0 = 5 |    *****
# i = 4 | new i = 4 - 3 = 1  | *: 5 - 2 = 3 | 0 + *** + 0
# i = 5 | new i = 5 - 3 = 2  | *: 5 - 4 = 1 | 00 + * + 00

num = int(input('How many lines would you like to have?: '))

for i in range(1, num + 1):
  i = i - (num//2 + 1)
  if i < 0:
    i = -i
  print(" " * i + "*" * (num - i * 2) + " " * i)