grades = ['A', 'B', 'C', 'F', 'F', 'A']

## filter(funtion, iterable)
def remove_fails(grade):
  return grade != 'F'
print(list(filter(remove_fails, grades)))

## for loop
filtered_grades = []
for grade in grades:
  if grade != 'F':
    filtered_grades.append(grade)
print(filtered_grades)

## Comprehension way
print( [grade for grade in grades if grade != 'F'] )