# Hangman

My first attempt at creating a text-based hangman game.

game.py - This file contains the main art of the game and is the one you run when you want to play the game. Game is the main class and has 4 methods:
 
guess - This takes a guess as a string
checkLetter - This takes the input and checks to see whether it is valid or whether its been guessed before
loseGame - Only run if the player has lost the game
checkWin - Checks to see whether the game has been won or not 

artwork.py - Has one class called art which has an array as an attribute which contains all the ASCII art for the hangman graphics (https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c)

sports.txt - Contains a list of all the words used in the sports category
