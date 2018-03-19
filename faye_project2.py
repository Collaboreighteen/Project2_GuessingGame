# Objectives: In 3 turns, guess which planet I'm thinking of with hints.

# Size (Bigger or Smaller)

# Moons (More or Less)

# Distance from Sun (Further or Closer)

import random

def distanceHint():
	if guess.distance > answer.distance:
		print("The correct answer is closer to the sun than "+str(guess.name))

	else:
		print("The correct answer is further from the sun than "+str(guess.name))

	return

def moonHint():
	if guess.moons > answer.moons:
		print("The correct answer has less moons than "+str(guess.name))

	else:
		print("The correct answer has more moons than "+str(guess.name))

	return


def sizeHint():
	if guess.size > answer.size:
		print("The correct answer is smaller than "+str(guess.name))

	else:
		print("The correct answer is larger than "+str(guess.name))

	return

def wrongAns():
	print("You suck")

	distanceHint()
	moonHint()
	sizeHint()

	return

print("Hello and welcome to my planet game.")

class planet:
	def __init__(self, name, distance, moons, size):
		self.name = name
		self.distance = distance # aphelion (AU)
		self.moons = moons # count
		self.size = size # mean radius

	def __str__(self):
		return self.name

	# def __eq__(self, other):
	# 	return self.name == other

mercury = planet("mercury", .466, 0, 2439.7)
venus = planet("venus", .728, 0, 6051.8)
earth = planet("earth", 1.017, 1, 6371)
mars = planet("mars", 1.666, 2, 3389.5)
jupiter = planet("jupiter", 5.4588, 67, 69911)
saturn = planet("saturn", 10.123, 62, 58232)
uranus = planet("uranus", 20.11, 27, 25362)
neptune = planet("neptune", 30.33, 14, 24622)

planetList = [
	mercury,
	venus,
	earth,
	mars,
	jupiter,
	saturn,
	uranus,
	neptune
]

answer = random.choice(planetList)

# print(answer.name)

guessNum = 0

while (guessNum < 3):
	guessLeft = 3 - guessNum

	guess = input("Can you guess what planet I'm thinking of? You have " + str(guessLeft) + " guesses left\n")

	try:
		guess = [planet for planet in planetList if planet.name == guess][0] # returns a list of 1
	except IndexError:
		print("Oops, that's not a planet")


	if guess == answer:
		print("You got it!")

	else:
		wrongAns()
		guessNum = guessNum + 1


print("Game Over!!!\nThe answer was " + str(answer))





	