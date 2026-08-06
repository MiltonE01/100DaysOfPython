import random

print("Welcome to rock paper scissors game! Let's play!")


computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
user_choice = input("Enter your choice (Rock, Paper, Scissors): ")  

if user_choice == computer_choice:
    print("It's a tie! Both chose", user_choice)
else:
    print("You chose", user_choice)
    print("Computer chose", computer_choice)
