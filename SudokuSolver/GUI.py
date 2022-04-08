import pygame
import sys
from solver import find_empty, valid

width = 550
height = 550
rows, cols = 9,9
black = (0,0,0)
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(white)
pygame.display.set_caption('Sudoku GUI')
font = pygame.font.SysFont('Times New Roman', 20)
board = [
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

def grid():
    for i in range(0,10):
        if (i == 0) or (i % 3 == 0):
            pygame.draw.line(screen, black, (50+50*i, 50), (50+50*i, 500), 2)
            pygame.draw.line(screen, black, (50, 50+50*i), (500, 50+50*i), 2)
        else:
            pygame.draw.line(screen, black, (50+50*i, 50), (50+50*i, 500), 1)
            pygame.draw.line(screen, black, (50, 50+50*i), (500, 50+50*i), 1)

def populate(bo):
    for i in range(len(bo[0])):
        for j in range(len(bo[0])):
            if(0<bo[i][j]<10):
                val = font.render(str(bo[i][j]), True, black)
                screen.blit(val, ((j+1)*50+20, (i+1)*50+15))
    pygame.display.update()

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            val = font.render(str(bo[row][col]), True, black)
            pygame.time.wait(100)
            pygame.draw.rect(screen, white, (col*50+55, row*50+55, 40, 40))
            screen.blit(val, ((col+1)*50+20, (row+1)*50+15))
            pygame.display.update()
            if solve(bo):
                return True
            bo[row][col] = 0
            val = font.render(str(bo[row][col]), True, black)
            pygame.time.wait(100)
            screen.blit(val, ((col+1)*50+20, (row+1)*50+15))
            pygame.display.update()
    return False

            

def main():
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        grid()
        populate(board)
        pygame.time.wait(100)
        solve(board)
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()



main()
