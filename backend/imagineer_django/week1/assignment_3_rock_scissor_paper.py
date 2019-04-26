## Ask a user to enter 'rock' or 'scissors' or 'paper'
## Computer will play against the user and the winner will be chosen
## When a player wins or loses three times in total, the game will be over.

import secrets
options = ['rock', 'scissors', 'paper']
win_count = 0
lose_count = 0

while (win_count < 3) or (lose_count < 3):
  if (win_count == 3) or (lose_count == 3):
    print(f"[ GAME OVER ] You've won {win_count} time(s) and lost {lose_count} time(s).")
  else:
    user_input = input("Enter 'rock' or 'paper' or 'scissors' : ")
    computer_input = secrets.choice(options)
    count()
    print(f"Computer played {computer_input}. You've won {win_count} time(s) and lost {lose_count} time(s).")    

def count():
  if (user_input == 'rock' and computer_input == 'scissors') or (user_input == 'scissors' and computer_input == 'paper') or (user_input == 'paper' and computer_input =='rock'):
    print('You won!')
    win_count = win_count + 1
  elif (user_input == 'rock' and computer_input == 'paper') or (user_input == 'scissors' and computer_input == 'rock') or (user_input == 'paper' and computer_input == 'scissors'):
    print('You lost!')
    lose_count += 1
  elif user_input == computer_input:
    print('You drew!')
    win_count = win_count
    lose_count = lose_count

# Show what a computer played each time and the progress.
# End the game when win or lose count is equal to "3" and Show the end result.