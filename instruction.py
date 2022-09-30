from pygame import font

import screen
import pygame
from item import *
import objekte
import player
import screen
import language
from control_pictures import *

# Load and position Controller Pics
player_1_png_rec = player_1_png.get_rect()
player_1_png_rec.center = ((screen.W / 8), (screen.H / 2) + 200)

player_2_png_rec = player_2_png.get_rect()
player_2_png_rec.center = ((screen.W / 8) + 500, (screen.H / 2) + 200)

player_3_png_rec = player_3_png.get_rect()
player_3_png_rec.center = ((screen.W / 8) + 1000, (screen.H / 2) + 200)

player_4_png_rec = player_3_png.get_rect()
player_4_png_rec.center = ((screen.W / 8) + 1500, (screen.H / 2) + 200)

#Control
def instruction_screen_1():
    # Control
    screen.templates.textfild(None, 50, 50, 800, 80, (255, 0, 0), language.tr().M7(0), 80)  # M7 Steuerung '#TODO: tr

    # Info TEXT
    screen.templates.textfild(None, 50, 140, 1500, 80, (255, 0, 0), language.tr().M7(13), 40)  # TODO: tr ok

    # player_1
    screen.screen.blit(player_1_png, player_1_png_rec)
    pygame.draw.rect(screen.screen, (255, 0, 0), [player_1_png_rec[0] + 85, player_1_png_rec[1] - 150, 100, 100], 10)
    # player_2
    screen.screen.blit(player_2_png, player_2_png_rec)
    pygame.draw.rect(screen.screen, (0, 255, 0), [player_2_png_rec[0] + 85, player_2_png_rec[1] - 150, 100, 100], 10)
    # player_3
    screen.screen.blit(player_3_png, player_3_png_rec)
    pygame.draw.rect(screen.screen, (255, 0, 255), [player_3_png_rec[0] + 85, player_3_png_rec[1] - 150, 100, 100], 10)
    # player_4
    screen.screen.blit(player_4_png, player_4_png_rec)
    pygame.draw.rect(screen.screen, (0, 255, 255), [player_4_png_rec[0] + 85, player_4_png_rec[1] - 150, 100, 100], 10)

#Explaint points
def instruction_screen_2():
    # Pukte Stand
    screen.templates.textfild(None, 50, 50, 800, 80, (255, 0, 0), language.tr().M7(1), 80)  # TODO: tr ok
    # Info TEXT
    screen.templates.textfild(None, 50, 140, 1500, 80, (255, 0, 0), language.tr().M7(5), 40)  # TODO: tr ok
    screen.templates.textfild(None, 50, 180, 1500, 80, (255, 0, 0), language.tr().M7(6), 40)  # TODO: tr ok

    # Point and Speed View
    font = pygame.font.SysFont(None, 50)
    point_view = font.render(str(10), True, (255, 255, 255))
    screen.screen.blit(point_view, ((screen.W / 2) - 20, (screen.H / 2) + 200))
    pygame.draw.rect(screen.screen, (80, 80, 80), [(screen.W / 2) - 30, (screen.H / 2 + 255), 73, 16], 2)

    # Blue ITem
    item = pygame.draw.rect(screen.screen, (0, 0, 255), [((screen.W / 2) - 30), (screen.H / 2) - 10, 60, 60], 0)

