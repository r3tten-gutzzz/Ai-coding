import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20

COLUMNS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

CLOCK = pygame.time.Clock()


def draw_rect(pos, color):
    r = pygame.Rect(
        pos[0] * CELL_SIZE,
        pos[1] * CELL_SIZE,
        CELL_SIZE,
        CELL_SIZE
    )
    pygame.draw.rect(SCREEN, color, r)


def random_food(snake):
    while True:
        x = random.randint(0, COLUMNS - 1)
        y = random.randint(0, ROWS - 1)

        if (x, y) not in snake:
            return (x, y)


def show_text(text, size, color, center):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=center)
    SCREEN.blit(surface, rect)


def game_loop():
    snake = [(COLUMNS // 2, ROWS // 2)]
    direction = (1, 0)

    food = random_food(snake)

    score = 0
    speed = 7

    paused = False

    while True:

        # EVENTS
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # UP
                if event.key in (pygame.K_w, pygame.K_UP) and direction != (0, 1):
                    direction = (0, -1)

                # DOWN
                elif event.key in (pygame.K_s, pygame.K_DOWN) and direction != (0, -1):
                    direction = (0, 1)

                # LEFT
                elif event.key in (pygame.K_a, pygame.K_LEFT) and direction != (1, 0):
                    direction = (-1, 0)

                # RIGHT
                elif event.key in (pygame.K_d, pygame.K_RIGHT) and direction != (-1, 0):
                    direction = (1, 0)

                # PAUSE
                elif event.key == pygame.K_p:
                    paused = not paused

        # PAUSE SCREEN
        if paused:
            SCREEN.fill((0, 0, 0))

            show_text(
                "Paused - Press P to Resume",
                36,
                (255, 255, 255),
                (WIDTH // 2, HEIGHT // 2)
            )

            pygame.display.flip()
            CLOCK.tick(10)
            continue

        # MOVE SNAKE
        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        # GAME OVER
        if (
            head[0] < 0 or
            head[0] >= COLUMNS or
            head[1] < 0 or
            head[1] >= ROWS or
            head in snake
        ):

            SCREEN.fill((0, 0, 0))

            show_text(
                f"Game Over - Score: {score}",
                40,
                (255, 0, 0),
                (WIDTH // 2, HEIGHT // 2 - 20)
            )

            show_text(
                "Press R to Restart or Q to Quit",
                30,
                (255, 255, 255),
                (WIDTH // 2, HEIGHT // 2 + 30)
            )

            pygame.display.flip()

            while True:
                for e in pygame.event.get():

                    if e.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    if e.type == pygame.KEYDOWN:

                        # RESTART
                        if e.key == pygame.K_r:
                            return

                        # QUIT
                        if e.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()

                CLOCK.tick(10)

        # ADD HEAD
        snake.insert(0, head)

        # FOOD
        if head == food:
            score += 1
            food = random_food(snake)

            if score % 5 == 0:
                speed += 1
        else:
            snake.pop()

        # DRAW
        SCREEN.fill((0, 0, 0))

        draw_rect(food, (255, 0, 0))

        for i, segment in enumerate(snake):

            color = (0, 200, 0) if i == 0 else (0, 120, 0)

            draw_rect(segment, color)

        show_text(
            f"Score: {score}",
            28,
            (255, 255, 255),
            (80, 20)
        )

        pygame.display.flip()
        CLOCK.tick(speed)


if __name__ == "__main__":

    while True:
        game_loop()