# Card Duel:player vs computer
import random

ranks = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suites = ["Hearts","Clubs","Spades","Diamonds"]
value = {"Ace": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"10": 10,"Jack": 11,"Queen": 12,"King": 13}

player_suite = random.choice(suites)
computer_suite = random.choice(suites)

player_rank = random.choice(ranks)
print("You :",player_suite,"of",player_rank)

computer_rank = random.choice(ranks)
print("Computer :",computer_suite,"of",computer_rank)

player_value = value[player_rank]
computer_value = value[computer_rank]

if player_value < computer_value :
  print("Computer wins!")

elif player_value > computer_value :
  print("Player win!")

elif player_value == computer_value :
  print("It's a Tie!")

else :
  print("Invalid Input")
