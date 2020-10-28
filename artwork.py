class Art():
	def __init__(self):
		self.pics = ['''
					  +---+
					  |   |
					      |
					      |
					      |
					      |
					=========''', '''
					  +---+
					  |   |
					  O   |
					      |
					      |
					      |
					=========''', '''
					  +---+
					  |   |
					  O   |
					  |   |
					      |
					      |
					=========''', '''
					  +---+
					  |   |
					  O   |
					 /|   |
					      |
					      |
					=========''', '''
					  +---+
					  |   |
					  O   |
					 /|\  |
					      |
					      |
					=========''', '''
					  +---+
					  |   |
					  O   |
					 /|\  |
					 /    |
					      |
					=========''', '''
					  +---+
					  |   |
					  O   |
					 /|\  |
					 / \  |
					      |
					=========''']

	def chooseImage(self, stage):
		if(stage == 1):
			return self.pics[0]
		if(stage == 2):
			return self.pics[1]
		if(stage == 3):
			return self.pics[2]
		if(stage == 4):
			return self.pics[3]
		if(stage == 5):
			return self.pics[4]
		if(stage == 6):
			return self.pics[5]
		if(stage == 7):
			return self.pics[6]

	def picsLength(self):
		return len(self.pics)