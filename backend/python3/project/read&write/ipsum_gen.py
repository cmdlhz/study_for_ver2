## Random integer b/t the starting number and the ending number
from random import randint

colors = [
  ' 1 RED', '2 ORANGE', '3 YELLOW', '4 GREEN', '5 BLUE', '6 PURPLE', '7 BLACK',
  '8 GRAY', '9 BROWN', '10 CORAL', '11 GOLD', '12 SILVER', '13 LAVENDER', '14 LIME'
]

def colorize(word):
  random_pos = randint(0, len(colors)-1)
  return f'{word} || {colors[random_pos]}'

paragarphs = int(input('How many paragraphs of ninja ipsum? : '))

with open('files/ipsum.txt') as ipsum_original:
  items = ipsum_original.read().split()

  for n in range(paragarphs):
    color_text = list(map(colorize, items))
    with open('files/ipsum_colorize.txt', 'a') as ipsum_colorize:
      ipsum_colorize.write(' '.join(color_text) + '\n\n')