import pygame, sys, random, os, json
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

        self.head_up = pygame.image.load('assets/head_up.png')
        self.head_down = pygame.image.load('assets/head_down.png')
        self.head_left = pygame.image.load('assets/head_left.png')
        self.head_right = pygame.image.load('assets/head_right.png')

        self.body_bl = pygame.image.load('assets/body_bl.png')
        self.body_br = pygame.image.load('assets/body_br.png')
        self.body_tl = pygame.image.load('assets/body_tl.png')
        self.body_tr = pygame.image.load('assets/body_tr.png')

        self.body_horizontal = pygame.image.load('assets/body_horizontal.png')
        self.body_vertical = pygame.image.load('assets/body_vertical.png')

        self.tail_down = pygame.image.load('assets/tail_down.png')
        self.tail_left = pygame.image.load('assets/tail_left.png')
        self.tail_right = pygame.image.load('assets/tail_right.png')
        self.tail_up = pygame.image.load('assets/tail_up.png')

        self.crunch_sound = pygame.mixer.Sound('assets/Sound_crunch.wav')

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index -1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down


    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.current_score = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            self.current_score += 1

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            # self.show_game_over()
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                # self.show_game_over()
                self.game_over()

    def show_game_over(self):
        print("show game")
        screen.fill(BACKGROUND)
        line0 = game_font.render("High Scores", True, (255, 255, 255))
        screen.blit(line0, (200, 150))

        top1 = game_font.render(main_game.get_top_scores()[0], True, (255, 255, 255))
        screen.blit(top1, (200, 200))
        top2 = game_font.render(main_game.get_top_scores()[1], True, (255, 255, 255))
        screen.blit(top2, (200, 250))
        top3 = game_font.render(main_game.get_top_scores()[2], True, (255, 255, 255))
        screen.blit(top3, (200, 300))
        top4 = game_font.render(main_game.get_top_scores()[3], True, (255, 255, 255))
        screen.blit(top4, (200, 350))
        top5 = game_font.render(main_game.get_top_scores()[4], True, (255, 255, 255))
        screen.blit(top5, (200, 400))
        line2 = game_font.render(f"Game is Over: Your score is {self.current_score}", True, (255, 255, 255))
        screen.blit(line2, (200, 450))
        line3 = game_font.render(f"To play again press Enter. To exit press Escape!", True, (255, 255, 255))
        screen.blit(line3, (200, 500))




        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    main_game.current_score = 0
                    return

    def draw_player_name(self):
        player_name = ''
        name_font = pygame.font.Font(None, 40)
        name_text = name_font.render('Enter your name:', True, (255, 255, 255))
        name_rect = name_text.get_rect(center=(800 // 2, 800 // 2))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Player has entered their name
                        self.add_high_score(player_name, self.current_score)
                        print("HERE")
                        return "end"
                    if event.key == pygame.K_TAB:
                        print("TAB")
                        self.show_game_over()
                    elif event.key == pygame.K_BACKSPACE:
                        # Remove last character from player's name
                        player_name = player_name[:-1]

                    else:
                        # Add typed character to player's name
                        player_name += event.unicode

            # Draw the name prompt and the player's name
            screen.fill((0, 0, 0))
            screen.blit(name_text, name_rect)
            player_name_text = name_font.render(player_name, True, (255, 255, 255))
            player_name_rect = player_name_text.get_rect(center=(800 // 2, 800 // 2 + 50))
            screen.blit(player_name_text, player_name_rect)
            pygame.display.update()

    def add_high_score(self, player_name, current_score):
        high_scores = []
        if os.path.exists('high_scores.json'):
            with open('high_scores.json', 'r') as file:
                high_scores = json.load(file)

        high_scores.append({'name': player_name, 'score': self.current_score})
        high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)

        with open('high_scores.json', 'w') as file:
            json.dump(high_scores, file, indent=4)


    def get_top_scores(self):
        high_scores = []
        if os.path.exists('high_scores.json'):
            with open('high_scores.json', 'r') as file:
                high_scores = json.load(file)

        high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)[:5]

        result = []
        for i, score in enumerate(high_scores):
            result.append(f"{i + 1}. {score['name']}: {score['score']}")

        return result




    def game_over(self):
        global pause
        pause = True
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167, 209, 61)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61),bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
BACKGROUND = (96, 108, 56)
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('assets/apple.png')
game_font = pygame.font.Font('assets/PoetsenOne-Regular.ttf', 25)
pause = False
running = True
pause2 = False
game_over = False
main_game = MAIN()
current_score = 0

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pause is False:
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RETURN:
                    running = True
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)

            screen.fill((175, 215, 70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)
        elif pause is True:
            end_me = main_game.draw_player_name()
            if end_me == "end":
                pause = False
                pause2 = True
                if pause2 is True:
                    main_game.show_game_over()
                    main_game.get_top_scores()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pause2 = False
                        if event.key == pygame.K_ESCAPE:
                            running = False

if __name__ == '__main__':
    MAIN()
