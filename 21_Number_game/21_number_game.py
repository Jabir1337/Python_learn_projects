import random


def check_21(last_number):
	return (last_number == 21)


def last_number_of_array(array):
	return (array[len(array) - 1])


def user_ui(array):
	i = 0
	print("How many number you want enter")
	playe_number = int(input(">"))
	last_number = last_number_of_array(array)
	while (i < playe_number):
		last_number += 1
		if (check_21(last_number)):
			return False
		array.append(last_number)
		i += 1
	if (array[0] == 0):
		array.remove(0)
	print("order input after your turn:")
	print(array)
	return (True)


def player_turn(array):
	if (user_ui(array)):
		if (computer_turn(array) == 'computer'):
			return 'computer'
		else:
			return 'continue'
	else:
		return 'player'


def computer_ui(array):
	i = 0
	computer_number = random.randint(1, 3)
	last_number = last_number_of_array(array)
	while (i < computer_number):
		last_number += 1
		if (check_21(last_number)):
			return False
		array.append(last_number)
		i += 1
	if (array[0] == 0):
		array.remove(0)
	print("Order after computer's turn")
	print(array)
	return (True)


def computer_turn(array):
	if (computer_ui(array)):
		if (player_turn(array) == 'player'):
			return 'player'
		else:
			return 'continue'
	else:
		return 'computer'


print("\tWelcome to 21 game!!")
yes_no = input("Do you want to start the game? (yes/no)\n>")
if (yes_no == 'No'):
	exit(0)
array = [0]
print("Enter 'f' to take the first chance.")
print("Enter 's' to take the first chance.")
turn = input(">")
if (turn == 'f'):
	string = player_turn(array)
elif (turn == 's'):
	string = computer_ui(array)
else:
	print("Wrong input!")
	exit(0)
if (string == 'player'):
	print(f"\n=> final result: {array}")
	print("congrats you win!!")
else:
	print(f"\n=> final result: {array}")
	print("Congrats you lose!!\n because you add the 21 number")
