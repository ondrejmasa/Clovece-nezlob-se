from pygame import gfxdraw
from parameters import *


class Board:
    def __init__(self):
        self.offset = 25
        self.outer_radius = 25
        self.inner_radius = 20
        self.x_coordinates = [250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250]
        self.y_coordinates = [50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100]

    def draw_circle(self, screen, color, pos):
        gfxdraw.aacircle(screen, pos[0], pos[1], self.outer_radius, Colors.dark_grey)
        gfxdraw.filled_circle(screen, pos[0], pos[1], self.outer_radius, Colors.dark_grey)
        gfxdraw.aacircle(screen, pos[0], pos[1], self.inner_radius, color)
        gfxdraw.filled_circle(screen, pos[0], pos[1], self.inner_radius, color)

    def draw(self, screen):
        # main path
        for x, y in zip(self.x_coordinates, self.y_coordinates):
            self.draw_circle(screen, Colors.white, (x, y))

        # finish path
        for y in range(100, 300, 50):
            self.draw_circle(screen, Colors.green, (300, y))

        for y in range(350, 550, 50):
            self.draw_circle(screen, Colors.blue, (300, y))

        for x in range(100, 300, 50):
            self.draw_circle(screen, Colors.red, (x, 300))

        for x in range(350, 550, 50):
            self.draw_circle(screen, Colors.yellow, (x, 300))

        # start
        for x in (50, 100):
            for y in (50, 100):
                self.draw_circle(screen, Colors.red, (x, y))

        for x in (500, 550):
            for y in (50, 100):
                self.draw_circle(screen, Colors.green, (x, y))

        for x in (50, 100):
            for y in (500, 550):
                self.draw_circle(screen, Colors.blue, (x, y))

        for x in (500, 550):
            for y in (500, 550):
                self.draw_circle(screen, Colors.yellow, (x, y))
