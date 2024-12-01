import pygame


class Figure:
    def __init__(self):
        self.is_playable = False
        self.is_home = False
        self.x_coordinates = []
        self.y_coordinates = []
        self.spawn_pos = None
        self.actual_pos = None
        self.positions = []
        self.position_index = 0
        self.rect = None
        self.is_pressed = False
        self.jump_sound = pygame.mixer.Sound("resources/sounds/jump.mp3")

    def put_into_play(self):
        self.actual_pos = self.positions[0]
        self.is_playable = True

    def move(self, value):
        self.position_index += value
        self.actual_pos = self.positions[self.position_index]

    def get_kicked(self):
        self.jump_sound.play()
        self.position_index = 0
        self.actual_pos = self.spawn_pos
        self.is_playable = False

    def is_home_check(self, turn):
        if self.position_index > 39:
            rest_spaces = 43 - self.position_index
            rest_positions = [self.positions[i] for i in range(43, self.position_index, -1)]
            for figure in turn:
                if figure.actual_pos in rest_positions:
                    rest_spaces -= 1
            self.is_home = rest_spaces == 0

    def can_move(self, dice_value, turn):
        if self.is_home:
            return False
        elif not self.is_playable and dice_value != 6:
            return False
        elif self.position_index + dice_value > 43:
            return False
        for figure in turn:
            if self.is_playable and figure.actual_pos == self.positions[self.position_index + dice_value]:
                return False
            elif not self.is_playable and figure.actual_pos == self.positions[0]:
                return False
        return True

    def pressed_check(self, mouse_pos, dice_value, turn):
        if self.can_move(dice_value, turn) and self.rect.collidepoint(mouse_pos):
            self.is_pressed = True


class Yellow(Figure):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.image = pygame.transform.scale(pygame.image.load("resources/figures/yellow.png"), (40, 40))
        self.spawn_pos = self.get_spawn_pos()
        self.x_coordinates = [550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 500, 450, 400, 350]
        self.y_coordinates = [350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300]
        self.positions = list(zip(self.x_coordinates, self.y_coordinates))
        self.actual_pos = self.spawn_pos
        self.rect = self.image.get_rect(center=self.actual_pos)
        self.color = "yellow"

    def get_spawn_pos(self):
        if self.id == 1:
            spawn = (500, 500)
        elif self.id == 2:
            spawn = (550, 500)
        elif self.id == 3:
            spawn = (500, 550)
        else:
            spawn = (550, 550)
        return spawn

    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.actual_pos)
        screen.blit(self.image, self.rect)


class Blue(Figure):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.image = pygame.transform.scale(pygame.image.load("resources/figures/blue.png"), (40, 40))
        self.spawn_pos = self.get_spawn_pos()
        self.x_coordinates = [250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 300, 300, 300, 300]
        self.y_coordinates = [550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 500, 450, 400, 350]
        self.positions = list(zip(self.x_coordinates, self.y_coordinates))
        self.actual_pos = self.spawn_pos
        self.rect = self.image.get_rect(center=self.actual_pos)
        self.color = "blue"

    def get_spawn_pos(self):
        if self.id == 1:
            spawn = (50, 500)
        elif self.id == 2:
            spawn = (100, 500)
        elif self.id == 3:
            spawn = (50, 550)
        else:
            spawn = (100, 550)
        return spawn

    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.actual_pos)
        screen.blit(self.image, self.rect)


class Red(Figure):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.image = pygame.transform.scale(pygame.image.load("resources/figures/red.png"), (40, 40))
        self.spawn_pos = self.get_spawn_pos()
        self.x_coordinates = [50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 100, 150, 200, 250]
        self.y_coordinates = [250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 300, 300, 300, 300]
        self.positions = list(zip(self.x_coordinates, self.y_coordinates))
        self.actual_pos = self.spawn_pos
        self.rect = self.image.get_rect(center=self.actual_pos)
        self.color = "red"

    def get_spawn_pos(self):
        if self.id == 1:
            spawn = (50, 50)
        elif self.id == 2:
            spawn = (100, 50)
        elif self.id == 3:
            spawn = (50, 100)
        else:
            spawn = (100, 100)
        return spawn

    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.actual_pos)
        screen.blit(self.image, self.rect)


class Green(Figure):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.image = pygame.transform.scale(pygame.image.load("resources/figures/green.png"), (40, 40))
        self.spawn_pos = self.get_spawn_pos()
        self.x_coordinates = [350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 300, 300, 300, 300]
        self.y_coordinates = [50, 100, 150, 200, 250, 250, 250, 250, 250, 300, 350, 350, 350, 350, 350, 400, 450, 500, 550, 550, 550, 500, 450, 400, 350, 350, 350, 350, 350, 300, 250, 250, 250, 250, 250, 200, 150, 100, 50, 50, 100, 150, 200, 250]
        self.positions = list(zip(self.x_coordinates, self.y_coordinates))
        self.actual_pos = self.spawn_pos
        self.rect = self.image.get_rect(center=self.actual_pos)
        self.color = "green"

    def get_spawn_pos(self):
        if self.id == 1:
            spawn = (500, 50)
        elif self.id == 2:
            spawn = (550, 50)
        elif self.id == 3:
            spawn = (500, 100)
        else:
            spawn = (550, 100)
        return spawn

    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.actual_pos)
        screen.blit(self.image, self.rect)
