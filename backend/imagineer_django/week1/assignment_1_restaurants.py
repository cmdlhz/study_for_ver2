## 1) Make a user to enter a type of food among 'Korean', 'Chinese', and 'Japanese'.
## 2) Recommend a restuarant randomly.

import secrets

korean_food = ['Bibimbap', 'Kimbap', 'Galbi']
italian_food = ['Lasagne', 'Italian Pizza', 'Pasta e fagioli']
japanese_food = ['Sushi', 'Udon', 'Tempura']

while True:
  try:
    choice = input("What kinds of cuisines would you like to eat? (Enter 'Korean' or 'Italian' or 'Japanese') ")
  except NameError:
    print("Please enter 'Korean' or 'Italian' or 'Japanese': ") 
    continue
  else:
    break
   
if choice == 'Korean' or choice == 'korean':
    result = secrets.choice(korean_food)
elif choice == 'Italian' or choice == 'italian':
  result = secrets.choice(italian_food)
elif choice == 'Japanese' or choice == 'japanese':
  result = secrets.choice(japanese_food)
  
if result:
  print(f'I would like to recommend a {choice} food called "{result}". I hope you enjoy the food!')

# PROBLEM : How to continue the loop until a user enters a correct value?!

# What kinds of cuisines would you like to eat? (Enter 'Korean' or 'Italian' or 'Japanese') 
# Traceback (most recent call last):
#   File "assignment_1_restaurants.py", line 26, in <module>
#     if result:
# NameError: name 'result' is not defined

# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659#23294659