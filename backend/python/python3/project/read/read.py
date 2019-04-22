ipsum_file = open('files/ipsum.txt')

for line in ipsum_file:
  print(line)
  ## Get rid of line breaks
  print(line.rstrip())

## Restart from [n]th character.
ipsum_file.seek(0)
## Store each line as an element in a list (including '\n')
lines = ipsum_file.readlines()
print(lines)

ipsum_file.seek(50)
## Read 100 chracters from the starting point.
file_text = ipsum_file.read(100)
print(file_text)

## Must close reading the file
ipsum_file.close()