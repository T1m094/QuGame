import collections
import pygame.draw
import screen
import screens.screen_for_player_count_selection
import screens.main_screen
import screens.settings_screen
import screens.about_screen
import instruction

from main import *
from screen import *
from player import *
from multiplayer_game_start import multiplayer_game_start

def main_menue():
    sound = soundandmusic.sound()
    sound.sound_bg_play_1()
    def logo():
        y = 100
        pygame.draw.rect(screen.screen, (0, 255, 0), ((screen.W/2) - 60,  30 + y, 100, 100), 10) #green
        pygame.draw.rect(screen.screen, (255, 0, 0), ((screen.W/2),  90 + y, 100, 100), 10) #red
        pygame.draw.rect(screen.screen, (0, 0, 255), ((screen.W/2), 90 + y , 40, 40), 0)  # blue
        pygame.draw.rect(screen.screen, (0, 255, 0), ((screen.W/2) + 80,  30 + y, 20, 20), 10) #green
        pygame.draw.rect(screen.screen, (255, 0, 0), ((screen.W/2) - 60,  170 + y, 20, 20), 10) #red

    simple_player_array = []
    #Simple Player Init
    for x in range(0,8):
        simple_player_array.append(simple_player())

    #Begin Screen
    screen_number = 1 #<-----TEST DEFAULT 1

    mouse_clickt = False
    while True:
        mouse_presses = pygame.mouse.get_pressed()
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

        if (mouse_presses[0]):
            for x in range(0, 8):
                if (simple_player_array[x].draw_player().collidepoint(mouse())):
                    simple_player_array[x].pos_x = mouse()[0] - 50
                    simple_player_array[x].pos_y = mouse()[1] - 50

        screen.screen.fill((0, 0, 0))
        logo()

        #Start Simple Player
        for x in range(0, 8):
            simple_player_array[x].start()

        # Menü
        # 1. Spielen
        # 2. Anleitung
        # 3. Einstellung
        #   Sound, Ton Bild
        # 4. Info 5. Exit

        # Main Screen
        if (screen_number == 1):
            select = screens.main_screen.main_screen(mouse_clickt) #Open Main Chois
            if not select == None:
                if (select == 1): #Spiel starten
                    screen_number = 2
                elif (select == 2): #Anleitung
                    instruction.instruction()
                elif (select == 3): #Settings
                    screen_number = 3
                elif (select == 4): #Info
                    screen_number = 4

        # Player Count Selection
        elif (screen_number == 2):
            select = screens.screen_for_player_count_selection.screen_for_player_count_selection(mouse_clickt)
            if not select == None:
                if (select == 0): #back main
                    screen_number = 1
                elif (select == 1): #Two Player
                    screen_number = 1
                    screen.screen.fill((0, 0, 0))
                    multiplayer_game_start(2)
                elif (select == 2): #Tree Player
                    screen_number = 1
                    screen.screen.fill((0, 0, 0))
                    multiplayer_game_start(3)
                elif (select == 3): #Four Player
                    screen_number = 1
                    screen.screen.fill((0, 0, 0))
                    multiplayer_game_start(4)
                elif (select == 4): #Online
                    screen_number = 1
                    screen.screen.fill((0, 0, 0))

        elif (screen_number == 3): #Settings
            select = screens.settings_screen.settings_screen(mouse_clickt)
            if not select == None:
                if (select == 0): #Back main
                    screen_number = 1

        elif (screen_number == 4): #About
            select = screens.about_screen.about_screen(mouse_clickt)
            if not select == None:
                if (select == 0): #Back to main
                    screen_number = 1

        mouse_clickt = False
        pygame.display.flip()