from parameters import *
from game import Game


pygame.init()


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Člověče, nezlob se!")

FPS = 10
clock = pygame.time.Clock()

game = Game()

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            if not game.game_over:
                if not game.can_throw:
                    for figure in game.turn:
                        figure.pressed_check(event.pos, game.dice.value, game.turn)
                else:
                    game.get_dice_value_click(event.pos)
            else:
                game.restart()

    screen.fill(Colors.white)
    game.draw(screen)
    if not game.game_over:
        game.throw()
    pygame.display.update()

pygame.quit()
