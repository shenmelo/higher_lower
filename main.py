import random
from replit import clear
from art import logo, vs
from game_data import data


def get_data():
  return random.choice(data)


def format_account(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(letter, a_follower, b_follower):
  if a_follower > b_follower:
    return letter == 'a'
  else:
    return letter == 'b'

def game():
  print(logo)
  
  score = 0
  name_b = get_data()
  is_answer_correct = True
  
  while is_answer_correct:
    name_a = name_b
    name_b = get_data()
    while name_a == name_b:
      name_a = name_b
      name_b = get_data()
      print(f"Compare A: {format_account(name_a)} {name_a['follower_count']}")
      print(vs)
      print(f"Compare B: {format_account(name_b)} {name_b['follower_count']}")
      letter = input("Who has more followers? Type 'A' or 'B': ").lower()
  
      a_follower_count = name_a['follower_count']
      b_follower_count = name_b['follower_count']
      is_correct = check_answer(letter, a_follower_count, b_follower_count)
  
      clear()
      print(logo)
      if is_correct:
        score += 1
        print(f"You're right! Current score is: {score}")       
      else:
        print(f"Sorry, that's wrong. Your final score is: {score}")
        is_answer_correct = False
        
game()

