# space_invaders

## Credit and Collaborations
- Tyler Huntley
- James Ian Solima - Helped work out the scoring and name display

# Description
Recreation of retro style Space Invaders game

## Whiteboard Process
![gallery of games wireframe](team-agreement/Wireframe_Gallery_of_Games.jpg)

## Project Management
[Trello Gallery of Games](https://trello.com/invite/b/LdzZM5iA/ATTI95625f9015f7b008a888cf1edde70ac6CBECCA49/401-midterm)

## Resources 
[Pygame](https://www.pygame.org/docs/)
[W3 Schools](https://www.w3schools.com/python/)
[Chat GPT](gpt.md)
[Geeks for Geeks](https://www.geeksforgeeks.org/)
[Tech with Tim](https://www.techwithtim.net/tutorials/game-development-with-python/)
[Tech with Tim: Space Shooter Assets](https://techwithtim.net/wp-content/uploads/2020/04/assets.zip)
TAs: Tammy helped with getting user input to function, and scores to read from txt file and sort.
[Tammy's Replit](https://replit.com/@tammytdo/SnivelingDefenselessSynergy#main.py) - While she was helping figure out what data types I was getting back.

## Game instructions for "Space Invaders"
"Space Invaders" is a classic arcade game where the objective is to defeat a group of invading aliens with a laser cannon. In this version of the game, you control a spaceship and fight against enemy spaceships.
### Instructions
- Use the arrow keys (left, right, up, down) to move your spaceship around the screen.
- Press the spacebar to shoot lasers at the enemy spaceships.
- Your spaceship has a health bar underneath it, which decreases every time you get hit by an enemy laser or enemy ship. If your health bar reaches zero, you lose the game.
- If you destroy all of the enemy ships in the wave, you move on to the next wave.
- The game will keep track of your highest level achieved, so try to beat your previous high level every time you play.
- Good luck and have fun playing "Space Invaders"!

## SETUP
See top level README

## User Stories
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

## Link to Code
[Space Invaders](space_invaders.py)