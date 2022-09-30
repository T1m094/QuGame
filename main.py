import pygame
from mainmenue import *
from datetime import datetime
from control_pictures import icon

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_icon(icon)
    pygame.joystick.init()

    try:
        #TEST GIT
        main_menue()
    except Exception as e:
        error_text = e
        timestamp = datetime.now().strftime('%H-%M_%d-%m-%Y')

        error_datei_name = "DEBUGGER.txt"

        with open(error_datei_name, "a") as txtfile:
            print(timestamp," String Variable: {}".format(error_text), file=txtfile)

    pygame.joystick.quit()
    pygame.quit()