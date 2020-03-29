#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:53:40 2020

ROCK PAPER SCISSORS
FB LIVE STREAM

@author: averysmith
"""

# Give a title 
print("Rock Paper Scissors")
print('--------------------------------------------')

# Give instructions
print('In Rock, Paper, Scissors, you choose on the those three things in aim of beating your opponent. Rock beats Scissors, but loses to Paper. Paper loses to scissors.')
print('\n')

# Get input from player
print('Your Move?')
print("Please Enter 'Rock', 'Paper', or 'Scissors':")
player_turn = input()

# Get computer turn
import random # ability to get random numbers
computer_number = random.randint(1, 3) # A random 1, 2, 3
if computer_number == 1:
  computer_turn = 'Rock'
elif computer_number == 2:
  computer_turn = 'Paper'
else:
  computer_turn = 'Scissors'

# Showing who played what
print('-----------------------------')
print('\n')
import time
time.sleep(1)
print('The Human Played: {}'.format(player_turn))
time.sleep(1)
print('The Computer Played: {}'.format(computer_turn))
time.sleep(1)

print('-----------------------------')
print('\n')

# Compare the turns
# If you played Rock...
if player_turn == 'Rock':
  if computer_turn == 'Rock':
    print("It's a tie!")
  if computer_turn == 'Paper':
    print("Oops! Computer won :(")
  if computer_turn == 'Scissors':
    print("Yay! You won!")
# If you played Paper
if player_turn == 'Paper':
  if computer_turn == 'Rock':
    print("Booyeah! You win :)")
  if computer_turn == 'Paper':
    print("Boring--it's a tie")
  if computer_turn == 'Scissors':
    print("Shoot! You got cut! You lose.")
# If you played scissors
if player_turn == 'Scissors':
  if computer_turn == 'Rock':
    print("Smashed; you lose this one.")
  if computer_turn == 'Paper':
    print("Nice job! Victory!")
  if computer_turn == 'Scissors':
    print("Looks like you and the computer thought the same; tie!")
