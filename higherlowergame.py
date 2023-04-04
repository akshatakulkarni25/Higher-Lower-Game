from art import logo
from art import vs
import random
from game_data import data
import os
play_game=True

while (play_game):
  print(logo)
  randomA=random.choice(data)
  randomB=random.choice(data)
  while randomB == randomA:
    randomB=random.choice(data)
  game_over=False
  current_score=0
  while not game_over:
    print(f"Compare A: {randomA['name']}, a {randomA['description']}, from {randomA['country']}")
    print(vs)
    print(f"Agaist B: {randomB['name']}, a {randomB['description']}, from {randomB['country']}")
    user_ans=input("\nWho has more followers.Type 'A' or 'B'\n").lower()
    if (randomA['follower_count'] > randomB['follower_count']):
      more_followers='a'
    else:
      more_followers='b'
    #print(more_followers)
    if(user_ans == more_followers):
      current_score +=1
      os.system('clear')
      print(logo)
      print(f"You're right!! Current Score : {current_score}")
      randomA=randomB
      randomB = random.choice(data)
      while randomB == randomA:
        randomB=random.choice(data)
    else:
      print(f"Sorry that's wrong. Final score: {current_score}")
      game_over=True
      play=input("Do you want to play again! Type 'Y' or 'N'.\n").lower()
      if(play == 'y'):
        os.system('clear')
        play_game =True
      else:
        play_game = False
