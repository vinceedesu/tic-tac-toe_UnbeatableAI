# source >>> https://www.youtube.com/watch?v=Bk9hlNZc6sE

import sys
import pygame
import constants

from constants import *

# initialize pygame


pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Tic Tac Toe')
screen.fill( BG_Color )


class Game:
    
    def __init__(self): 
        self.show_lines()

    def show_lines(self):
        #vertical lines
        pygame.draw.line(screen,line_Color,(SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), line_WIDTH)
        pygame.draw.line(screen,line_Color,(SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), line_WIDTH)
        
        # horizontal lines
        pygame.draw.line(screen,line_Color,(SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), line_WIDTH)
        pygame.draw.line(screen,line_Color,(SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), line_WIDTH)

# main function
def main():
    
    game = Game()
     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

main()