from screen import *
import settings
def settings_screen(mouse_presses):
    button_x = (W / 2 - 250)
    button_y = 310

    #Text Language
    templates().textfild(button_x, button_y, 500, 60, (0, 155, 155), language.tr().M3(2), 80)
    button_y += 65

    #cahnge Language
    language_b = templates().button_change(button_x, button_y, 500, 60, (0, 155, 155), (0, 255, 255), language.tr().M3(1),80)
    button_y += 75

    #Text Sound
    templates().textfild(button_x, button_y, 500, 60, (0, 155, 155), language.tr().M3(4), 80)
    button_y += 65

    # Sound on off
    sound_bg_state = templates().button_change(button_x, button_y, 500, 60, (0, 155, 155), (0, 255, 255),language.tr().M3(3)[settings.settings.sound_background_state],80)
    button_y += 75

    #Textfild Volume
    templates().textfild(button_x, button_y, 500, 60, (0, 155, 155), language.tr().M3(5), 70)
    button_y += 75

    # Sound Volume
    sound_bg_vol = templates().sound_volume(button_x, button_y, 500, 100, (0, 155, 155), (0, 255, 255),soundandmusic.sound.get_bg_vol(templates))
    button_y += 65
    button_y += 150

    #Text Back
    b0 = templates().button(button_x, button_y, 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(0), 80)

    mouse_cursor()

    if mouse_presses:
        if b0.collidepoint(mouse()):
            return 0
        # Language
        if (language_b == 0):
            settings.settings.leg_change(0)
        if (language_b == 1):
            settings.settings.leg_change(1)

        # SoundVOl
        if (sound_bg_vol == 1):
            soundandmusic.sound.change_bg_vol(0.20)
            settings.settings.sound_on(settings)

        if (sound_bg_vol == 2):
            soundandmusic.sound.change_bg_vol(0.40)
            settings.settings.sound_on(settings)

        if (sound_bg_vol == 3):
            soundandmusic.sound.change_bg_vol(0.60)
            settings.settings.sound_on(settings)
        if (sound_bg_vol == 4):
            soundandmusic.sound.change_bg_vol(1)
            settings.settings.sound_on(settings)

        # SOUND State
        if (sound_bg_state == 1):
            settings.settings.sound_state_change(1)
        if (sound_bg_state == 0):
            settings.settings.sound_state_change(0)