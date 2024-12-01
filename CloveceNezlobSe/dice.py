import random

import pygame.mixer

from parameters import *


class Dice:
    def __init__(self):
        self.images = {i: image for i, image in enumerate(dice_images, start=1)}
        self.positions = {"red": (135, 135), "green": (385, 135), "blue": (135, 385), "yellow": (385, 385)}
        self.value = 1
        self.is_rolling = False
        self.rolling_image_counter = 0
        self.number_of_throws = 0
        self.rect = self.get_rect("yellow")
        self.dice_sound = pygame.mixer.Sound("resources/sounds/dice.mp3")

    def roll_dice(self):
        self.is_rolling = True
        self.value = random.randint(1, 6)
        self.number_of_throws += 1
        self.dice_sound.play()

    def pressed_check(self, mouse_pos):
        if self.rect[self.value].collidepoint(mouse_pos):
            self.roll_dice()

    def get_rect(self, color):
        return {i: self.images[i].get_rect(topleft=self.positions[color]) for i in range(1, len(self.images) + 1)}

    def draw(self, screen, color):
        if self.is_rolling:
            screen.blit(self.images[random.randint(1, 6)], self.positions[color])
            self.rolling_image_counter += 1
            if self.rolling_image_counter > 5:
                self.is_rolling = False
        else:
            self.rect = self.get_rect(color)
            screen.blit(self.images[self.value], self.positions[color])
            self.rolling_image_counter = 0
