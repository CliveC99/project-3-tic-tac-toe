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
  - <p><a href="#imported-modules">Imported Modules</a></p>
  - <p><a href="#bugs-and-fixes">Bugs and Fixes</a></p>
  - <p><a href="#deployment">Deployment</a></p>
  - <p><a href="#cloning">Cloning</a></p>
  - <p><a href="#forking">Forking</a></p>
  - <p><a href="#git-commits">Git Commits</a></p>

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

   # Imported Modules
  - OS
    - I used `os.system('clear')` to clear the terminal so it wouldn't be clogged up.
  - Time
    - I used `time.sleep(3)` so it would give the user time to read the information.

    # Bugs and Fixes
  | Bugs/Errors        |   Explain   | Fix |
   | -------------  |:-------------:| -----: |
   | User input  | I was having issues with user input if the wrong data was entered. | I got help from [Stack Overflow.](https://stackoverflow.com/questions/49496609/user-input-being-incorrectly-appended-to-python-list) |
   | Index errors | I was having issues with index errors being one off. | I fixed this by adding `int(position) - 1` where needed. |
   | Score counter | I was having issues with the score counter adding for a win. |  I solved this by adding `player_one += 1` I got help from [Stack Overflow](https://stackoverflow.com/questions/26514438/python-how-to-keep-score-in-a-tic-tac-toe-game)|
   | Reset score counter | I was having issues with the score counter resetting. | I solved this by adding `player_one = 0 player_two = 0` |

   # Deployment

1. Open up [Heroku.](https://dashboard.heroku.com/apps)
2. Click "New" at the top right.
3. Click "Create new app".
4. Choose an "App name" and pick your region.
5. Click "Create app".
6. Click "Settings".
7. Locate config vars and click "Reveal Config Vars".
8. Set the key to "PORT".
9. Set the value to "8000".
10. Click "Add buildpack".
11. Add "python" and "nodejs".
12. Click "Deploy" and connect Github.
13. Search for your "repo-name".
14. Click "Automatic Deploys"

# Cloning
1. Open up the repository [project-3-tic-tac-toe.](https://github.com/CliveC99/project-3-tic-tac-toe)
2. Above the list of files click "Code".
3. Click if you would like to clone as "HTTPS", "SSH", or "GitHub CLI".
4. Once selected press copy.
5. Open Git Bash.
6. Change the directory to where you want the clone to appear.
7. Paste in the link you copied in step 4. (This is the line for my repository): <br>
  `$ git clone https://github.com/CliveC99/project-3-tic-tac-toe`
8. Press enter and the clone will happen.

# Forking
1. Open up the repository [project-3-tic-tac-toe.](https://github.com/CliveC99/project-3-tic-tac-toe)
2. Locate the fork button at the top right.
3. Select an owner and repository name.
4. Add a description (optional).
5. Click "Create fork".
6. The repository should appear in your repositories now.

# **Git Commits**
   - I structured my git commits whenever I would add, change or update code.
   - I did this by using:
   1. git status
   2. git add (file name)
   3. git commit -m (message)
   4. git push.
  ![Git Commits](https://res.cloudinary.com/dp9lxtk3y/image/upload/v1681686359/p3-tic-tac-toe/git-commits1_esa2s2.jpg)
