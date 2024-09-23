# Walk-through: Rock Paper Scissors
# In this assignment, we'll build a Rock Paper Scissors game. 
# Rock Paper Scissors is a simple game played between two opponents. 
# Both opponents choose an item from rock, paper, or scissors. 
# The winner is decided according to the following rules:

# If player a chooses rock and player b chooses scissors, player a wins.
# If player a chooses paper and player b chooses rock, player a wins.
# If player a chooses scissors and player b chooses paper, player a wins.
# If both players choose the same item, neither player wins. It's a tie.
# Our version of the game lets the user play against the computer. The game flow should go like this:

# The user makes a player.
# The computer makes a player.
# The winner is displayed.

import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
	print(f'===> {message}')

def display_winner(player, computer):
	if player == computer:
		prompt("It's a tie!")
	elif ((player == 'rock' and computer == 'scissors') or
		(player == 'paper' and computer == 'rock') or 
		(player == 'scissors' and computer == 'paper')):
		prompt('You win!')
	else:
		prompt('You lose!')

while True:
	prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
	choice = input()

	while choice not in VALID_CHOICES:
		prompt("That's not a valid choice.")
		choice = input().lower()

	computer_choice = random.choice(VALID_CHOICES)

	prompt(f'You chose {choice}, computer chose {computer_choice}')

	display_winner(choice, computer_choice)

	prompt("Do you want to play again? (y/n) ")
	answer = input().lower()
	while True:
		if answer.startswith('n') or answer.startswith('y'):
				break
		
		prompt('Please enter "y" or "n".')
		answer = input().lower()

	if answer[0] == 'n':
		break
