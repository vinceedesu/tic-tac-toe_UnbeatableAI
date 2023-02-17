# source >>> https://www.youtube.com/watch?v=Bk9hlNZc6sE

import sys
import pygame
import constants
import numpy as np 
import random
import copy

from constants import *

# initialize pygame


pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BG_Color )


class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0
        
    def final_state(self):
        """
            @return 0 if no win yet
            @return 1 if player 1 win
            @return 2 if player 2 win
        """
        
        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]
        
        #horizontal wins 
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]
        
        #diag  decs win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            return self.squares[1][1]
        
        #diag asc win 
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            return self.squares[1][1]
        
        #no win yet
        return 0
    
    def markSquare(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1
        
    def emptySquare(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.emptySquare(row, col):
                    empty_sqrs.append( (row, col) )

        return empty_sqrs
    
    def isFull(self):
        return self.marked_sqrs == 9
    
    def isempty(self):
        return self.marked_sqrs == 0
    
class AI:
    def __init__(self, level=1, player = 2):
        self.level =level
        self.player = player
        
    def rnd(self, board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0, len(empty_sqrs))
        
        return empty_sqrs[idx]
    
    def minimax(self, board, maximizing):
        #terminal cases
        case = board.final_state()
        
        #player 1 win
        if case == 1:
            return 1, None
        
        #player 2 win
        if case == 2:
            return -1, None
        
        #draw
        elif board.isFull():
            return 0, None
        
        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()
            
            for (row, col) in empty_sqrs:
                temp_board =  copy.deepcopy(board)
                temp_board.markSquare(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
                    
            return max_eval, best_move
        
        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()
            
            for (row, col) in empty_sqrs:
                temp_board =  copy.deepcopy(board)
                temp_board.markSquare(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
                    
            return min_eval, best_move
        
        
    
    def eval(self, main_board):
        if self.level == 0:
            eval =  'random'
            move = self.rnd(main_board)
        else:
            # minimax algo
            eval, move = self.minimax(main_board, False)
        print(f'AI chose to mark the square in pos {move} with an eval of {eval}')
        return move
class Game:
    
    def __init__(self): 
        self.board = Board()
        self.ai = AI()
        self.player = 1 #1- cross #2- circle
        self.gamemode = 'ai'
        self.running = True
        self.show_lines()

    def show_lines(self):
        #vertical lines
        pygame.draw.line(screen,line_Color,(SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), line_WIDTH)
        pygame.draw.line(screen,line_Color,(WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), line_WIDTH)
        
        # horizontal lines
        pygame.draw.line(screen,line_Color,(0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), line_WIDTH)
        pygame.draw.line(screen,line_Color,(0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT - SQUARE_SIZE), line_WIDTH)
        
    def next_player(self):
        self.player = self.player % 2 + 1
        
    def draw_fig(self, row, col):
        if self.player == 1:
            #draw cross
            startDecs = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            endDecs = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            pygame.draw.line(screen, cross_color, startDecs, endDecs, cross_width)
            
            #draw decline
            startAsc = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            endAsc = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET)
            pygame.draw.line(screen, cross_color, startAsc, endAsc, cross_width)
        
        elif self.player == 2:
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE// 2)
            pygame.draw.circle(screen, circle_color, center, Radius, circle_width)
        

# main function
def main():
    
    game = Game()
    ai = game.ai
    board = game.board
    # mainLoop game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:   
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                
                # code for not filling not empty cells
                if board.emptySquare(row,col):
                    board.markSquare(row, col, game.player)
                    game.draw_fig(row, col)
                    
                    game.next_player()

            if game.gamemode == 'ai' and game.player == ai.player:
                pygame.display.update()
                
                row, col = ai.eval(board)
                board.markSquare(row, col, ai.player)
                game.draw_fig(row, col)
                
                game.next_player()
                
        
        pygame.display.update()

main()