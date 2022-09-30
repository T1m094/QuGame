from screen import *
import settings
def settings_screen(mouse_presses):
    button_x = (W / 2 - 250)
    button_y = 310

    #Text Sprache
    templates().textfild(button_x, button_y, 500, 60, (0, 155, 155), language.tr().M3(2), 80)#TODO: tr ok

    button_y += 65

    #Änderen der Sprache
    language_b = templates().button_change(button_x, button_y, 500, 60, (0, 155, 155), (0, 255, 255), language.tr().M3(1),80)#TODO: tr ok

    button_y += 75

    #Text Sound
    templates().textfild(button_x, button_y, 500, 60, (0, 155, 155), language.tr().M3(4), 80)  #TODO: tr ok

    button_y += 65

    # Sound on off
    sound_bg_state = templates().button_change(button_x, button_y, 500, 60, (0, 155, 155), (0, 255, 255),language.tr().M3(3)[settings.settings.sound_background_state],80)   #TODO: tr ok

    button_y += 65

    # Sound Volume
    sound_bg_vol = templates().sound_volume(button_x, button_y, 500, 100, (0, 155, 155), (0, 255, 255),soundandmusic.sound.get_bg_vol(templates))
    print(sound_bg_vol)
    button_y += 150

    #Text Back
    b0 = templates().button(button_x, button_y, 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(0), 80)  #TODO: tr ok

    mouse_cursor()

    if mouse_presses:
        print("klick")
        if b0.collidepoint(mouse()):
            return 0
        # Language
        if (language_b == 0):
            settings.settings.leg_change(0)
        if (language_b == 1):
            settings.settings.leg_change(1)

        # SoundVOl
        if (sound_bg_vol == 1):
            soundandmusic.sound.change_bg_vol(0.10)

        if (sound_bg_vol == 2):
            soundandmusic.sound.change_bg_vol(0.40)

        if (sound_bg_vol == 3):
            print("BG_vol = 3")
            soundandmusic.sound.change_bg_vol(0.60)

        if (sound_bg_vol == 4):
            print("BG_vol = 4")
            soundandmusic.sound.change_bg_vol(1)

        # SOUND State
        if (sound_bg_state == 1):
            print("sound 1")
            settings.settings.sound_state_change(1)
        if (sound_bg_state == 0):
            print("sound 0")
            settings.settings.sound_state_change(0)
