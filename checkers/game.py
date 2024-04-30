import pygame
from .constants import RED, WHITE, GREY, BLUE, SQUARE_SIZE
from checkers.board import Board
from checkers.stopwatch import Stopwatch

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.stopwatch = Stopwatch()
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.draw_stopwatch()
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
            
            return False
    
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            print("Time after Red player's move:", self.stopwatch.get_elapsed_time_str())
        else:
            return False

        return True
    

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
            
    def draw_stopwatch(self):
        font = pygame.font.SysFont("Arial", 30)
        
        self.stopwatch.start()
        #BUG: elapsed_time_str shows time as 00:00 but when called in main, it works fine
        elapsed_time_str = self.stopwatch.get_elapsed_time_str()

        text = font.render(f"Time: {elapsed_time_str}", True, GREY)  # Blue color
        blit_position = (10, 10)
        
        self.win.blit(text, blit_position)

        # Update the game window
        pygame.display.update()


    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
    
    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        if board is not None:
            self.board = board
        self.change_turn()
        print("Time after white player's move:", self.stopwatch.get_elapsed_time_str())
        
    def has_valid_moves(self):
        for piece in self.board.get_all_pieces(self.turn):
            if self.board.get_valid_moves(piece):
                return True
        return False
        
