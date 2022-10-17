from screen import *

def main_screen(mouse_presses):
    button_x = (W / 2 - 250)
    button_y = (H / 2 - 50)

    #Text Start
    b1 = templates().button(button_x, (button_y - 120), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(1), 80)
    #Text Instruction
    b2 = templates().button(button_x, button_y, 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(2), 80)
    #Text Settings
    b3 = templates().button(button_x, (button_y + 120), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(3), 80)
    #Text INFO
    b4 = templates().button(button_x, (button_y + 240), 250, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(6), 70)
    #Text Exit
    b0 = templates().button((button_x + 260), (button_y + 240), 240, 100, (0, 155, 155), (0, 255, 255), language.tr().M1(0), 80)

    mouse_cursor()

    if mouse_presses:
        if b0.collidepoint(mouse()):
            quit()
        elif b1.collidepoint(mouse()):
            return 1
        elif b2.collidepoint(mouse()):
            return 2
        elif b3.collidepoint(mouse()):
            return 3
        elif b4.collidepoint(mouse()):
            return 4