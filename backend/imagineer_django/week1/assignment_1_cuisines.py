## 1) Make a user to enter a type of food among 'Korean', 'Chinese', and 'Japanese'.
## 2) Recommend a restuarant randomly.

import secrets

# PROBLEM : How to continue the loop until a user enters a correct value?!

def recommend_cuisine():
  try:
    korean_food = ['Bibimbap', 'Kimbap', 'Galbi']
    italian_food = ['Lasagne', 'Italian Pizza', 'Pasta e fagioli']
    japanese_food = ['Sushi', 'Udon', 'Tempura']

    choice = input("What kinds of cuisines would you like to eat? (Enter 'Korean' or 'Italian' or 'Japanese') ")
      
    if choice == 'Korean' or choice == 'korean':
      result = secrets.choice(korean_food)
    elif choice == 'Italian' or choice == 'italian':
      result = secrets.choice(italian_food)
    elif choice == 'Japanese' or choice == 'japanese':
      result = secrets.choice(japanese_food)
      
    if result:
      print(f'I would like to recommend a {choice} food called "{result}". I hope you enjoy the food!')
  except:
    print("Please enter among 'Korean' or 'Italian' or 'Japanese' !!!!!")
    recommend_cuisine()

recommend_cuisine()

# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response/23294659#23294659