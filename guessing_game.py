import random
import sys


def is_digit(value):
	if (type(value) is int):
		return True
	return False


def get_number_from_user():
	number = input("*Enter a number between 1 and 50: ")
	return int(number)


random_number = random.randint(1, 50)
try_time = 0
valid_number = 0

while True:
	input_user = get_number_from_user()
	while (not is_digit(input_user)):
		valid_number += 1
		print("*Enter a valid number next time")
		input_user = get_number_from_user()
		if (valid_number > 3):
			print(f"\nYou have entered invalid input too many times. The correct number\
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
	if (try_time > 7):
		print(f"\nYou reach the maximum number of guesses. The correct number \
		was {random_number}.")
		sys.exit(0)
print(f"\nTotal Guesses: {try_time}")
