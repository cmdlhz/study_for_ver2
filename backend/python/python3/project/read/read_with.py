def sequence_filter(line):
  return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
  lines = dna_file.readlines()
  print(list(filter(sequence_filter, lines)))

## Don't need to close reading the file