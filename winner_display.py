import pygame.display
import language
from player import *

def winner_display(player_array):
    sound.sound_bg_play_1(self=sound)
    # Schrift
    font = pygame.font.SysFont('''Arial Baltic''', 80)
    name_font = pygame.font.SysFont('''Arial Baltic''', 50)


    player_count = len(player_array)
    winner_array = []

    #Winner sort
    for x in range(0, player_count):
        winner_array.append([player_array[x].color,player_array[x].points,player_array[x].name])

    winner_array.sort(key=lambda x: x[1])
    #Reihenfolge umkehren
    winner_array = winner_array[::-1]
    #Show Score
    #Print Frame
    #     1                                  5
    # p1______p2                     p5__________p6
    # |        \   2     p9        4 /            |
    # |6        \p3_________________/p4           |8
    # |                  3                        |
    # |p7_________________ 7______________________| p8
    h = -200
    p1 = [(screen.W/2) - 450 ,(screen.H/4)  + h]
    p2 = [(screen.W/2) - 200 ,(screen.H/4)  + h]
    p3 = [(screen.W/2) - 150 ,(screen.H/4) + 50 + h]
    p4 = [(screen.W/2) + 150 ,(screen.H/4) + 50 + h]
    p5 = [(screen.W/2) + 200 ,(screen.H/4) + h]
    p6 = [(screen.W/2) + 450 ,(screen.H/4) + h]
    p7 = [(screen.W/2) - 450 , screen.H + h]
    p8 = [(screen.W/2) + 450, screen.H + h]
    p9 = [(screen.W/2), (screen.H/4) + h]

    button_x = (screen.W/2) - 450
    button_y = (screen.H / 2 - 50)

    #Points
    point_view = str(winner_array[0][1])
    text_point_1= name_font.render(point_view, True, winner_array[0][0])

    point_view = str(winner_array[1][1])
    text_point_2 = name_font.render(point_view, True, winner_array[1][0])

    if (player_count > 2):
        point_view = str(winner_array[2][1])
        text_point_3 = name_font.render(point_view, True, winner_array[2][0])

    if (player_count > 3):
        point_view = str(winner_array[3][1])
        text_point_4 = name_font.render(point_view, True, winner_array[3][0])


    #R
    simple_player_2 = simple_player_winner(winner_array[0][0], ((screen.W/2) + 500),((screen.H) - 200))
    simple_player_21 = simple_player_winner(winner_array[0][0], ((screen.W/2) + 500),((screen.H) - 400))
    simple_player_22 = simple_player_winner(winner_array[0][0], ((screen.W/2) + 500),((screen.H) - 600))
    simple_player_23 = simple_player_winner(winner_array[0][0], ((screen.W/2) + 500),((screen.H) - 800))
    simple_player_24 = simple_player_winner(winner_array[0][0], ((screen.W/2) + 500),((screen.H) - 1000))

    #L
    simple_player_1 = simple_player_winner(winner_array[0][0], ((screen.W/2) - 600),((screen.H) - 200))
    simple_player_11 = simple_player_winner(winner_array[0][0], ((screen.W/2) - 600),((screen.H) - 400))
    simple_player_12 = simple_player_winner(winner_array[0][0], ((screen.W/2) - 600),((screen.H) - 600))
    simple_player_13 = simple_player_winner(winner_array[0][0], ((screen.W/2) - 600),((screen.H) - 800))
    simple_player_14 = simple_player_winner(winner_array[0][0], ((screen.W/2) - 600),((screen.H) - 1000))




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                return
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    quit()
                    return

        screen.screen.fill((0,0,0))
        # Line 1
        pygame.draw.line(screen.screen, (0, 255, 255), p1, p2, 5)
        # Line 2
        pygame.draw.line(screen.screen, (0, 255, 255), p2, p3, 5)
        # Line 3
        pygame.draw.line(screen.screen, (0, 255, 255), p3, p4, 5)
        # Line 4
        pygame.draw.line(screen.screen, (0, 255, 255), p4, p5, 5)
        # Line 5
        pygame.draw.line(screen.screen, (0, 255, 255), p5, p6, 5)
        # Line 6
        pygame.draw.line(screen.screen, (0, 255, 255), p1, p7, 10)
        # Line 7
        pygame.draw.line(screen.screen, (0, 255, 255), p7, p8, 10)
        # Line 8
        pygame.draw.line(screen.screen, (0, 255, 255), p6, p8, 10)

        text_surface = font.render(str(language.tr().M0(7)), True, (0, 255, 255)) #TODO: tr ok
        text_rec = text_surface.get_rect(center=(p9))

        screen.screen.blit(text_surface, text_rec)

        # Draw Player
        #Frame
        pos_y = 0
        name_and_point_pos_y = 260

        #Info Text Name Punkte
        text = name_font.render("Spielername", True, (0,255,255)) #TODO: TR
        screen.screen.blit(text, ((screen.W / 2) - 300, ((screen.H/4) + 90 + h)))
        text = name_font.render("Punkte", True, (0,255,255)) #TODO: TR
        screen.screen.blit(text, ((screen.W / 2) + 200, ((screen.H/4) + 90 + h)))


        pygame.draw.rect(screen.screen, (winner_array[0][0]), ((screen.W / 2) - 400, 230 + pos_y, 800, 100), 5) #Frame
        screen.screen.blit(text_point_1, ((screen.W / 2) + 200, name_and_point_pos_y))                         #Points

        name_and_point_pos_y += 150
        pos_y += 150

        pygame.draw.rect(screen.screen, (winner_array[1][0]), ((screen.W / 2) - 400, 230 + pos_y, 800, 100), 5)
        screen.screen.blit(text_point_2, ((screen.W / 2) + 200, name_and_point_pos_y))

        # Text pos y
        name_and_point_pos_y = 260
        # Name
        name = str(winner_array[0][2])
        name_text = name_font.render(name, True, winner_array[0][0]) # <-- xD
        screen.screen.blit(name_text, ((screen.W / 2) - 300, name_and_point_pos_y))
        name_and_point_pos_y +=  150

        name = str(winner_array[1][2])
        name_text = name_font.render(name, True, winner_array[1][0])
        screen.screen.blit(name_text, ((screen.W / 2) - 300, name_and_point_pos_y))

        if (player_count > 2):
            name_and_point_pos_y += 150
            pos_y += 150
            pygame.draw.rect(screen.screen, (winner_array[2][0]), ((screen.W / 2) - 400, 230 + pos_y, 800, 100), 5)
            screen.screen.blit(text_point_3, ((screen.W / 2) + 200, name_and_point_pos_y))

            name = str(winner_array[2][2])
            name_text = name_font.render(name, True, winner_array[2][0])
            screen.screen.blit(name_text, ((screen.W / 2) - 300, name_and_point_pos_y))

        if (player_count > 3):
            name_and_point_pos_y += 150
            pos_y += 150
            pygame.draw.rect(screen.screen, (winner_array[3][0]), ((screen.W / 2) - 400, 230 + pos_y, 800, 100), 5)
            screen.screen.blit(text_point_4, ((screen.W / 2) + 200, name_and_point_pos_y))

            name = str(winner_array[3][2])
            name_text = name_font.render(name, True, winner_array[3][0])
            screen.screen.blit(name_text, ((screen.W / 2) - 300, name_and_point_pos_y))

        #Backbutton
        b0 = screen.templates().button(button_x, (button_y + 450), 400, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(2),
                                       80) #TODO: tr ok
        b1 = screen.templates().button((screen.W/2) + 50, (button_y + 450), 400, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(8),
                                       80) #TODO: tr ok

        # Start Simple Player
        simple_player_1.start()
        simple_player_2.start()
        simple_player_11.start()
        simple_player_12.start()
        simple_player_13.start()
        simple_player_14.start()
        simple_player_21.start()
        simple_player_22.start()
        simple_player_23.start()
        simple_player_24.start()




        pygame.display.update(screen.mouse_cursor())
        pygame.display.flip()

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if b0.collidepoint(mouse_pos):
                return False #Main menue
            if b1.collidepoint(mouse_pos):
                return True #PLAY AGAIN