from io import BytesIO

import pygame
from data.sound.bg_music_1 import bg_music_1
from data.sound.bg_music_2 import bg_music_2
from data.sound.time_out_music import time_out_music
from data.sound.item_blue_pf import item_blue_pf
from data.sound.item_yellow_pf import item_yellow_pf
from data.sound.item_speed_pf import item_speed_pf
from data.sound.item_destroy_pf import item_destroy_pf

pygame.mixer.init()
class sound():
    #TODO: Durchlesen!
    # https://www.python-lernen.de/rueckgabewert-funktionen.htm

    #Backgroundmusic
    #bg_music_1 = bg_music_1  #"data/sound/musicfox_brainstorming.mp3" #https://www.musicfox.com/info/kostenlose-gemafreie-musik.php
    #bg_music_2 = bg_music_2 #"data/sound/Dario_sound.mp3"
    time_out_music = time_out_music #"data/sound/time_out.mp3" #https://mixkit.co/free-sound-effects/
    '''
    #Sound Effects
    item_blue_pf = item_blue_pf #"data/sound/sms-alert-2-daniel_simon.wav"#https://soundbible.com/
    item_yellow_pf = item_yellow_pf #"data/sound/Fiep_2.mp3"  #https://soundbible.com/#Andreas Bruch "data/sound/sms-alert-1-daniel_simon.mp3"
    item_speed_pf = item_speed_pf #"data/sound/sms-alert-5-daniel_simon.mp3"#https://soundbible.com/
    '''
    bg_state = 1
    bg_vol = 1

    def mute(self, state):
        if state:
            self.bg_vol = 0
            self.bg_state = 0
            pygame.mixer.music.set_volume(0)
        else:
            self.bg_vol = 1
            self.bg_state = 1
            pygame.mixer.music.set_volume(1)

    def get_bg_vol(self):
        return sound.bg_vol

    def get_bg_state(self):
        return sound.bg_state

    def change_bg_vol(vol):
        sound.bg_vol = vol
        pygame.mixer.music.set_volume(vol)

    def sound_bg_play_1(self):
        pygame.mixer.music.load(BytesIO(bg_music_1))
        pygame.mixer.music.play(-1, 0.0)

    def sound_bg_play_2(self):
        pygame.mixer.music.load(BytesIO(bg_music_2))
        pygame.mixer.music.play(-1, 0.0)

    def sound_bg_stopp(self):
        pygame.mixer.music.fadeout(3000)

    def time_out_play(self):
        pygame.mixer.music.load(BytesIO(time_out_music))
        pygame.mixer.music.play(1, 0.0)

    def blue_item(self):
        self.item_blue = pygame.mixer.Sound(BytesIO(item_blue_pf))
        pygame.mixer.Sound.play(self.item_blue)
        #pygame.mixer.music.play(1, 0.0)

    def yellow_item(self):
        self.item_yellow = pygame.mixer.Sound(BytesIO(item_yellow_pf))
        pygame.mixer.Sound.play(self.item_yellow)
        #pygame.mixer.music.play(1, 0.0)

    def speed_item(self):
        self.item_speed = pygame.mixer.Sound(BytesIO(item_speed_pf))
        pygame.mixer.Sound.play(self.item_speed)
        #pygame.mixer.music.play(1, 0.0)

    def destroy_item(self):
        self.item_destroy = pygame.mixer.Sound(BytesIO(item_destroy_pf))  # "data/sound/item_destroy.mp3"#https://soundbible.com/
        pygame.mixer.Sound.play(self.item_destroy)