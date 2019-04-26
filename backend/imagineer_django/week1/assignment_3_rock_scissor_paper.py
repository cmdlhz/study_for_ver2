## Ask a user to enter 'rock' or 'scissors' or 'paper'
## Computer will play against the user and the winner will be chosen
## When a player wins or loses three times in total, the game will be over.

import secrets
options = ['rock', 'scissors', 'paper']
win_count = 0
lose_count = 0

while (win_count < 3) and (lose_count < 3):
  user_input = input("Enter 'rock' or 'paper' or 'scissors' : ")
  computer_input = secrets.choice(options)

  if((user_input == 'rock' and computer_input == 'scissors') 
    or (user_input == 'scissors' and computer_input == 'paper') 
    or (user_input == 'paper' and computer_input =='rock')):
    win_count += 1
    print(f"YOU WON!!! You've won {win_count} time(s) and lost {lose_count} time(s).")
  elif user_input == computer_input:
    print('You drew!')
  elif user_input not in options:
    print("[ INCORRECT INPUT ] Please enter among 'rock', 'scissors', & 'paper'.")
  else:
    lose_count += 1 
    print(f"YOU LOST!!! You've won {win_count} time(s) and lost {lose_count} time(s).")    

if win_count == 3:
  print(f"[ GAME OVER ] YOU WON!!! You've won {win_count} time(s) and lost {lose_count} time(s).")
else:
  print(f"[ GAME OVER ] YOU LOST!!! You've won {win_count} time(s) and lost {lose_count} time(s).")  

# Show what a computer played each time and the progress.
# End the game when win or lose count is equal to "3" and Show the end result.