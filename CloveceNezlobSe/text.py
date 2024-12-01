import pygame


class Text:
    def __init__(self, size, text, color, position):
        self.size = size
        self.text = text
        self.color = color
        self.position = position
        self.font = pygame.font.Font(None, size)

    def draw(self, screen):
        surface = self.font.render(self.text, True, self.color)
        bg = self.font.render(self.text, True, "black")
        rect = surface.get_rect(center=self.position)
        temp = tuple([i+1 for i in self.position])
        bg_rect = bg.get_rect(center=temp)
        screen.blit(bg, bg_rect)
        screen.blit(surface, rect)