import pygame
from solver import solve, valid

screen = pygame.display.set_mode((500, 500))
background_color = (255,255,255)
screen.fill(background_color)
pygame.display.flip()
pygame.display.set_caption('Sudoku GUI')


running = True

while running:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running = False