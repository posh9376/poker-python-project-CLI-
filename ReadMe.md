## Python Poker CLI
This is a simple Python-based Poker game implemented as a Command-Line Interface (CLI) application. The game allows two players (one human and one computer) to play a simplified version of Four-Card Stud Poker. The game features three betting rounds, hand evaluation, and a basic computer opponent that can randomly make decisions.

## Acknowledgement
## Authors
Posh9376 (Scrum master)
Marilynmonroecode
Abdirahman005
Augustinemeso
BsCit-05-39008695
Alvin wanjohi


## Features
Two Players: Play against an computer opponent (Player 1 vs Player 2).
Poker Hand Evaluation: Poker hands are evaluated based on card ranks.
Betting Rounds: Three betting rounds where players can bet, raise, check, or fold.
Pot Management: The game tracks the pot and chips for each player.
computer Opponent: The computer randomly chooses to check, bet, raise, or fold based on its current hand.
Simple Command-Line Interface: Interaction happens through simple prompts in the terminal.

## Requirements
Python: Python3 is required to run this project.
No external libraries are needed, as the game uses only the built-in Python random module for shuffling cards and making random decisions.

## Installation
Clone the repository:

git clone https://github.com/posh9376/poker-python-project-CLI-.git
cd poker-python-project-CLI

Run the Game: In your terminal, navigate to the project directory and run the following command:

run app.py in your terminal
This will start the game and prompt you for actions during the betting rounds.

## Game Instructions
Welcome Screen: The game introduces the poker variant and explains the betting structure.
Card Dealing: Each player (Player 1 and Player 2) receives 4 cards.
Betting Rounds:
Player 1 will be prompted to Bet, Raise, Check, or Fold.
Player 2 (computer) will randomly choose to Check, Bet, Raise, or Fold.
Showdown: After all betting rounds, the hands are compared, and the winner is determined based on the hand scores.
Chip Management: Players start with 1000 chips each. Betting affects the chips available to each player, and the total pot increases with each bet.
End of Game: The game displays the winner, the final chip count for both players, and the total amount of chips in the pot.
