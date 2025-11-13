import pygame as pg
import sys
from pygame.math import Vector2

pg.init()

GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24)

cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = Vector2(5,6)
    def draw(self):
        food_rect = pg.Rect(self.position.x*cell_size,self.position.y*cell_size,cell_size,cell_size )
        pg.draw.rect(screen,DARK_GREEN,food_rect)
screen = pg.display.set_mode((cell_size*number_of_cells,cell_size*number_of_cells))

pg.display.set_caption("Retro Snake")

clock = pg.time.Clock()

food =Food()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    #drawing
    screen.fill(GREEN)
    food.draw()
    pg.display.update()
    clock.tick(60)
