import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE, YELLOW
from checkers.game import Game
from minimax.algorithm import minimax
from checkers.menu import show_menu
from checkers.stopwatch import Stopwatch

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def show_winner(win, winner):
    font = pygame.font.SysFont('Arial', 60)
    if winner == RED:
        text = font.render('Red has won!', True, YELLOW)
    else:
        text = font.render('White has won!', True, YELLOW)
    
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()

    # Wait for a few seconds or until the user closes the window
    pygame.time.delay(3000)

# Show menu and get game mode and difficulty
menu_result = show_menu(WIN)
if menu_result is None:
    pygame.quit()
    exit()

game_mode, difficulty = menu_result

if difficulty == 'easy':
    depth = 1
elif difficulty == 'medium':
    depth = 3
elif difficulty == 'hard':
    depth = 6
    
stopwatch = Stopwatch()


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    winner = None
    stopwatch.start()

    while run:
        clock.tick(FPS)
        
        if winner is None:
            if game_mode == 'ai_vs_ai':
                if game.turn == WHITE:   
                    value, new_board = minimax(game.get_board(), 5, True, game)
                    game.ai_move(new_board)
                elif game.turn == RED:
                    value, new_board = minimax(game.get_board(), 3, False, game)
                    game.ai_move(new_board)
            elif game_mode == 'player_vs_ai':
                if game.turn == WHITE:
                    value, new_board = minimax(game.get_board(), depth, True, game)
                    game.ai_move(new_board)
                elif game.turn == RED:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            pos = pygame.mouse.get_pos()
                            row, col = get_row_col_from_mouse(pos)
                            game.select(row, col)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        game.update()
        
        if not game.has_valid_moves():
            winner = WHITE if game.turn == RED else RED
            show_winner(WIN, winner)
            run = False

        winner = game.winner()
        if winner is not None:
            show_winner(WIN, winner)
            run = False
    
    pygame.quit()

main()
