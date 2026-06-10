import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 500, 640
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

BG_COLOR = (245, 248, 255)
LINE_COLOR = (50, 50, 50)
X_COLOR = (220, 20, 60)
O_COLOR = (30, 144, 255)
TEXT_COLOR = (40, 40, 40)
BTN_COLOR = (0, 170, 170)

FONT_LARGE = pygame.font.SysFont("segoeui", 72, bold=True)
FONT_MED = pygame.font.SysFont("segoeui", 30, bold=True)
FONT_SMALL = pygame.font.SysFont("segoeui", 20)

BOARD = [str(i) for i in range(1, 10)]
CELL_SIZE = WIDTH // 3
GAME_OVER = False
WINNER = None

PLAYER_SCORE = 0
AI_SCORE = 0 
DRAW_SCORE = 0 

def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(WIN, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 3)
        pygame.draw.line(WIN, LINE_COLOR, (i * CELL_SIZE,0), (i * CELL_SIZE, WIDTH), 3)

def draw_marks():
    for i in range(9):
        row = i // 3 
        col = i % 3
        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2
        if BOARD[i] == "X":
            text = FONT_LARGE.render("X", True, X_COLOR)
            WIN.blit(text, text.get_rect(center=(x, y)))
        elif BOARD[i] == "O":
            text = FONT_LARGE.render("O", True, O_COLOR)
            WIN.blit(text, text.get_rect(center=(x, y)))

def display_status():
    rect = pygame.Rect(0, WIDTH, WIDTH, HEIGHT - WIDTH)
    pygame.draw.rect(WIN, (230, 235, 245), rect)

    score_text = FONT_SMALL.render(
        f"Player: {PLAYER_SCORE}      AI {AI_SCORE}   DRAW: {DRAW_SCORE}",
        True, TEXT_COLOR
    )


    WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, WIDTH + 10))

    status_text = FONT_MED.render(WINNER if WINNER else "your turn", True, TEXT_COLOR) 
    WIN.blit(status_text, (WIDTH // 2 - 90, WIDTH + 85, 180, 45))
    
    btn = pygame.Rect(WIDTH // 2 - 90, WIDTH + 85, 180, 45)
    pygame.draw.rect(WIN, BTN_COLOR, btn, border_radius=8)
    txt = FONT_SMALL.render("Restart", True, (255, 255, 255))
    WIN.blit(txt, txt.get_rect(center=btn.center))


    return btn



def check_win(symbol):
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(BOARD[a] == BOARD[b] == BOARD[c] == symbol for a,b,c in combos)

def check_full():
    return all(not cell.isdigit() for cell in BOARD)


def ai_move():
    for i in range(9):
        if BOARD[i].isdigit():
            temp = BOARD.copy()
            temp[i] = "O"
            if check_virtual_win(temp, "O"):
                BOARD[i] = "O"
                return
            
    for i in range(9):
        if BOARD[i].isdigit():
            temp = BOARD.copy()
            temp[i] = "X"
            if check_virtual_win(temp, "X"):
                BOARD[i] = "O"
                return
            
    choices = [i for i in range(9) if BOARD[i].isdigit()]
    BOARD[random.choice(choices)] = "O"

def check_virtual_win(board, symbol):
    combos = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a] == board[b] == board[c] == symbol for a,b,c in combos)

def reset_game():
    global BOARD, GAME_OVER, WINNER
    BOARD = [str(i) for i in range(1, 10)]
    GAME_OVER = False
    WINNER = None


def reset_game():
    global BOARD, GAME_OVER, WINNER
    BOARD = [str(i) for i in range(1, 10)]
    GAME_OVER = False
    WINNER = None


def get_cell(pos):
    x, y = pos
    if y >= WIDTH:
        return None
    col = x // CELL_SIZE
    row = y // CELL_SIZE
    return row * 3 + col

clock = pygame.time.Clock()
run = True


while run:
    clock.tick(60)
    WIN.fill(BG_COLOR)
    draw_grid()
    draw_marks()
    restart_btn = display_status()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()


            if restart_btn.collidepoint(pos):
                reset_game()

            if not GAME_OVER:
                idx = get_cell(pos)
                if idx is not None and BOARD[idx].isdigit():
                    BOARD[idx] = "X"

                    if check_win("X"):
                        GAME_OVER = True
                        WINNER = "You win!!"
                        PLAYER_SCORE += 1

                    elif check_full():
                        GAME_OVER = True
                        WINNER = "Draw"
                        DRAW_SCORE += 1
                    
                    else:
                        ai_move()

                        if check_win("O"):
                            GAME_OVER = True
                            WINNER = "AI wins!!"
                            AI_SCORE += 1

                        elif check_full():
                            GAME_OVER = True
                            WINNER = "Draw"
                            DRAW_SCORE += 1
    
    pygame.display.update()

pygame.quit()
sys.exit()

            

    
                        


                        
                    




















            
                    


            
    


        
        
