# space_invaders

## Credit and Collaborations
- Tyler Huntley

# Description
Recreation of retro style Space Invaders game

## Whiteboard Process
![gallery of games wireframe](team-agreement/Wireframe_Gallery_of_Games.jpg)

## Project Management
[Trello Gallery of Games](https://trello.com/invite/b/LdzZM5iA/ATTI95625f9015f7b008a888cf1edde70ac6CBECCA49/401-midterm)

## Resources 
[Pygame](https://www.pygame.org/docs/)
[Tech with Tim](https://www.techwithtim.net/tutorials/game-development-with-python/)
[Space Invaders Assets](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkhzMi1yNjdIYXJlMDBZLUQwUzNvb2N5V2V6d3xBQ3Jtc0ttbnc1bG5hcWtmUDZvaEhTbnJDTHVxZEtYcGpZcUU3eHpXVDNfRXZIbkJVQ3pWMEJsMGJPcDhUWGtxMTRlUnM2RXhXd0JlcjhZck9KT3VNMzdWMjFkb00wc28ySk5MQmZXNW9ickR3R2hjWmlHN3FJSQ&q=https%3A%2F%2Ftechwithtim.net%2Fwp-content%2Fuploads%2F2020%2F04%2Fassets.zip&v=Q-__8Xw9KTM)


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