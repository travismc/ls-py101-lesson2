import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

WINNING_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}


def prompt(message):
    print(f'===> {message}')


def player_wins(player_choice, computer_choice):
    if computer_choice in WINNING_COMBOS[player_choice]:
        prompt("You win!")
    else:
        prompt("You lose!")


while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    player_choice = input()

    while player_choice not in VALID_CHOICES:
        prompt("That's not a valid choice.")
        choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(f'You chose {player_choice}, computer chose {computer_choice}')

    player_wins(player_choice, computer_choice)

    prompt("Do you want to play again? (y/n) ")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] == 'n':
        break
