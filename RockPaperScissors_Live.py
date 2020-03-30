
# 1) Title - Rock, Paper, Scissors
print("Human VS Computer: Rock, Paper, Scissors!")
print("---------------------------------------------")
import time
time.sleep(1)

# 2) Give User Instructions
print("Instructions:")
print("---------------")
print("Type in 'Rock', 'Paper', or 'Scissors' into the computer. Rules are rock beats scissors, but loses to paper. Scissors beats paper.")
time.sleep(1)

# 3) Get input from human
print("Please enter: 'Rock', 'Paper', or 'Scissors':")
print('\n')
human_turn = input()
print('\n')
print("---------------")

time.sleep(1)
print("The human played: {}".format(human_turn))

print('\n')
print("---------------")

# 4) Input from computer
import random # ability to get random numbers
computer_number = random.randint(1,3) # Chooses random number from 1, 2, or 3

if computer_number == 1:
    computer_turn = "Rock"
elif computer_number == 2:
    computer_turn = "Paper"
else:
    computer_turn = "Scissors"

time.sleep(1)
print("The AI Crazy Computer Genius played: {}".format(computer_turn))

# 5) Show who played what

# 6) To compare ; who wins?

time.sleep(1)
# If human plays Rock
if human_turn == 'Rock':
    # If computer plays Rock
    if computer_turn == 'Rock':
        print('It is a tie! Both Rock! Darn it.')
    # if computer plays paper
    elif computer_turn == 'Paper':
        print('Shoot! Paper beats Rock. You got beat by the computer.')
    # if computer plays scissors
    else:
        print('Congrats! You win! ')

# If human plays paper
if human_turn == 'Paper':
    # If computer plays Rock
    if computer_turn == 'Rock':
        print('Humans rule! Computers drool(?)')
    # if computer plays paper
    elif computer_turn == 'Paper':
        print('Paper, paper -- tie')
    # if computer plays scissors
    else:
        print('AI will take over the earth. Scissors > Paper')

# If human plays scissors
if human_turn == 'Scissors':
    # If computer plays Rock
    if computer_turn == 'Rock':
        print('Computer wins; sorry')
    # if computer plays paper
    elif computer_turn == 'Paper':
        print('Haha humans forever! Scissors > Paper')
    # if computer plays scissors
    else:
        print('Scissor tie')

print('To play again, click the green run button at the top')
