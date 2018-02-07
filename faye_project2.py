# Objectives: In 3 turns, guess which planet I'm thinking of with hints.

# Size (Bigger or Smaller)

# Moons (More or Less)

# Distance from Sun (Further or Closer)

import random

print("Hello and welcome to my planet game.")

class planet:
	def __init__(self, name, distance, moons, size):
		self.name = name
		self.distance = distance # aphelion (AU)
		self.moons = moons # count
		self.size = size # mean radius		

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

print(answer.name)

guess = input("Can you guess what planet I'm thinking of? \n")

guess = [planet for planet in planetList if planet.name == guess][0] # returns a list of 1

print(guess.name)

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


if guess == answer:
	print("You got it!")

else:
	print("You suck")

	distanceHint()
	moonHint()
	sizeHint()

	