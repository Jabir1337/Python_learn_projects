🎯 21 Game

A strategic counting game — don’t be the one who says 21!

🧠 Overview

21 Game is a simple yet tricky number game where you compete against the computer.
Players take turns adding 1 to 3 consecutive numbers to a growing sequence.
Whoever is forced to say 21... loses! 😅

⚙️ How It Works

Choose whether to go first or second.

On your turn, you can add 1 to 3 consecutive numbers to the sequence.

The computer does the same on its turn.

Whoever says 21 — loses the game.

💻 Usage

Run the game with:

python 21_game.py

🕹️ Example Session
Welcome to 21 Game!!
Do you want to start the game? (yes/no)
> yes

Enter 'f' to take the first chance.
Enter 's' to let the computer go first.
> f

How many numbers you want to enter?
> 3
Order after your turn:
[1, 2, 3]

Order after computer's turn:
[1, 2, 3, 4, 5]

How many numbers you want to enter?
> 2
Order after your turn:
[1, 2, 3, 4, 5, 6, 7]

Order after computer's turn:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

...

Congrats! You lose 😭  
Because you added the number **21**.

📜 Game Rules

You can add 1, 2, or 3 numbers per turn.

Numbers must be consecutive (if last is 5 → you can add 6, 7, 8).

The player who adds 21 loses.

You can choose to start first or let the computer start.

🧩 Strategy Tip

Think backwards from 21!
If you can make the computer reach one of these numbers:
1, 5, 9, 13, 17,
you’ll always win.

🧮 Formula:

(21 - current_number) % 4 == 0

🕹️ Controls
Input	Action
f	Take the first turn
s	Let the computer go first
1–3	Numbers to add on your turn
🧰 Requirements

Python 3.x

👨‍💻 Author

Jabir Gaadi

📂 This project is open-source and made for learning purposes.
