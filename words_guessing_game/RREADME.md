Word Guessing Game (Hangman)
A classic hangman-style word guessing game built in Python. Guess the hidden word one letter at a time before you run out of attempts!
How It Works

Enter your name — it might become one of the mystery words!
A random word is selected from the word bank
You get 2× the word length in attempts
Guess one letter at a time to reveal the hidden word
Each guess (right or wrong) costs one attempt

Usage
bashpython word_guessing_game.py
Example Session
What's your name hero? :Alex
Good luck ! Alex
you have 10 tries
_
_
_
_
_
Guess a character: i
character founded!
You have 9 left to guess
_
i
_
_
_
Guess a character: l
character founded!
You have 8 left to guess
l
i
_
_
_
Guess a character: n
character founded!
You have 7 left to guess
l
i
n
_
_
Guess a character: u
character founded!
You have 6 left to guess
l
i
n
u
_
Guess a character: x
character founded!
You have 5 left to guess
l
i
n
u
x
You Wiiin!
=>The word was : linux
Word Bank
The game selects from these words:

python
linux
games
coding
your name

Game Rules

Enter one character per guess
Entering more than one character ends the game
Just incorrect guesses reduce your remaining attempts
the correct one add one attempts
Win by revealing all letters before attempts reach zero

Requirements

Python 3.x

Author
Jabir
License
This project is open source and available for learning purposes.
