import  pygame
import screen

def user_input(controller_count, player_array, timer):
    player_array_len = len(player_array)
    player = player_array

    spielpause = False

    #Wenn Joystick anzahl sich ändert wird pausiert
    if not (controller_count == pygame.joystick.get_count()):
        timer.pause()
        spielpause = True
        pygame.mixer.music.pause()
        back_to_main = screen.templates().breake_screen()
        if (back_to_main == 1):
            pygame.mixer.music.unpause()
            return 1
        timer.start()
        pygame.mixer.music.unpause()

#Kann noch verbessert werden
    # For Two Player
    if (player_array_len == 2):
        for event in pygame.event.get():
            # For Controller
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 7:
                    if spielpause == True:
                        spielpause = False
                    else:
                        timer.pause()
                        spielpause = True
                        pygame.mixer.music.pause()
                        back_to_main = screen.templates().breake_screen()
                        if (back_to_main == 1):
                            pygame.mixer.music.unpause()
                            return 1
                        timer.start()
                        pygame.mixer.music.unpause()
            if event.type == pygame.JOYAXISMOTION:
                # Links
                if ((event.value < -0.68) and (event.axis == 0)):
                    #print("links")
                    player[event.joy].change_direction(4)
                # Oben
                if ((event.value < -0.68) and (event.axis == 1)):
                    #print("oben")
                    player[event.joy].change_direction(8)
                # Rechts
                if ((event.value > 0.68) and ((event.axis == 0))):
                    #print("rechts")
                    player[event.joy].change_direction(6)
                # Unten
                if ((event.value > 0.68) and (event.axis == 1)):
                    #print("unten")
                    player[event.joy].change_direction(2)
            if event.type == pygame.JOYHATMOTION:
                # print("oben")
                if event.value == (0, 1):
                    player[event.joy].change_direction(8)
                # print("unten")
                if event.value == (0, -1):
                    player[event.joy].change_direction(2)
                # print("links")
                if event.value == (-1, 0):
                    player[event.joy].change_direction(4)
                # print("rechts")
                if event.value == (1, 0):
                    player[event.joy].change_direction(6)

            if event.type == pygame.QUIT:
                quit()
                return
            elif event.type == pygame.KEYDOWN:

                if ((event.key == pygame.K_ESCAPE) or (event.key == pygame.K_SPACE)) :
                    if spielpause == True:
                        spielpause = False

                    else:
                        timer.pause()
                        spielpause = True
                        pygame.mixer.music.pause()
                        back_to_main = screen.templates().breake_screen()
                        if (back_to_main == 1):
                            pygame.mixer.music.unpause()
                            return 1
                        timer.start()
                        pygame.mixer.music.unpause()


                # Player 1
                elif event.key == pygame.K_RIGHT:
                    player[0].change_direction(6)
                elif event.key == pygame.K_LEFT:
                    player[0].change_direction(4)
                elif event.key == pygame.K_UP:
                    player[0].change_direction(8)
                elif event.key == pygame.K_DOWN:
                    player[0].change_direction(2)
                # Player 2
                elif event.key == pygame.K_w:
                    player[1].change_direction(8)
                elif event.key == pygame.K_a:
                    player[1].change_direction(4)
                elif event.key == pygame.K_s:
                    player[1].change_direction(2)
                elif event.key == pygame.K_d:
                    player[1].change_direction(6)

    #For Tree Player
    if (player_array_len == 3):
        for event in pygame.event.get():
            # For Controller
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 7:
                    if spielpause == True:
                        spielpause = False
                    else:
                        timer.pause()
                        spielpause = True
                        pygame.mixer.music.pause()
                        back_to_main = screen.templates().breake_screen()
                        if (back_to_main == 1):
                            pygame.mixer.music.unpause()
                            return 1
                        timer.start()
                        pygame.mixer.music.unpause()
            if event.type == pygame.JOYAXISMOTION:
                # Links
                if ((event.value < -0.35) and (event.axis == 0)):
                    player[event.joy].change_direction(4)

                # Oben
                if ((event.value < -0.35) and (event.axis == 1)):
                    player[event.joy].change_direction(8)
                # Rechts
                if ((event.value > 0.35) and ((event.axis == 0))):
                    player[event.joy].change_direction(6)
                # Unten
                if ((event.value > 0.35) and (event.axis == 1)):
                    player[event.joy].change_direction(2)
            if event.type == pygame.QUIT:
                quit()
                return
            elif event.type == pygame.KEYDOWN:

                if ((event.key == pygame.K_ESCAPE) or (event.key == pygame.K_SPACE)) :
                    if spielpause == True:
                        spielpause = False

                    else:
                        timer.pause()
                        spielpause = True
                        pygame.mixer.music.pause()
                        back_to_main = screen.templates().breake_screen()
                        if (back_to_main == 1):
                            pygame.mixer.music.unpause()
                            return 1
                        timer.start()
                        pygame.mixer.music.unpause()

                # Player 1
                elif event.key == pygame.K_RIGHT:
                    player[0].change_direction(6)
                elif event.key == pygame.K_LEFT:
                    player[0].change_direction(4)
                elif event.key == pygame.K_UP:
                    player[0].change_direction(8)
                elif event.key == pygame.K_DOWN:
                    player[0].change_direction(2)
                # Player 2
                elif event.key == pygame.K_w:
                    player[1].change_direction(8)
                elif event.key == pygame.K_a:
                    player[1].change_direction(4)
                elif event.key == pygame.K_s:
                    player[1].change_direction(2)
                elif event.key == pygame.K_d:
                    player[1].change_direction(6)
                # Player 3
                elif event.key == pygame.K_i:
                    player[2].change_direction(8)
                elif event.key == pygame.K_j:
                    player[2].change_direction(4)
                elif event.key == pygame.K_k:
                    player[2].change_direction(2)
                elif event.key == pygame.K_l:
                    player[2].change_direction(6)

    #For Four Player
    if (player_array_len == 4):
        for event in pygame.event.get():
            # For Controller
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 7:
                    if spielpause == True:
                        spielpause = False
                    else:
                        timer.pause()
                        spielpause = True
                        pygame.mixer.music.pause()
                        back_to_main = screen.templates().breake_screen()
                        if (back_to_main == 1):
                            pygame.mixer.music.unpause()
                            return 1
                        timer.start()
                        pygame.mixer.music.unpause()
            if event.type == pygame.JOYAXISMOTION:
                # print(event)
                # Links
                if ((event.value < -0.35) and (event.axis == 0)):
                    player[event.joy].change_direction(4)

                # Oben
                if ((event.value < -0.35) and (event.axis == 1)):
                    player[event.joy].change_direction(8)
                # Rechts
                if ((event.value > 0.35) and ((event.axis == 0))):
                    player[event.joy].change_direction(6)
                # Unten
                if ((event.value > 0.35) and (event.axis == 1)):
                    player[event.joy].change_direction(2)
            if event.type == pygame.QUIT:
                quit()
                return
            elif event.type == pygame.KEYDOWN:

                if ((event.key == pygame.K_ESCAPE) or (event.key == pygame.K_SPACE)) :
                    if spielpause == True:
                        spielpause = False
                    else:
                        timer.pause()
                        spielpause = True
                        pygame.mixer.music.pause()
                        back_to_main = screen.templates().breake_screen()
                        if (back_to_main == 1):
                            pygame.mixer.music.unpause()
                            return 1
                        timer.start()
                        pygame.mixer.music.unpause()

                # Player 1
                elif event.key == pygame.K_RIGHT:
                    player[0].change_direction(6)
                elif event.key == pygame.K_LEFT:
                    player[0].change_direction(4)
                elif event.key == pygame.K_UP:
                    player[0].change_direction(8)
                elif event.key == pygame.K_DOWN:
                    player[0].change_direction(2)
                # Player 2
                elif event.key == pygame.K_w:
                    player[1].change_direction(8)
                elif event.key == pygame.K_a:
                    player[1].change_direction(4)
                elif event.key == pygame.K_s:
                    player[1].change_direction(2)
                elif event.key == pygame.K_d:
                    player[1].change_direction(6)
                # Player 3
                elif event.key == pygame.K_i:
                    player[2].change_direction(8)
                elif event.key == pygame.K_j:
                    player[2].change_direction(4)
                elif event.key == pygame.K_k:
                    player[2].change_direction(2)
                elif event.key == pygame.K_l:
                    player[2].change_direction(6)
                # Player 4
                elif event.key == pygame.K_KP8:
                    player[3].change_direction(8)
                elif event.key == pygame.K_KP4:
                    player[3].change_direction(4)
                elif event.key == pygame.K_KP2:
                    player[3].change_direction(2)
                elif event.key == pygame.K_KP6:
                    player[3].change_direction(6)