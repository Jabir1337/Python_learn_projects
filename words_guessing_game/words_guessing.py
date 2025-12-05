import random
import sys

guesses = ''
trys = None
i = None

name = input("What's your name hero? :")
print("Good luck !", name)
words = ['python', name, 'linux', 'games', 'coding']
word_to_guess = random.choice(words)
trys = len(word_to_guess) * 2
print(f"you have {trys} tries")
while trys > 0:
	failed = 0
	i = 0
	while i < len(word_to_guess):
		if word_to_guess[i] in guesses:
			print(word_to_guess[i])
		else:
			print('_')
			failed = 1
		i += 1
	if failed == 0:
		print("You Wiiin!")
		print("=>The word was :", word_to_guess)
		break
	user_guess = input("Guess a character: ")
	if (len(user_guess) != 1):
		print("You should enter a character!")
		print("=>The word was :", word_to_guess)
		print(">>>> Ending game >>>>")
		sys.exit(0)
	guesses += user_guess
	if (user_guess not in word_to_guess):
		trys -= 1
		print("Wrong")
		print(f"You have {trys} left to guess")
	else:
		trys += 1
		print("character founded!")
		print(f"You have {trys} left to guess")
	if trys == 0:
		print("\nYou lose!")
		print("=>The word was :", word_to_guess)
