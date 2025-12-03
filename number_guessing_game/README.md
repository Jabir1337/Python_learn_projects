Number Guessing GameA simple command-line number guessing game written in Python. The program challenges you to guess a randomly selected number within a range you define.How It Works
Set your range by entering a lower and upper bound
The program randomly selects a number within your range
Guess the number — you get feedback after each attempt:

Too Low — your guess is below the target
Too High — your guess is above the target
Correct — you found it!


Try to guess the number in 6 attempts or fewer
Usagebashpython number_guessing_game.pyExample Session		
------------------Welcome to the Guessing Game!-----------------

	Enter the highest number you want to guess (default = 50): 100
	Enter the lowest number you want to guess (default is 1): 1
		*Enter a number between 1 and 100: 50
Guess 1:50  ->  Too Low!
		*Enter a number between 1 and 100: 75
Guess 2:75  ->  Too High!
		*Enter a number between 1 and 100: 62
Guess 3:62  ->  Correct!!!

AuthorJabirLicenseThis project is open source and available for learning purposes.
