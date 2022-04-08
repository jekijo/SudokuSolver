import pygame
import sys

from solver import solve, valid

width = 550
height = 550
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
    for i in range(0,10):
        if (i == 0) or (i % 3 == 0):
            pygame.draw.line(screen, black, (50+50*i, 50), (50+50*i, 500), 2)
            pygame.draw.line(screen, black, (50, 50+50*i), (500, 50+50*i), 2)
        else:
            pygame.draw.line(screen, black, (50+50*i, 50), (50+50*i, 500), 1)
            pygame.draw.line(screen, black, (50, 50+50*i), (500, 50+50*i), 1)
            

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