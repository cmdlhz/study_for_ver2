from random import shuffle

def jumble(word):
  # 'blue' => 'b','l','u','e'
  anagram = list(word) 
  # Mix the order => 'l','u','b','e'
  shuffle(anagram)
  # join the letters => 'lube'
  return ''.join(anagram)

words = ['yellow', 'blue', 'green']

## for loop
anagrams = []
for word in words:
  anagrams.append(jumble(word))
print(anagrams)

## Comprehension way
print( [jumble(word) for word in words] )

## map(function, data)
print(list(map(jumble, words)))