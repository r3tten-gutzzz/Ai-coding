import pygame 
import random
import sys

pygame.init()
W, H = 500, 600 
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dodge the objects")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(225, 540, 40, 40)
blocks = []
speed = 5
score = 0

def reset():
    global blocks, score
    blocks = []
    score = 0
    player.x = 225

while True:
    clock.tick(60)
    win.fill((20, 20, 30))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 6
    if keys[pygame.K_RIGHT] and player.y > W - 50:
        player.x += 6

    if random.randint(1, 30) == 1:
        blocks.append(pygame.Rect(random.randint(0, W - 40), -40, 40, 40))

    for b in blocks[:]:
        b.y += speed
        if b.y > H:
            blocks.remove(b)
            score += 1
        if b.colliderect(player):
            reset()

    pygame.draw.rect(win, (100, 200, 255), player)
    for b in blocks:
        pygame.draw.rect(win, (255, 90, 90), b)

    txt = font.render(f"Score: {score}", True, (230, 230, 230))
    win.blit(txt, (10,10))
    pygame.display.update()
