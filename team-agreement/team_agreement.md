# 401-midterm

## Credit and Collaborations

- James Ian Solima
- Darran Holmes
- Tyler Huntley
- Dutch Foy
- Mandela Steele-Dadzie

### Communication

What hours will you be available to communicate?

- M-F 9am-6pm PST (We'll keep in contact)
- Weekends, on discretion

What platform will you use to communicate (ie. Slack, phone …)?

- Slack

How often will you take breaks?

- breaks as needed, Hourly

What is your plan if you start to fall behind?

- We'll decide to take a little extra time and plan out what needs to be done. Before or after class with a fresh mind
Potentially reevaluate goals and features, and complete what needs to be done for a working MVP.

How will you communicate after hours and on the weekend?

- Slack, Remo

What is your strategy for ensuring everyone’s voice is heard?

- We will do a daily meet to check on progress with each member, where we address issues, code challenges and set goals for the day.

How will you ensure that you are creating a safe environment where everyone feels comfortable speaking up?

- We will keep open communication and an inclusive and non hostile environment

### Cooperative

Make a list of each parson’s strengths.

- James: Decent at algorithms and learning new concepts, usually flexible and available
- Tyler: Communication, Time management, Growth mindset
- Darran: Diligent, Patient
- Dutch: Communication visionary
- Mandela: API setup


How can you best utilize these strengths in the execution of your project?

- We will help each other through the process using our different strengths to cover another's possible weaknesses and learn from each other wherever possible. 

In which professional competencies do you each want to develop greater strength?

- James: Understanding documentation and being better at coding in general
- Tyler: Craft and quality competencies
- Darran: Problem-solving
- Dutch: Inflexibility, impulsive
- Mandela: Communication

Knowing that every person in your team needs to understand the code, how do you plan to approach the day-to-day development?

- We will do our best to write idiomatic and meaningful code, so it is understandable by everyone on the group

## Conflict Resolution

What will be your group’s process to resolve conflict, when it arises?

- We will write out our conflicts and get a third party involved to give advice on how to move forward. We will also talk out our issue first before the become a problem.

What will your team do if one person is pulling all the weight while the other person is not contributing?

- Give that person driver responsibility or otherwise have them help the team. We can also have them in a navigator role to help another member who is not a strong learn.

What will your team do if one person is taking over the project and not letting the other member contribute?

- Have a meeting and separate the tasks so it doesn't belong to one person. 

How will you approach each other and the challenge of building an application knowing that it is impossible for two people to be at the exact same place in understanding and skill level?

- Be patient and have a more confident person navigate while the person who may not be at the same skill drives.

How will you raise concerns to members who are not adequately contributing?

- We will raise these concerns in a meeting and task them appropriately.

How and when will you escalate the conflict if your resolution attempts are unsuccessful?

- Get a third party involved when it becomes detrimental to the progress of the project

## Work Plan

- How you will identify tasks, assign tasks, know when they are complete, and manage work in general?

Through daily morning standups, we'll go over what needs to be accomplished and assign tasks based on what we feel comfortable doing and break for the day.

- What project management tool will be used?

Trello

## Git Process

- What components of your project will live on GitHub?

Our code

- How will you share the repository with your teammates?

All members of the group will be assigned collaborator roles on the github repo

- What is your Git flow?

We will have a developer branch -> 
Each person creates a new branch from developer branch -> 
works on a feature -> pushes to developer branch -> 
other teammate reviews and approves -> 
Merge into developer branch -> 
delete feature of the day branch -> 
merge into main branch

- Will you be using a PR review workflow? If so, consider:

Yes

  - How many people must review a PR?
  
  1 other teammate
  
  - Who merges PRs?
  
  Reviewer
  
  - How often will you merge?
  
  At least once a day, or when a feature is complete
  
  - How will you communicate that it’s time to merge?
  
  We will communicate through Slack and Remo

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
