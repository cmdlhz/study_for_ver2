geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

## Method 1
def goose_filter(birds):
  filtered_birds = []
  for bird in birds:
    if bird not in geese:
      filtered_birds.append(bird)
      
  return filtered_birds


## Method 2
def goose_filter2(birds):
  return [bird for bird in birds if bird not in geese]
