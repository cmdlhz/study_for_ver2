with open('files/write.txt', 'w') as write_file:
  write_file.write('Hello, nice to meet you!!')

with open('files/write.txt', 'a') as write_file:
  write_file.write('\nYooooooooooooooo')

quotes = [
  '\nLove like you\'ve have never loved before.',
  '\nLive like there is no tomorrow.'
]

with open('files/write.txt', 'a') as write_file:
  write_file.writelines(quotes)