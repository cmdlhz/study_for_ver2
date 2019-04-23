age = 10
num = 0

while num < age:
  if num == 0:
    num += 1
    continue
  if num % 2 == 0:
    print(num)
  if num > 4:
    break
  num += 1