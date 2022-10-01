import pygame.math
import before_the_game_start
from winner_display import *
from screen import *
from item import *
from  user_input import *
from MyTimer import *

def multiplayer_game_start(player_count):
    sound = soundandmusic.sound()

    #Time
    clock = pygame.time.Clock()
    #Schrift
    font = pygame.font.SysFont(None, 50)

    def convert(sekunde):
        sekunde = sekunde % (24 * 3600)
        hour = sekunde // 3600
        sekunde %= 3600
        minutes = sekunde // 60
        sekunde %= 60

        return "%02d:%02d" % (minutes, sekunde)

    def init_player(count):
        if (count > 4):
            print("Max 4 Player")
            return

        player_array = []
        for x in range(count):
            player_array.append(player())
        return player_array

    def start_player(player_array):
        for x in range(len(player_array)):
            player_array[x].start()

    #Init Item
    item_d = item_destroy()
    item_p = item_point(((screen.W/2) - 30), ((screen.H/2) - 30), 60, 60, 0, 0, 0, (0, 0, 255), 0)
    fiep = item_fiep()

    #Init Player
    player_array = init_player(player_count)

    #Item
    item_p.start()
    fiep.start()

    pygame.display.flip()

    def quit():
        return

    #Variablen
    close = False

    timer_sound_timeout = True
    timer_1 = MyTimer()



    # Start menü
    controller_count = before_the_game_start.befor_the_game_start(item_p, player_array)

    sound.sound_bg_play_2()
    timer_1.start()

    #______________Start Game_________________
    while not close:
        seconds_current = timer_1.get_current_sec()

        '''
        if (seconds_current < 13):
            if timer_sound_bg:
                sound.sound_bg_stopp()
                timer_sound_bg = False
        '''

        if (seconds_current < 10):

            if seconds_current % 1 > 0.5: # Time Blinking
                count_t = font.render(str(convert(seconds_current)), True, (0, 0, 0))
            else:
                count_t = font.render(str(convert(seconds_current)), True, (155, 25, 0))
            '''
            if timer_sound_timeout:
                sound.time_out_play()
                timer_sound_timeout = False
            '''
        else:
            count_t = font.render(str(convert(seconds_current)), True, (255, 255, 255))

        #End
        if (seconds_current <= 0):
            close = True

        screen.screen.blit(count_t, (((screen.W / 2) - 30), (screen.H - 50)))

        #User input
        timer_1.get_elapsed()
        back_to_main = user_input(controller_count,player_array,timer_1)

        if (back_to_main == 1):
            sound.sound_bg_play_1()
            close = True
            timer_1.get_elapsed()
        timer_1.start()


        #Logic
        #Item start
        item_d.start(player_array)
        item_p.start()
        fiep.start()

        #Player start
        start_player(player_array)

        pygame.display.flip()

        #Bumping Opponent
        player_array[1].opponent_bumping(player_array[0])
        player_array[0].opponent_bumping(player_array[1])

        if (player_count > 2):
            player_array[2].opponent_bumping(player_array[0])
            player_array[0].opponent_bumping(player_array[2])

            player_array[2].opponent_bumping(player_array[1])
            player_array[1].opponent_bumping(player_array[2])

        if (player_count > 3):
            player_array[3].opponent_bumping(player_array[0])
            player_array[0].opponent_bumping(player_array[3])

            player_array[3].opponent_bumping(player_array[1])
            player_array[1].opponent_bumping(player_array[3])

            player_array[3].opponent_bumping(player_array[2])
            player_array[2].opponent_bumping(player_array[3])

        item_d.bumping(player_array)
        item_p.acquire_by_include(player_array, 1)
        fiep.acquire_by_include(player_array,3)

        # Window update
        screen.screen.fill((0, 0, 0))
        clock.tick(screen.FPS)

    pygame.display.flip()

    winner_display(player_array)
    objekt.count_player = 0

def countdown(clock):
    screen.screen.fill((0, 0, 0))
    clock.tick(screen.FPS)
    pygame.display.flip()