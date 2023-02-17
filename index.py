# source >>> https://www.youtube.com/watch?v=Bk9hlNZc6sE

import sys
import pygame
import constants
import numpy as np 

from constants import *

# initialize pygame


pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BG_Color )


class Board:
    
    def __init__(self):
        self.squares = np.zeros( (ROWS, COLS) )
        
    
    def markSquare(self, row, col, player):
        self.squares[row][col] = player
        
    def emptySquare(self, row, col):
        return self.squares[row][col] == 0



class Game:
    
    def __init__(self): 
        self.board = Board()
        self.player = 1 #1- cross #2- circle
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

        
        
        pygame.display.update()

main()