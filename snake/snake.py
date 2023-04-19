import pygame, sys, time, random

SIZE = 40
BACKGROUND = (96, 108, 56)


class Apple:
    def __init__(self, parent_screen):
        self.apple_image = pygame.image.load("arcade/assets/apple.jpeg")
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.parent_screen.blit(self.apple_image, (self.x, self.y))
        pygame.display.update()

    def move(self):
        self.x = random.randint(0, 24)*SIZE
        self.y = random.randint(0, 19)*SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("arcade/assets/block.jpeg")
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'

    def draw(self):
        self.parent_screen.fill(BACKGROUND)
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.update()

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'


class Game:
    def __init__(self):
        pygame.init()
        self.background_color = (96, 108, 56)
        self.screen_width = 1000
        self.screen_height = 800
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.snake = Snake(self.screen, 1)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()
        pygame.display.set_caption("Snake")

    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True

        return False
    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(score, (800, 10))

    def show_game_over(self):
        self.screen.fill(BACKGROUND)
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is Over: Your score is {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(line1, (200, 300))
        line2 = font.render(f"To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        self.screen.blit(line2, (200, 350))
        pygame.display.update()

    def play(self):
        self.screen.fill(self.background_color)
        self.snake.draw()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        time.sleep(0.2)
        self.clock.tick(60)
        pygame.display.update()

        # snake colliding with apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # snake colliding with itself
        for i in range(1, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise Exception("Game Over")



    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def run(self):
        running = True
        pause = False
        while running:
            # Handling input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == pygame.K_UP:
                            self.snake.move_up()
                        if event.key == pygame.K_DOWN:
                            self.snake.move_down()
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()


# Updating the window
if __name__ == '__main__':
    game = Game()
    game.run()
