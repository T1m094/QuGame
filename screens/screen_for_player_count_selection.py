from screen import *

def screen_for_player_count_selection(mouse_presses):
    button_x = (W / 2 - 250)
    button_y = (H / 2 - 50)

    # Two Player
    b1 = templates().button(button_x, (button_y - 120), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M2(0),
                            80)  # TODO: tr ok
    # TREE Player
    b2 = templates().button(button_x, (button_y), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M2(1),
                            80)  # TODO: tr ok
    # Four Player
    b3 = templates().button(button_x, (button_y + 120), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M2(2),
                            80)  # TODO: tr ok
    # Online
    b4 = templates().button(button_x, (button_y + 240), 500, 100, (185, 185, 185), (155, 155, 155), language.tr().M2(3),
                            80)  # TODO: tr ok #TODO:ONLINE
    # Back
    b0 = templates().button(button_x, (button_y + 360), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(0),
                            80)  # TODO: tr ok

    mouse_cursor()

    if mouse_presses:
        if b1.collidepoint(mouse()):
            return 1
        elif b2.collidepoint(mouse()):
            return 2
        elif b3.collidepoint(mouse()):
            return 3
        # elif b4.collidepoint(mouse()):
        #    return 4
        elif b0.collidepoint(mouse()):
            return 0
