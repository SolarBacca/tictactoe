import pygame
import sys


WIDTH, HEIGHT = 500, 500
ROWS, COLS = 3, 3
CELL_SIZE = WIDTH // COLS
LINE_WIDTH = 5


BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")
clock = pygame.time.Clock()


font = pygame.font.SysFont('arial', 28, bold=True)



def draw_grid():
    """Рисует сетку 3x3"""
    for row in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
    for col in range(1, COLS):
        pygame.draw.line(screen, LINE_COLOR, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT - 30), LINE_WIDTH)


def draw_marks(board):

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 'O':
                center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CELL_SIZE // 3, LINE_WIDTH)
            elif board[row][col] == 'X':

                start1 = (col * CELL_SIZE + 20, row * CELL_SIZE + 20)
                end1 = (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + CELL_SIZE - 20)
                pygame.draw.line(screen, CROSS_COLOR, start1, end1, LINE_WIDTH)

                start2 = (col * CELL_SIZE + 20, row * CELL_SIZE + CELL_SIZE - 20)
                end2 = (col * CELL_SIZE + CELL_SIZE - 20, row * CELL_SIZE + 20)
                pygame.draw.line(screen, CROSS_COLOR, start2, end2, LINE_WIDTH)


def display_message(message):

    text = font.render(message, True, TEXT_COLOR)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT - 15))
    screen.blit(text, text_rect)



def check_win(board, player):


    for row in range(ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    for col in range(COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw(board):

    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == '':
                return False
    return True


def reset_game():

    return [['' for _ in range(COLS)] for _ in range(ROWS)], 'X', False



def main():
    board, current_player, game_over = reset_game()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x, mouse_y = event.pos
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE


                if row < ROWS and col < COLS and board[row][col] == '':
                    board[row][col] = current_player

                    if check_win(board, current_player):
                        game_over = True
                    elif check_draw(board):
                        game_over = True
                    else:

                        current_player = 'O' if current_player == 'X' else 'X'


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board, current_player, game_over = reset_game()


        screen.fill(BG_COLOR)
        draw_grid()
        draw_marks(board)


        if game_over:
            if check_win(board, 'X'):
                display_message("Победили Крестики! (R - рестарт)")
            elif check_win(board, 'O'):
                display_message("Победили Нолики! (R - рестарт)")
            else:
                display_message("Ничья! (R - рестарт)")
        else:
            display_message(f"Ход игрока: {current_player}")


        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()