#Speed - Item
def instruction_screen_3():
    # Speed - Item
    font = pygame.font.SysFont(None, 50)
    point_view = font.render(str(10), True, (255, 255, 255))
    # Speed
    screen.templates.textfild(None, 50, 50, 800, 80, (255, 0, 0), language.tr().M7(2), 80)  # TODO: tr ok

    # Info TEXT
    screen.templates.textfild(None, 50, 140, 1500, 80, (255, 0, 0), language.tr().M7(7), 40)  # TODO: tr ok
    screen.templates.textfild(None, 50, 180, 1500, 80, (255, 0, 0), language.tr().M7(8), 40)  # TODO: tr ok

    # player_1
    pygame.draw.rect(screen.screen, (255, 0, 0), [player_1_png_rec[0] + 120, player_1_png_rec[1] - 220, 30, 30], 0)
    pygame.draw.rect(screen.screen, (255, 0, 0), [player_1_png_rec[0] + 85, player_1_png_rec[1] - 150, 100, 100], 10)

    screen.screen.blit(point_view, (player_1_png_rec[0] + 95, player_1_png_rec[1] + 10))
    pygame.draw.rect(screen.screen, (80, 80, 80), [player_1_png_rec[0] + 85, player_1_png_rec[1] + 50, 73, 16], 2)
    pygame.draw.rect(screen.screen, (255, 0, 0),
                     pygame.Rect(player_1_png_rec[0] + 85, player_1_png_rec[1] + 53, 10, 10))  # Geschwindigkeit

    # player_2
    pygame.draw.rect(screen.screen, (0, 255, 0), [player_2_png_rec[0] + 120, player_1_png_rec[1] - 220, 30, 30], 0)
    pygame.draw.rect(screen.screen, (0, 255, 0), [player_2_png_rec[0] + 85, player_2_png_rec[1] - 150, 100, 100], 10)

    screen.screen.blit(point_view, (player_2_png_rec[0] + 95, player_2_png_rec[1] + 10))
    pygame.draw.rect(screen.screen, (80, 80, 80), [player_2_png_rec[0] + 85, player_2_png_rec[1] + 50, 73, 16], 2)
    pygame.draw.rect(screen.screen, (0, 255, 0),
                     pygame.Rect(player_2_png_rec[0] + 85, player_2_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 0),
                     pygame.Rect(player_2_png_rec[0] + 95, player_2_png_rec[1] + 53, 10, 10))

    # player_3
    pygame.draw.rect(screen.screen, (255, 0, 255), [player_3_png_rec[0] + 120, player_1_png_rec[1] - 220, 30, 30], 0)
    pygame.draw.rect(screen.screen, (255, 0, 255), [player_3_png_rec[0] + 85, player_3_png_rec[1] - 150, 100, 100], 10)

    screen.screen.blit(point_view, (player_3_png_rec[0] + 95, player_3_png_rec[1] + 10))
    pygame.draw.rect(screen.screen, (80, 80, 80), [player_3_png_rec[0] + 85, player_3_png_rec[1] + 50, 73, 16], 2)
    pygame.draw.rect(screen.screen, (255, 0, 255),
                     pygame.Rect(player_3_png_rec[0] + 85, player_3_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (255, 0, 255),
                     pygame.Rect(player_3_png_rec[0] + 95, player_3_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (255, 0, 255),
                     pygame.Rect(player_3_png_rec[0] + 105, player_3_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (255, 0, 255),
                     pygame.Rect(player_3_png_rec[0] + 115, player_3_png_rec[1] + 53, 10, 10))

    # player_4
    pygame.draw.rect(screen.screen, (0, 255, 255), [player_4_png_rec[0] + 120, player_4_png_rec[1] - 220, 30, 30], 0)
    pygame.draw.rect(screen.screen, (0, 255, 255), [player_4_png_rec[0] + 85, player_4_png_rec[1] - 150, 100, 100], 10)

    screen.screen.blit(point_view, (player_4_png_rec[0] + 95, player_4_png_rec[1] + 10))
    pygame.draw.rect(screen.screen, (80, 80, 80), [player_4_png_rec[0] + 85, player_4_png_rec[1] + 50, 73, 16], 2)
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 85, player_4_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 95, player_4_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 105, player_4_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 115, player_4_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 125, player_4_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 135, player_4_png_rec[1] + 53, 10, 10))
    pygame.draw.rect(screen.screen, (0, 255, 255),
                     pygame.Rect(player_4_png_rec[0] + 145, player_4_png_rec[1] + 53, 10, 10))

#Yellow Item
def instruction_screen_4():
    # yellow item
    screen.templates.textfild(None, 50, 50, 800, 80, (255, 0, 0), language.tr().M7(3), 80)  # TODO: tr ok
    pygame.draw.rect(screen.screen, (255, 255, 0), pygame.Rect((screen.W / 2) - 25, (screen.H / 2) - 25, 50, 25))

    # Info TEXT
    screen.templates.textfild(None, 50, 140, 1500, 80, (255, 0, 0), language.tr().M7(9), 40)  # TODO: tr ok
    screen.templates.textfild(None, 50, 180, 1500, 80, (255, 0, 0), language.tr().M7(10), 40)  # TODO: tr ok

#White item
def instruction_screen_5():
    # white item
    screen.templates.textfild(None, 50, 50, 800, 80, (255, 0, 0), language.tr().M7(4), 80)  # TODO: tr ok
    pygame.draw.rect(screen.screen, (255, 255, 255), pygame.Rect((screen.W / 2) - 25, (screen.H / 2) - 25, 100, 100))

    # Info TEXT
    screen.templates.textfild(None, 50, 140, 1500, 80, (255, 0, 0), language.tr().M7(11), 40)  # TODO: tr ok
    screen.templates.textfild(None, 50, 180, 1500, 80, (255, 0, 0), language.tr().M7(12), 40)  # TODO: tr ok

#Mainloop for instruction
def instruction():
    screen_number = 1

    while True:
        screen.screen.fill((0, 0, 0))
        mouse_clickt = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    mouse_clickt = True

        if (screen_number == 1):
            instruction_screen_1()
            pass
        elif (screen_number == 2):  # Screen 2
            instruction_screen_2()

        elif (screen_number == 3):
            instruction_screen_3()
            pass
        elif (screen_number == 4):
            instruction_screen_4()
            pass
        elif (screen_number == 5):
            instruction_screen_5()
            pass

        # Button
        back_m = screen.templates.button(None, (screen.W / 2) - 250, (screen.H - 150), 500, 100, (0, 155, 155),
                                         (0, 255, 255), language.tr().M0(2), 80)  # TODO: tr ok
        if (screen_number > 1):
            back = screen.templates.button(None, (screen.W / 2) - 550, (screen.H - 150), 250, 100, (0, 155, 155),
                                           (0, 255, 255), language.tr().M0(0), 80)  # TODO: tr
            if mouse_clickt:
                if back.collidepoint(screen.mouse()):
                    screen_number -= 1

        if (screen_number < 5):
            next = screen.templates.button(None, (screen.W / 2) + 300, (screen.H - 150), 250, 100, (0, 155, 155),
                                           (0, 255, 255), language.tr().M0(1), 80)  # TODO: tr ok
            if mouse_clickt:
                if next.collidepoint(screen.mouse()):
                    screen_number += 1

        screen.mouse_cursor()
        pygame.display.flip()

        if mouse_clickt:
            if back_m.collidepoint(screen.mouse()):
                return 0
