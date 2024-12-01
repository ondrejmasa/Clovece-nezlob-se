import pygame.mixer

from board import Board
from figure import *
from dice import Dice
from text import Text
from parameters import *
from button import Button


class Game:
    def __init__(self):
        self.board = Board()
        self.dice = Dice()
        self.button2 = Button(100, 100, pygame.image.load("resources/buttons/2players.png"))
        self.button3 = Button(100, 250, pygame.image.load("resources/buttons/3players.png"))
        self.button4 = Button(100, 400, pygame.image.load("resources/buttons/4players.png"))
        self.yellow = [Yellow(i+1) for i in range(4)]
        self.blue = [Blue(i+1) for i in range(4)]
        self.red = [Red(i+1) for i in range(4)]
        self.green = [Green(i+1) for i in range(4)]
        self.figures = [self.yellow, self.blue, self.red, self.green]
        self.turn_index = 0
        self.turn = self.figures[self.turn_index]
        self.can_throw = True
        self.winner_color = None
        self.game_over = False
        self.menu = True
        self.win_sound = pygame.mixer.Sound("resources/sounds/win.mp3")

    def move_exists(self):
        for figure in self.turn:
            if figure.can_move(self.dice.value, self.turn):
                return True
        return False

    def are_all_figures_not_playable(self):
        for figure in self.turn:
            if figure.is_playable and not figure.is_home:
                return False
        return True

    def kicked_check(self, pos):
        rest = self.figures.copy()
        rest.pop(self.turn_index)
        for color in rest:
            for figure in color:
                if figure.actual_pos == pos:
                    figure.get_kicked()

    def is_winner(self):
        for figure in self.turn:
            if not figure.is_home:
                return False
        return True

    def choose_figure_to_move(self):
        if not self.move_exists():
            if self.are_all_figures_not_playable():
                if self.dice.number_of_throws < 3:
                    self.can_throw = True
                else:
                    if not self.dice.is_rolling:
                        self.change_player()
                        self.can_throw = True
            else:
                if not self.dice.is_rolling:
                    self.change_player()
                    self.can_throw = True
        else:
            for figure in self.turn:
                if figure.is_playable and figure.is_pressed:
                    figure.move(self.dice.value)
                    self.kicked_check(figure.actual_pos)
                    for figure2 in self.turn:
                        figure2.is_home_check(self.turn)
                    if self.is_winner():
                        self.winner_color = self.turn[0].color
                        self.game_over = True
                        self.win_sound.play()
                    if self.dice.value != 6:
                        figure.is_pressed = False
                        self.change_player()
                    else:
                        figure.is_pressed = False
                    self.can_throw = True
                elif not figure.is_playable and figure.is_pressed:
                    if self.dice.value != 6:
                        figure.is_pressed = False
                        self.change_player()
                    else:
                        figure.put_into_play()
                        self.kicked_check(figure.actual_pos)
                        figure.is_pressed = False
                    self.can_throw = True

    def change_player(self):
        self.dice.number_of_throws = 0
        self.turn_index = (self.turn_index + 1) % len(self.figures)
        self.turn = self.figures[self.turn_index]

    def get_dice_value_enter(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.dice.roll_dice()
            self.can_throw = False

    def get_dice_value_click(self, mouse_pos):
        if self.dice.rect[self.dice.value].collidepoint(mouse_pos):
            self.dice.roll_dice()
            self.can_throw = False

    def throw(self):
        if self.can_throw:
            self.get_dice_value_enter()
        else:
            self.choose_figure_to_move()

    def get_color(self, color):
        colors = {"red": Colors.red, "blue": Colors.blue, "green": Colors.green, "yellow": Colors.yellow}
        return colors[color]

    def restart(self):
        self.board = Board()
        self.dice = Dice()
        self.yellow = [Yellow(i + 1) for i in range(4)]
        self.blue = [Blue(i + 1) for i in range(4)]
        self.red = [Red(i + 1) for i in range(4)]
        self.green = [Green(i + 1) for i in range(4)]
        self.figures = [self.yellow, self.blue, self.red, self.green]
        self.turn_index = 0
        self.turn = self.figures[self.turn_index]
        self.can_throw = True
        self.winner_color = None
        self.game_over = False
        self.menu = True

    def draw(self, screen):
        self.board.draw(screen)
        if self.menu:
            if self.button2.draw(screen):
                self.figures = [self.yellow, self.red]
                self.menu = False
            if self.button3.draw(screen):
                self.figures = [self.yellow, self.blue, self.red]
                self.menu = False
            if self.button4.draw(screen):
                self.figures = [self.yellow, self.blue, self.red, self.green]
                self.menu = False
        else:
            self.dice.draw(screen, self.turn[0].color)
            for figures in self.figures:
                for figure in figures:
                    figure.draw(screen)
            if self.game_over:
                text1 = Text(80, "Winner: ", Colors.light_grey, (width//2, height//2-25))
                text1.draw(screen)
                text2 = Text(80, f"{self.winner_color}", self.get_color(self.winner_color), (width//2, height//2+25))
                text2.draw(screen)
