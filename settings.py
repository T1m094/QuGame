import soundandmusic

class settings():
    language = 0 # | 0 Deutsch | 1 English |

    sound_background_state = 1
    sound_background_vol = 1

    def sound_state_change(change): # 0 == links 1 == rechts
        if change == 1:
            settings.sound_background_state += 1
        if change == 0:
            settings.sound_background_state -= 1

        if (settings.sound_background_state > 1):
            settings.sound_background_state = 0
        elif (settings.sound_background_state < 0):
            settings.sound_background_state = 1


        if (settings.sound_background_state == 0):#Aus
            soundandmusic.sound.mute(soundandmusic, True)
        else:
            soundandmusic.sound.mute(soundandmusic, False)

    def leg_change(change): # 0 == left 1 == right
        global language

        if change == 1:
            settings.language += 1
        if change == 0:
            settings.language -= 1

        if (settings.language > 1): #for mor Languages
            settings.language = 0
        elif (settings.language < 0):
            settings.language = 1

    def get_language(self):
        return settings.language

    def get_sound_state(self):
        return self.sound_background_state
    def get_sound_vol(self):
        return self.sound_background_vol

