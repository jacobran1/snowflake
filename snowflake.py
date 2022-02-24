import pygame
pygame.display.set_caption("Снежинка")
COLOR = (27, 152, 247)


def draw():
    #
    pygame.draw.rect(screen, COLOR, (390, 40, 20, 720))
    pygame.draw.rect(screen, COLOR, (40, 390, 720, 20))
    pygame.draw.circle(screen, COLOR, (400, 40), 10)
    pygame.draw.circle(screen, COLOR, (400, 760), 10)
    pygame.draw.circle(screen, COLOR, (40, 400), 10)
    pygame.draw.circle(screen, COLOR, (760, 400), 10)
    #
    pygame.draw.line(screen, COLOR, [50, 750], [750, 50], 22)
    pygame.draw.line(screen, COLOR, [50, 50], [750, 750], 22)
    #
    pygame.draw.line(screen, COLOR, [400, 130], [490, 40], 22)
    pygame.draw.line(screen, COLOR, [400, 130], [310, 40], 22)
    pygame.draw.line(screen, COLOR, [400, 670], [490, 760], 22)
    pygame.draw.line(screen, COLOR, [400, 670], [310, 760], 22)
    pygame.draw.line(screen, COLOR, [130, 400], [40, 310], 22)
    pygame.draw.line(screen, COLOR, [130, 400], [40, 490], 22)
    pygame.draw.line(screen, COLOR, [670, 400], [760, 310], 22)
    pygame.draw.line(screen, COLOR, [670, 400], [760, 490], 22)
    #
    pygame.draw.line(screen, COLOR, [130, 130], [130, 40], 18)
    pygame.draw.line(screen, COLOR, [130, 130], [40, 130], 18)
    pygame.draw.line(screen, COLOR, [670, 130], [670, 40], 18)
    pygame.draw.line(screen, COLOR, [670, 130], [760, 130], 18)
    pygame.draw.line(screen, COLOR, [130, 670], [40, 670], 18)
    pygame.draw.line(screen, COLOR, [130, 670], [130, 760], 18)
    pygame.draw.line(screen, COLOR, [670, 670], [760, 670], 18)
    pygame.draw.line(screen, COLOR, [670, 670], [670, 760], 18)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    draw()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
