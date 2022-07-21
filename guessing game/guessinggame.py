# Created by Samiyanur Islam
# September 2020
# All rights reserved to Samiyanur Islam

import random  # imports random from the library
CONSTANT = 100  # global variable is set to 100


def main():
	intro()
	again = True  # boolean variable to check whether to play or not
	g = 0
	tg = 0
	bg = 0
	goodgame = 0
	while (again == True):  # while loop to play the game as many times by user's command
		g += 1
		guesses = guessinggame()  # returns the output of guessinggameagain function
		tg += guesses
		# checks whether best game is smaller than best game and if goodgame is 0
		if (guesses < bg or goodgame == 0):
			bg = guesses
			goodgame = g
		print()
		again = guessinggameagain()  # runs the game again after returning true
	x = total(g, tg, goodgame)


def total(g, guesses, best):  # function that prints the results after user's command
	guesses_per_game = guesses / g  # calculates guesses/game
	print("\nOverall results:")
	print("Total games   = " + str(g))
	print("Total guesses = " + str(guesses))
	print("Guesses/game  = " + str(guesses_per_game))
	print("Best game     = " + str(best))
	print()


def intro():  # little intro about the game with instructions
	print('\t\t'"WELCOME TO GUESS THE NUMBER GAME"'\n'"I am Samiya. I am thinking of a number between 1 and", CONSTANT, end='')
	print(". Guess my number to win. I will tell you if it's higher or lower.")


def guessinggameagain():  # checks whether user wants to play again or not
	gameplay = str(input("Do you want to play again? "))
	# checks if the first element is y and returns true so that player can play again
	if gameplay[0].lower() == "y":
		return True
	else:
		return False  # anything else other than y returns false and prints the results


def guessinggame():
	print("\nI'm thinking of a number between 1 and " + str(CONSTANT) + "...")
	# geberates random number for the user to guess
	n = random.randint(1, CONSTANT)
	guess = 0
	count = 0
	while (int(guess) != n):  # while loop to keep repeating till user gets it right
		guess = input("Your Guess? ")
		if (int(guess) < n):
			print("It's higher.")  # tells the user if the its higher
		elif (int(guess) > n):
			print("It's lower.")  # tells the user if the its lower
		count += 1  # cumulitive sum algorithm
	if (count > 1):
		print("You got it right in " + str(count) +
		      " guesses!")  # prints the count value
	else:
		print("You got it right in 1 guess!")
	return count  # returns the value so it can be used elsewhere


main()