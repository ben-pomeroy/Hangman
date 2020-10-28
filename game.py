import random
import sys
from artwork import Art

art = Art()

f = open("sports.txt", "r")
words = f.readlines()
words = [x.strip().upper() for x in words]

class Game():
	def __init__(self):
		self.alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		self.word = random.choice(words)
		self.cpuWord = [char for char in self.word]
		self.userWord = ["?" for char in self.cpuWord]
		self.stage = 0
		self.maxGuesses = art.picsLength()
		self.guessedLetters = []
		print(self.userWord)

	def guess(self):
		guess = input("Enter the letter you want to guess: ").upper()
		while(self.checkLetter(guess)) == False:
			guess = input("Enter the letter you want to guess: ").upper()

		letterFound = False
		for i in range(len(self.cpuWord)):
			if self.cpuWord[i] == guess:
				self.userWord[i] = guess
				
				letterFound = True
		if(letterFound == False):
			print(guess + " is not in the word!")
			self.stage += 1
			if(self.stage > self.maxGuesses):
				self.loseGame()
			else:
				print(art.chooseImage(self.stage))
				print(self.userWord)
		else:
			print(guess + " is in the word!")
			print(self.userWord)

	def checkLetter(self, guess):
		if(guess in self.alphabet):
			if guess in self.guessedLetters:
				print("Already guessed " + guess)
				return False
			else:
				self.guessedLetters.append(guess)
				return True
		else:
			print("Not a valid character")
			return False

	def loseGame(self):
		print("You have run out of guesses!")
		print("The final word was: " + self.cpuWord)

	def checkWin(self):
		if "?" in self.userWord:
			return False

		else:
			print("Congratulations you have won!")
			livesLeft = self.maxGuesses - self.stage
			print("You had " + str(livesLeft) + " lives left")
			sys.exit()

game = Game()

while(game.checkWin() == False):
	game.guess()
	game.checkWin()
