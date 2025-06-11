import pygame

# Inicializa o pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 400, 400
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Toggle Game")

# Cores
WHITE = (255, 255, 255)
BLACK = (255, 0, 0)
GREEN = (0, 255, 0)

# Estado do tabuleiro (False = apagado, True = aceso)
board = [[False for _ in range(COLS)] for _ in range(ROWS)]

def draw_board():
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = GREEN if board[row][col] else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)

def toggle_cell(row, col):
    board[row][col] = not board[row][col]

def check_win():
    return all(all(row) for row in board)

# Loop do jogo
running = True
while running:
    draw_board()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // CELL_SIZE, x // CELL_SIZE
            toggle_cell(row, col)
            if check_win():
                print("Você venceu!")
                running = False

pygame.quit()