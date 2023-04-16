# Tic-Tac-Toe - 2 Player Edition
Here you can play Tic-Tac-Toe against your friends.

The aim of the game is to get 3 'X's' or 3 'O's' in a row, column or diagonally.

Check out [Tic-Tac-Toe](https://tic-tac-toe-2-player.herokuapp.com/)

### **Disclaimer if you would like to open any links in a new tab use `Ctrl` and click the link.**

# Table of Contents
  
  - <p><a href="#flowchart">Flowchart</a></p>
  - <p><a href="#how-to-play">How To Play</a></p>
  - <p><a href="#ux">UX</a></p>
  - <p><a href="#features">Features</a></p>
  - <p><a href="#manual-testing">Manual Testing</a></p>

# Flowchart
![Flowchart](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681663239/p3-tic-tac-toe/flowchart-start.drawio_4_lrgkpj.png)


# How to play
- The game is played on a 3x3 board.
- Player 1 is given 'X' and Player 2 is given 'O'
- The aim of the game is to get 3 'X's or 3 'O's in a row, column or diagonally.
- If the board is filled without the above terms. The game is a draw

  # UX
### **User Goals** 
- As a user, I want to be able to play against my friends.
- As a user, I want the information to be understandable.
- As a user, I want my score to be counted to see who wins overall.
- As a user, I want the game to run smoothly.
- As a user, I want to be able to play again.

### **Owner Goals**
- As the owner, I want to be able to add new features.

### **Returning User**
- As a returning user, I want to try and beat my previous scores against friends.

# Features
## **Exisiting Features**
* Welcome message
* Gameboard
* Python sleep()
* Players turns
* Winner/Draw
* Scoreboard
* Play again
* Reset score
| Feature        |      |
   | -------------  |:-------------:| 
   | Welcome message | ![Welcome Message](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681675512/p3-tic-tac-toe/welcome-message_ybkagc.jpg) |
   | User input validation | ![User input validation](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681675621/p3-tic-tac-toe/input-validation_nnnx4m.jpg) |
   | Gameboard | ![Gameboard](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681675701/p3-tic-tac-toe/gameboard_sbrv1d.jpg) |
   | Python sleep() example | ![Python sleep()](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681676075/p3-tic-tac-toe/sleep-module_tz7g7l.jpg) |
   | Example of players turn | ![Players turn](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681676217/p3-tic-tac-toe/players-turn_g8ykty.jpg) |
   | Example of winner/draw | ![Winner/draw](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681676657/p3-tic-tac-toe/winner_gr8gvf.jpg) |
   | Scoreboard | ![Scoreboard](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681677425/p3-tic-tac-toe/scoreboard_wv8sk4.jpg) |
   | Play again | ![Play again](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681677497/p3-tic-tac-toe/play-again_zrmdwi.jpg) |
   | Reset scoreboard | ![Reset scoreboard](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681677564/p3-tic-tac-toe/reset-score_h2btkj.jpg) |
## Features to be added
* Option to play against the computor.
* Username control.
* Leaderboard.

# Manual Testing
   | Feature        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | User input verifaction | Show error message and let the user input the right data. | If the user input the wrong data, an error shows. If the user inputs the correct data, it moves to the next step. | Input correct data and input incorrect data. |
   | Python sleep   | Pause the next step from showing up.    | There was a pause of the next step showing where required. | Input data to move to the next step. |
   | Players turns   | Switch from 'X' to 'O'.   | Switched correctly | Input data on the board. |
   | Win or Draw | Show who won or the game was a draw.  | Printed the winner or if the game was a draw. | Played the game to see if it would give the right output. |
   | Play again | Start the game again.   | The game started. | Restart the game. |
   | Reset score   | Score either is reset or continues | When selected the score reset, when not selected the score kept counting. | Reset the score, play without resetting the score. |


   | Testing        |    Expected   | Result       | Test |
   | -------------  |:-------------:| -----:| -----: |
   | Pep8 Linter | Pass. | No Errors. | ![test](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681679398/p3-tic-tac-toe/pep8_leax3w.jpg) |
   | Local Terminal | Game to function without issues. | Game functioned. | Play the game. |
   | CI Heroku Terminal | Game to function without issues. | Game functions. | Play the game. |
