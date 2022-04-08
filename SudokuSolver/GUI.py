import pygame
import sys

from solver import solve, valid

width = 450
height = 450
rows, cols = 9,9
black = (0,0,0)
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption('Sudoku GUI')

'''
class Board:
    def __init__(self):
        self.board = [
                        [7, 8, 0, 4, 0, 0, 1, 2, 0],
                        [6, 0, 0, 0, 7, 5, 0, 0, 9],
                        [0, 0, 0, 6, 0, 1, 0, 7, 8],
                        [0, 0, 7, 0, 4, 0, 2, 6, 0],
                        [0, 0, 1, 0, 5, 0, 9, 3, 0],
                        [9, 0, 4, 0, 6, 0, 0, 0, 5],
                        [0, 7, 0, 3, 0, 0, 0, 1, 2],
                        [1, 2, 0, 0, 0, 7, 4, 0, 0],
                        [0, 4, 9, 2, 0, 6, 0, 0, 7]
                    ]
'''
def grid():
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen,black,(row*50, col*50, 50, 50), 1)

def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        grid()
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()