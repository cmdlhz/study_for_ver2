# Make the following by using a for loop.
# 00100
# 01110
# 11111
# 01110
# 00100

n = 5

for a1 in range(1, (n+1)//2 + 1): #from row 1 to 5
  for a2 in range((n+1)//2 - a1):
    print("0", end = "")
  for a3 in range((a1*2)-1):
    print("1", end = "")
  print()

for a1 in range((n+1)//2 + 1, n + 1): #from row 6 to 9
  for a2 in range(a1 - (n+1)//2):
    print("0", end = "")
  for a3 in range((n+1 - a1)*2 - 1):
    print("1", end = "")
  print()

# https://stackoverflow.com/questions/39548099/printing-simple-diamond-pattern-in-python