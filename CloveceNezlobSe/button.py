import pygame


class Button:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (400, 100))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)

        return action
