import pygame
from checkers.stopwatch import Stopwatch

# define colors using RGB values
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (90, 90, 90)


# define the window dimensions
WIDTH = 800
HEIGHT = 600

# Initialize the stopwatch
stopwatch = Stopwatch()

def show_menu(win):
    """
   displays the main menu for selecting difficulty level.
   Arguments: win (pygame.Surface): the game window surface where the menu is displayed.
   Returns: str or None: returns the selected difficulty as a string ('easy', 'medium', 'hard'). returns None if the window is closed.
   """
    pygame.font.init()  # initialize the font
    font = pygame.font.SysFont('Arial', 40)  # main font for the menu text
    small_font = pygame.font.SysFont('Arial', 30)  # font for the selected text

    run = True  # flag to keep the menu running
    selected_difficulty = None  # variable to store the selected difficulty
    game_mode = None  # variable to store the selected game mode
    mode_selected = False

    # defines button properties
    button_width, button_height = 220, 50
    button_y = HEIGHT // 2
    
    ai_vs_ai_button = pygame.Rect(WIDTH // 2 - button_width // 2, button_y - 30, button_width, button_height)
    player_vs_ai_button = pygame.Rect(WIDTH // 2 - button_width // 2, button_y + 30, button_width, button_height)
    
    easy_button = pygame.Rect(WIDTH // 2 - button_width // 2, button_y - 60, button_width, button_height)
    medium_button = pygame.Rect(WIDTH // 2 - button_width // 2, button_y, button_width, button_height)
    hard_button = pygame.Rect(WIDTH // 2 - button_width // 2, button_y + 60, button_width, button_height)

    while run:
         # fill the window with a dark grey color [change later]
        win.fill(BLACK)
        
        if not mode_selected:
            # shows the main menu text
            title_text = font.render('Select Game Mode:', True, WHITE)
            win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

            # make the buttons for game mode
            pygame.draw.rect(win, RED if game_mode == 'ai_vs_ai' else GREY, ai_vs_ai_button)
            pygame.draw.rect(win, RED if game_mode == 'player_vs_ai' else GREY, player_vs_ai_button)

            # make the button texts for game mode
            ai_vs_ai_text = font.render('AI vs AI', True, WHITE)
            player_vs_ai_text = font.render('Player vs AI', True, WHITE)

            win.blit(ai_vs_ai_text, (ai_vs_ai_button.x + (ai_vs_ai_button.width - ai_vs_ai_text.get_width()) // 2, ai_vs_ai_button.y + (ai_vs_ai_button.height - ai_vs_ai_text.get_height()) // 2))
            win.blit(player_vs_ai_text, (player_vs_ai_button.x + (player_vs_ai_button.width - player_vs_ai_text.get_width()) // 2, player_vs_ai_button.y + (player_vs_ai_button.height - player_vs_ai_text.get_height()) // 2))

            if game_mode:
                mode_text = small_font.render(f'Selected Mode: {game_mode.replace("_", " ").capitalize()}', True, WHITE)
                win.blit(mode_text, (WIDTH // 2 - mode_text.get_width() // 2, HEIGHT - 80))
        else:
            # shows the difficulty selection text
            title_text = font.render('Select Difficulty:', True, WHITE)
            win.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

            # make the buttons for difficulty
            pygame.draw.rect(win, RED if selected_difficulty == 'easy' else GREY, easy_button)
            pygame.draw.rect(win, RED if selected_difficulty == 'medium' else GREY, medium_button)
            pygame.draw.rect(win, RED if selected_difficulty == 'hard' else GREY, hard_button)

            # make the button texts for difficulty
            easy_text = font.render('Easy', True, WHITE)
            medium_text = font.render('Medium', True, WHITE)
            hard_text = font.render('Hard', True, WHITE)

            win.blit(easy_text, (easy_button.x + (easy_button.width - easy_text.get_width()) // 2, easy_button.y + (easy_button.height - easy_text.get_height()) // 2))
            win.blit(medium_text, (medium_button.x + (medium_button.width - medium_text.get_width()) // 2, medium_button.y + (medium_button.height - medium_text.get_height()) // 2))
            win.blit(hard_text, (hard_button.x + (hard_button.width - hard_text.get_width()) // 2, hard_button.y + (hard_button.height - hard_text.get_height()) // 2))

            if selected_difficulty:
                diff_text = small_font.render(f'Selected Difficulty: {selected_difficulty.capitalize()}', True, WHITE)
                win.blit(diff_text, (WIDTH // 2 - diff_text.get_width() // 2, HEIGHT - 50))

        pygame.display.update()  # update the display to show changes

        # event loop to handle user inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos 

                if not mode_selected:
                    if ai_vs_ai_button.collidepoint(mouse_pos):
                        game_mode = 'ai_vs_ai'
                        mode_selected = True
                        return game_mode, None
                    elif player_vs_ai_button.collidepoint(mouse_pos):
                        game_mode = 'player_vs_ai'
                        mode_selected = True
                else:
                    if easy_button.collidepoint(mouse_pos):
                        selected_difficulty = 'easy'
                        stopwatch.start()
                    elif medium_button.collidepoint(mouse_pos):
                        selected_difficulty = 'medium'
                        stopwatch.start()
                    elif hard_button.collidepoint(mouse_pos):
                        selected_difficulty = 'hard'
                        stopwatch.start()
                    
                   
                    if selected_difficulty:
                        return game_mode, selected_difficulty
