## Method 1
def sum_array(numbers):
  sum = 0
  for number in numbers:
    sum += number
  return sum

## Method 2
def sum_array2(numbers):
  return sum(numbers)