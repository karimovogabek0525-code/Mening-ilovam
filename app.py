import pygame
import sys
import random

# Pygame ishga tushirish
pygame.init()

# Ekran o'lchami
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1-Ilovam — Ball Game")

# Ranglar
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
GREEN = (50, 200, 100)
BLACK = (0, 0, 0)

# Ball sozlamalari (o'yinchi)
player_radius = 20
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Yashil to'plar (ball)
coins = []
for _ in range(5):
    x = random.randint(30, WIDTH - 30)
    y = random.randint(30, HEIGHT - 30)
    coins.append(pygame.Rect(x, y, 15, 15))

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# FPS
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tugmalarni boshqarish
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ekrandan chiqmaslik
    player_x = max(player_radius, min(WIDTH - player_radius, player_x))
    player_y = max(player_radius, min(HEIGHT - player_radius, player_y))

    # To'plarni tekshirish (collision)
    player_rect = pygame.Rect(player_x - player_radius, player_y - player_radius, player_radius*2, player_radius*2)
    for coin in coins[:]:
        if player_rect.colliderect(coin):
            coins.remove(coin)
            score += 1
            # Yangi coin qo'shish
            x = random.randint(30, WIDTH - 30)
            y = random.randint(30, HEIGHT - 30)
            coins.append(pygame.Rect(x, y, 15, 15))

    # Chizish
    screen.fill(WHITE)
    # O'yinchi (ko'k to'p)
    pygame.draw.circle(screen, BLUE, (player_x, player_y), player_radius)
    # Yashil to'plar
    for coin in coins:
        pygame.draw.rect(screen, GREEN, coin)
    # Score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
