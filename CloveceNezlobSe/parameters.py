import pygame

width = 600
height = 600

dice_size = 80


class Colors:
    dark_grey = (141, 141, 141)
    light_grey = (211, 211, 211)
    green = (47, 230, 23)
    red = (232, 18, 18)
    yellow = (237, 234, 4)
    blue = (13, 64, 216)
    white = (255, 255, 255)


def get_dice_images():
    images = []
    for i in range(1, 7):
        image = pygame.image.load(f"resources/dice/dice{i}.png")
        image = pygame.transform.scale(image, (dice_size, dice_size))
        images.append(image)
    return images


dice_images = get_dice_images()
