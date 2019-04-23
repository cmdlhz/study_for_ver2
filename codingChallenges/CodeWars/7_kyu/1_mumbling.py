def accum(str):
  return '-'.join(
    letter.upper() 
    + letter.lower() * index 
    for index, letter in enumerate(str)
  )