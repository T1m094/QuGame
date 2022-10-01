import pygame

import screen
from screen import *
from control_pictures import *
from  user_input import *
import input_box
# For Joystick

def befor_the_game_start(item_p, player_array):
    start_p_1 = False
    start_p_2 = False
    start_p_3 = False
    start_p_4 = False
    font = pygame.font.SysFont(None, 50)
    start = False
    start_user = False
    timer_sound_bg = True

    size_input = [200,60]


    game_start_button = screen.templates.button(None, (screen.W / 2) - 250, (screen.H - 150), 500, 100, (0, 155, 155),
                                     (0, 255, 255), "Spiel Starten", 80)  # TODO: TEXT Spiel starten



    sound = soundandmusic.sound()
    player_count = len(player_array)

    # create inputbox for Player 1
    input_box1 = input_box.InputBox(250, (screen.H - 300), size_input[0], size_input[1],  (0, 255, 255),player_array[0].name)
    # create input for Player 2
    input_box2 = input_box.InputBox((screen.W - 250), (screen.H - 300), size_input[0], size_input[1], (0, 255, 255),player_array[1].name)
    #Box 1 aktiv

    #Visible Imput Filds
    if player_count == 2:
        input_boxes = [input_box1, input_box2]
    if player_count == 3:
        # create input for Player 3
        input_box3 = input_box.InputBox(250, 300, size_input[0], size_input[1], (0, 255, 255), player_array[2].name)
        input_boxes = [input_box1, input_box2, input_box3]
    if player_count == 4:
        # create input for Player 3
        input_box3 = input_box.InputBox(250, 300, size_input[0], size_input[1], (0, 255, 255), player_array[2].name)
        # create input for Player 4
        input_box4 = input_box.InputBox((screen.W - 250), 300, size_input[0], size_input[1], (0, 255, 255), player_array[3].name)
        input_boxes = [input_box1, input_box2, input_box3, input_box4]

    input_box1.toggel_active()

    while not start:
        joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        screen.screen.fill((0, 0, 0))
        # User Input
        for event in pygame.event.get():

            if event.type == pygame.JOYBUTTONUP:
                if event.joy == 0:
                    start_p_1 = True
                if event.joy == 1:
                    start_p_2 = True
                if event.joy == 2:
                    start_p_3 = True
                if event.joy == 3:
                    start_p_4 = True
                # VVV Kann eventuell verkürtzt werden
                if pygame.joystick.get_count() == 2:
                    if ((start_p_1 == True) and (start_p_2 == True)):
                        start_user = True
                if pygame.joystick.get_count() == 3:
                    if ((start_p_1 == True) and (start_p_2 == True) and (start_p_3 == True)):
                        start_user = True
                if pygame.joystick.get_count() == 4:
                    if ((start_p_1 == True) and (start_p_2 == True) and (start_p_3 == True) and (start_p_4)):
                        start_user = True

            if event.type == pygame.QUIT:
                quit()
                start = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_start_button.collidepoint(event.pos):
                    start_user = True

            for box in input_boxes:
                box.handle_event(event)

        #imput
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen.screen)

        #Text Klick for input





        #Start Button
        screen.templates.button(None, (screen.W / 2) - 250, (screen.H - 150), 500, 100, (0, 155, 155),
                                (0, 255, 255), "Spiel Starten", 80)  # TODO: TEXT Spiel starten

        item_p.draw_player()


        for x in range(0, player_count):
            player_array[x].draw_player()

        # Count Controller
        controller_count = pygame.joystick.get_count()
        # Text Leertaste to start
        text_start = font.render(str(language.tr().M0(5)), True, (255, 255, 255))  # TODO: tr ok
        screen.screen.blit(text_start, (((screen.W / 2) - 350), 40))

        # Instruction
        #Text Player-Name Player 1
        text_start = font.render("Spielername:", True, (255, 255, 255))  # TODO: TEXT Player NAme
        screen.screen.blit(text_start, (10, (screen.H - 300)))
        # Keyboard player 1
        player_1_png_rec = player_1_png.get_rect()
        player_1_png_rec.center = (150, (screen.H - 150))
        screen.screen.blit(player_1_png, player_1_png_rec)
        # Joystick player 1
        if (controller_count >= 1):
            if (start_p_1 == False):
                j_player_1_png_rec = joystick_png.get_rect()
                j_player_1_png_rec.center = (430, (screen.H - 120))
                screen.screen.blit(joystick_png, j_player_1_png_rec)
            else:
                j_player_1_png_rec = joystick_png.get_rect()
                j_player_1_png_rec.center = (430, (screen.H - 120))
                screen.screen.blit(joystick_1_png, j_player_1_png_rec)
        #Text Player-Name Player 2
        text_start = font.render("Spielername:", True, (255, 255, 255))  # TODO: TEXT Player NAme
        screen.screen.blit(text_start, ((screen.W - 500), (screen.H - 300)))
        # Keyboard player 2
        player_2_png_rec = player_2_png.get_rect()
        player_2_png_rec.center = ((screen.W - 150), (screen.H - 150))
        screen.screen.blit(player_2_png, player_2_png_rec)

        # Joystick player 2
        if (controller_count >= 2):
            # Not Start
            if (start_p_2 == False):
                j_player_2_png_rec = joystick_png.get_rect()
                j_player_2_png_rec.center = (screen.W - 450, (screen.H - 120))
                screen.screen.blit(joystick_png, j_player_2_png_rec)
            else:
                j_player_2_png_rec = joystick_png.get_rect()
                j_player_2_png_rec.center = (screen.W - 450, (screen.H - 120))
                screen.screen.blit(joystick_2_png, j_player_2_png_rec)

        if (player_count > 2):
            # Text Player-Name Player 3
            text_start = font.render("Spielername:", True, (255, 255, 255))  # TODO: TEXT Player NAme
            screen.screen.blit(text_start, (10, 300))
            # Keyboard player 3
            player_3_png_rec = player_3_png.get_rect()
            player_3_png_rec.center = (150, 150)
            screen.screen.blit(player_3_png, player_3_png_rec)

            # Joystick player 3
            if (controller_count >= 3):
                if (start_p_3 == False):  # Not start
                    j_player_3_png_rec = joystick_png.get_rect()
                    j_player_3_png_rec.center = (430, 170)
                    screen.screen.blit(joystick_png, j_player_3_png_rec)
                else:
                    j_player_3_png_rec = joystick_png.get_rect()
                    j_player_3_png_rec.center = (430, 170)
                    screen.screen.blit(joystick_3_png, j_player_3_png_rec)

        if (player_count > 3):
            # Text Player-Name Player 4
            text_start = font.render("Spielername:", True, (255, 255, 255))  # TODO: TEXT Player NAme
            screen.screen.blit(text_start, ((screen.W - 500), 300))

            player_4_png_rec = player_4_png.get_rect()
            player_4_png_rec.center = ((screen.W - 150), 150)
            screen.screen.blit(player_4_png, player_4_png_rec)

            # Joystick player 4
            if (controller_count == 4):
                if (start_p_4 == False):  # Not Start
                    j_player_4_png_rec = joystick_png.get_rect()
                    j_player_4_png_rec.center = ((screen.W - 450), 170)
                    screen.screen.blit(joystick_png, j_player_4_png_rec)
                else:
                    j_player_4_png_rec = joystick_png.get_rect()
                    j_player_4_png_rec.center = ((screen.W - 450), 170)
                    screen.screen.blit(joystick_4_png, j_player_4_png_rec)

        mouse_cursor()
        pygame.display.flip()

        # Wenn Spiel startet
        if start_user:
            if player_count == 2:
                player_array[0].name = input_box1.text
                player_array[1].name = input_box2.text
            if player_count == 3:
                player_array[0].name = input_box1.text
                player_array[1].name = input_box2.text
                player_array[2].name = input_box3.text

            if player_count == 4:
                player_array[0].name = input_box1.text
                player_array[1].name = input_box2.text
                player_array[2].name = input_box3.text
                player_array[3].name = input_box4.text
            start = True


    return controller_count

