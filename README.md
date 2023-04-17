# gallery-of-games

## Credit and Collaborations

- James Ian Solima
- Darran Holmes
- Tyler Huntley
- Dutch Foy
- Mandela Steele-Dadzie

# Description
We are creating an arcade style game that contains multiple games within our main pygame program.

## Whiteboard Process
![gallery of games wireframe](team-agreement/Wireframe_Gallery_of_Games.jpg)

## Project Management
[Trello Gallery of Games](https://trello.com/invite/b/LdzZM5iA/ATTI95625f9015f7b008a888cf1edde70ac6CBECCA49/401-midterm)

## Resources 
[Space Invaders Assets](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkhzMi1yNjdIYXJlMDBZLUQwUzNvb2N5V2V6d3xBQ3Jtc0ttbnc1bG5hcWtmUDZvaEhTbnJDTHVxZEtYcGpZcUU3eHpXVDNfRXZIbkJVQ3pWMEJsMGJPcDhUWGtxMTRlUnM2RXhXd0JlcjhZck9KT3VNMzdWMjFkb00wc28ySk5MQmZXNW9ickR3R2hjWmlHN3FJSQ&q=https%3A%2F%2Ftechwithtim.net%2Fwp-content%2Fuploads%2F2020%2F04%2Fassets.zip&v=Q-__8Xw9KTM)


## SETUP
```
python3 -m venv .venv
python3 .venv/bin/activate

pip install -r requirements.txt
# Will install pytest by default
# Will install pygame by default
```

## User Stories
As a User, I want an easy to follow UI in the terminal to guide me to some video games.
Feature Tasks:
Implement ‘Welcome’ Menu
Implement ‘Help’ Option
Help Option will show how to navigate menu
Help Option will show how to play game depending on what game user chooses
Display games that are available to play 
Displays ‘Exit’ option
Acceptance Tests:
Verify ‘Welcome’ message displays to user
Displays options
Options go to each pertaining menu choice, respectfully
‘Help’ option - shows the directions
‘Game Choice’ 
Goes to menu asking if user wants 1P or 2P 
Also displays Current high score of the ‘Game Choice’
Starts ‘Game Choice’ after selecting # of players 
Exits menu if user chooses to exit

As a player, I want to play Space Invaders, control my spaceships movement using arrow keys so that I can navigate through space and dodge enemy attacks.
Feature Tasks:
Implement arrow key controls for spaceship movement
Add collision detection to ensure the spaceship cannot move outside of the game screen
Ensure that the spaceship movement is smooth and responsive to player input
Acceptance Tests:
Verify spaceship actually moves in direction of key pressed
Ensure spaceship cannot move beyond screen bounds
Test movement for responsiveness and smoothness

As a player, I want to be able to shoot lasers from my spaceship so that I can destroy enemy ships
Feature Tasks:
Implement laser firing when player presses space bar
Add collision detection for lasers to detect hits on enemy ships
Enemy ship disappears when hit
Acceptance Tests:
Verify that lasers are fired when space bar is pressed
Ensure lasers collide with enemy ships

As a player, I want the ability to play a game of pong against a bot, and track the high score.
Feature Tasks:
paddles move up and down using the arrow keys
ball bounce off the paddles and the top and bottom walls of the game screen
Score - kept for each player - Displayed during/at end of the game - game ends after 5 missed balls
After the game ends, can players start a new game or exit
Sound effects(?) ball hits a paddle, wall, game is over, player scores
Build it
game screen, white paddles and ball, and a center dividing line.
paddles move when players press keys.
ball bounces off the paddles and the top and bottom walls of the game screen, and increases speed with each hit.
scoring system that displays each player's score on screen and updates when a player scores. The winning player's score, display differently or only once game over
sound effects for when the ball hits a paddle, a player scores, and the game ends.
players can pause and restart the game by pressing certain keys. When paused, should it display a "PAUSED" message?
Test
paddles move up and down when the corresponding arrow keys are pressed.
that the ball bounces off the paddles and the top and bottom walls of the game screen.
score is properly incremented when a player scores a point.
game ends when one player reaches a score of 11 and displays the winner message and gives the option to start a new game or exit.
sound effects are played when the ball hits a paddle, a player scores, and the game ends.
game can be paused and resumed correctly using keyboard shortcuts, and that the "PAUSED" message is displayed when the game is paused.

As a player, I want to play a Python version of the classic game Hangman, so that I can enjoy a fun and challenging word game.
Feature Tasks:
Can players guess letters to try and reveal the hidden word?
Is there a limit to the number of incorrect guesses a player can make before they lose?
Does the game display a cool hangman figure as incorrect guesses are made?
Does the game end when the word is correctly guessed or the player runs out of guesses? After the game ends, can players start a new game or exit?
Are there cool sound effects for when a player makes a correct or incorrect guess, and when the game ends?
Can players pause and restart the game using keyboard shortcuts?
Build it:
Create a cool game screen with a black background and a section for displaying the hidden word and the incorrect guesses.
Make sure players can input letters to guess using the keyboard.
Display a cool hangman figure that is gradually filled in as incorrect guesses are made.
Set up a limit for incorrect guesses, after which the game ends.
Add some cool sound effects for when a player makes a correct or incorrect guess, and when the game ends.
Make it so players can pause and restart the game by pressing certain keys. When paused, the game should display a "PAUSED" message in the center of the screen.
Test:
Make sure that players can guess letters and reveal the hidden word correctly.
Check if the game ends when the player runs out of guesses or correctly guesses the word, and if they have the option to start a new game or exit.
Ensure that the correct sound effects are played when a player makes a correct or incorrect guess, and when the game ends.
Verify that the game can be paused and resumed correctly using keyboard shortcuts, and that the "PAUSED" message is displayed when the game is paused.

## Requirements
pygame==2.3.0
attrs==22.2.0
exceptiongroup==1.1.1
iniconfig==2.0.0
packaging==23.0
pluggy==1.0.0
pytest==7.2.2
tomli==2.0.1