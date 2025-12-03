import random
import sys


def is_digit(value):
	try:
		int(value)
		return True
	except ValueError:
		return False


def get_number_from_user(high, low):
	number = input(f"\t\t*Enter a number between {low} and {high}: ")
	return (number)


print("\t\t------------------Welcome to the Guessing Game!-----------------")
high = input("\n\tEnter the highest number you want to guess (default = 50): ")
if (is_digit(high)):
	high = int(high)
else:
	high = 50
low = input("\tEnter the highest number you want to guess (default is 1): ")
if (is_digit(low)):
	low = int(low)
	if (low >= high):
		print("\t\t||Low number must be less than high number. Exiting the game.")
		sys.exit(0)
else:
	low = 1
random_number = random.randint(low, high)
try_time = 0
valid_number = 0

while True:
	input_user = get_number_from_user(high, low)
	while (not is_digit(input_user)):
		valid_number += 1
		print("\t\t||Enter a valid number next time")
		input_user = get_number_from_user(high, low)
		if (valid_number == 2):
			print(f"\n\t\tYou have entered invalid input too many times. The correct \
			{random_number}")
			sys.exit(0)
	input_user = int(input_user)
	if (random_number > input_user):
		try_time += 1
		print(f"Guess {try_time}:{input_user}  ->  Too Low!")
	elif (random_number < input_user):
		try_time += 1
		print(f"Guess {try_time}:{input_user}  ->  Too High!")
	else:
		try_time += 1
		print(f"Guess {try_time}:{input_user}  ->  Correct!!!")
		break
	if (try_time > 6):
		print(f"\nYou reach the maximum number of guesses. The correct number \
		was {random_number}.")
		sys.exit(0)
print(f"\n\t\tTotal Guesses: {try_time}")
