# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0,5,157)
LIGHT_GREEN = (111,255,109)
GREEN = (0, 255, 0)
DARK_GREEN = (0,102,2)
LIGHT_RED = (255, 111, 97)
RED = (255, 0, 0)
DARK_RED = (137, 2, 0)
LIGHT_CYAN = (0, 255, 255)
CYAN = (0, 133, 244)
DARK_CYAN = (0,65,132)
GREENISH_YELLOW = (181,255,14)
YELLOW = (255, 255, 0)
DARK_YELLOW = (168, 165, 0)
ORANGE = (255, 116, 3)
DARK_ORANGE = (143, 64, 0 )
PURPLE = (117, 0, 244)
DARK_PURPLE = (64, 0, 113)
PINK = (240, 0, 236)
DARK_PINK = (168, 0, 166)
BROWN = (150, 75, 0)
LIGHT_GRAY = (210, 210, 210)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

pygame.init()


janela = pygame.display.set_mode((700,650))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((WHITE))

    # desenhando na superfície
    pygame.draw.rect(janela, RED, [20, 20, 50, 100])
    pygame.draw.rect(janela, CYAN, [120, 20, 50, 100])
    pygame.draw.rect(janela, GREEN, [220, 20, 50, 100])
    pygame.draw.rect(janela, DARK_YELLOW, [320, 20, 50, 100])
    pygame.draw.rect(janela, ORANGE, [420, 20, 50, 100])
    pygame.draw.rect(janela, LIGHT_GRAY, [520, 20, 50, 100])
    pygame.draw.rect(janela, BLUE, [620, 20, 50, 100])
    pygame.draw.rect(janela, GREENISH_YELLOW, [20, 150, 50, 100])
    pygame.draw.rect(janela, DARK_CYAN, [120, 150, 50, 100])
    pygame.draw.rect(janela, LIGHT_CYAN, [220, 150, 50, 100])
    pygame.draw.rect(janela, PINK, [320, 150, 50, 100])
    pygame.draw.rect(janela, GRAY, [420, 150, 50, 100])
    pygame.draw.rect(janela, LIGHT_GREEN, [520, 150, 50, 100])
    pygame.draw.rect(janela, PURPLE, [620, 150, 50, 100])
    pygame.draw.rect(janela, DARK_ORANGE, [20, 280, 50, 100])
    pygame.draw.rect(janela, DARK_GRAY, [120, 280, 50, 100])
    pygame.draw.rect(janela, DARK_PINK, [220, 280, 50, 100])
    pygame.draw.rect(janela, DARK_GREEN, [320, 280, 50, 100])
    pygame.draw.rect(janela, DARK_RED, [420, 280, 50, 100])
    pygame.draw.rect(janela, DARK_PURPLE, [520, 280, 50, 100])
    pygame.draw.rect(janela, DARK_YELLOW, [620, 280, 50, 100])
    pygame.draw.rect(janela, LIGHT_GREEN, [20, 410, 50, 100])
    pygame.draw.rect(janela, DARK_ORANGE, [120, 410, 50, 100])
    pygame.draw.rect(janela, BLACK, [220, 410, 50, 100])
    pygame.draw.rect(janela, DARK_BLUE, [320, 410, 50, 100])
    pygame.draw.rect(janela, DARK_GRAY, [420, 410, 50, 100])
    pygame.draw.rect(janela, GREEN, [520, 410, 50, 100])
    pygame.draw.rect(janela, GRAY, [620, 410, 50, 100])
    pygame.draw.rect(janela, LIGHT_RED, [20, 540, 50, 100])
    pygame.draw.rect(janela, BROWN, [120, 540, 50, 100])
    pygame.draw.rect(janela, GREENISH_YELLOW, [220, 540, 50, 100])
    pygame.draw.rect(janela, LIGHT_GRAY, [320, 540, 50, 100])
    pygame.draw.rect(janela, CYAN, [420, 540, 50, 100])
    pygame.draw.rect(janela, PURPLE, [520, 540, 50, 100])
    pygame.draw.rect(janela, ORANGE, [620, 540, 50, 100])

    pygame.display.flip()






