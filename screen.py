import pygame
import language
import settings
import soundandmusic
from control_pictures import icon

pygame.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN, 1) #TODO: DISPLAY  V-Sync!!!
#screen = pygame.display.set_mode((1200,800),pygame.RESIZABLE, 1) #TODO: DISPLAY  V-Sync!!! TEST
pygame.display.set_caption("Qu")
pygame.display.set_icon(icon)
W, H = screen.get_size()
FPS = 60

def logo():
    pygame.draw.rect(screen, (0, 255, 0), ((W / 2) - 60, 30, 100, 100), 10)  # Grün
    pygame.draw.rect(screen, (255, 0, 0), ((W / 2), 90, 100, 100), 10)  # Rot
    pygame.draw.rect(screen, (0, 0, 255), ((W / 2), 90, 40, 40), 0)  # Blau
    pygame.draw.rect(screen, (0, 255, 0), ((W / 2) + 80, 30, 20, 20), 10)  # Grün
    pygame.draw.rect(screen, (255, 0, 0), ((W / 2) - 60, 170, 20, 20), 10)  # Rot

def mouse_cursor():
    # Mouse hidden
    pygame.mouse.set_visible(False)
    mouse_pos = pygame.mouse.get_pos()
    pos_x = mouse_pos[0]
    pos_y = mouse_pos[1]

    if pygame.mouse.get_pressed()[0]:
        pygame.draw.rect(screen, (255, 0, 0), (pos_x - 15, pos_y - 15, 30, 30), 5)
    else:
        pygame.draw.rect(screen, (255, 0, 0), (pos_x - 30, pos_y - 30, 60, 60), 5)

def mouse():
    mouse_pos = pygame.mouse.get_pos()
    pos_x = mouse_pos[0]
    pos_y = mouse_pos[1]
    return mouse_pos

class templates():
    back = 0
    #Templates
    def frame(self,bx, by, laenge, hoehe,farbe_bg, farbe_fr, text, text_size):
        font = pygame.font.SysFont('''Arial Baltic''', text_size)

        pygame.draw.rect(screen, farbe_fr, (bx, by, laenge, hoehe), 5)

        text_surface = font.render(text, True, farbe_fr)
        screen.blit(text_surface, ((bx + 50), (by + 20)))

    def textfild(self,bx, by, laenge, hoehe, farbe,text, text_size):
        font = pygame.font.SysFont('''Arial Baltic''', text_size)
        pygame.draw.rect(screen, farbe, (bx, by, laenge, hoehe))
        text_surface = font.render(text, True, (0,0,0))
        screen.blit(text_surface, ((bx + 50), (by + 10)))

    def button(self,bx, by, laenge, hoehe, farbe_normal, farbe_aktiv, text, text_size):
        font = pygame.font.SysFont('''Arial Baltic''', text_size)

        if (mouse()[0] > bx and mouse()[0] < bx + laenge and mouse()[1] > by and mouse()[1] < by + hoehe):
            button = pygame.draw.rect(screen, farbe_aktiv, (bx, by, laenge, hoehe))
            border = pygame.draw.rect(screen,  farbe_normal, (bx, by, laenge, hoehe), 5)
            text_surface = font.render(text, True, (0,0,0))
            text_rec = text_surface.get_rect(center=(button.center))

        else:
            button = pygame.draw.rect(screen, farbe_normal, (bx, by, laenge, hoehe))
            border = pygame.draw.rect(screen,  farbe_aktiv, (bx, by, laenge, hoehe), 5)
            text_surface = font.render(text, True, (farbe_aktiv))
            text_rec = text_surface.get_rect(center=(button.center))

        screen.blit(text_surface, text_rec)
        return button

    def sound_volume(self,bx, by, laenge, hoehe, farbe_normal, farbe_aktiv, vol):
        #2
        bx_2 = bx + 125
        #3
        bx_3 = bx + 250
        #4
        bx_4 = bx + 375

        selcetion = 4

        if (mouse()[0] > bx and mouse()[0] < bx + 100 and mouse()[1] > by and mouse()[1] < by + hoehe):
            pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
            selcetion = 1
            # Wenn maus dann Lautärke
        elif (mouse()[0] > bx_2 and mouse()[0] < bx_2 + 100 and mouse()[1] > by and mouse()[1] < by + hoehe):
            pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx_2, by, 100, hoehe))
            selcetion = 2
        elif (mouse()[0] > bx_3 and mouse()[0] < bx_3 + 100 and mouse()[1] > by and mouse()[1] < by + hoehe):
            pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx_2, by, 100, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx_3, by, 100, hoehe))
            selcetion = 3
        elif (mouse()[0] > bx_4 and mouse()[0] < bx_4 + 100 and mouse()[1] > by and mouse()[1] < by + hoehe):
            pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx_2, by, 100, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx_3, by, 100, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx_4, by, 100, hoehe))
            selcetion = 4
        else:
            selcetion = None

        if not (mouse()[0] > bx and mouse()[0] < bx + laenge and mouse()[1] > by and mouse()[1] < by + hoehe):
            if vol == 0.10:
                pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
            if vol == 0.40:
                pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
                pygame.draw.rect(screen, farbe_aktiv, (bx_2, by, 100, hoehe))
            if vol == 0.60:
                pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
                pygame.draw.rect(screen, farbe_aktiv, (bx_2, by, 100, hoehe))
                pygame.draw.rect(screen, farbe_aktiv, (bx_3, by, 100, hoehe))
            if vol == 1:
                pygame.draw.rect(screen, farbe_aktiv, (bx, by, 100, hoehe))
                pygame.draw.rect(screen, farbe_aktiv, (bx_2, by, 100, hoehe))
                pygame.draw.rect(screen, farbe_aktiv, (bx_3, by, 100, hoehe))
                pygame.draw.rect(screen, farbe_aktiv, (bx_4, by, 100, hoehe))


        #1
        pygame.draw.rect(screen, farbe_normal, (bx, by, 100, hoehe), 5)
        pygame.draw.rect(screen, farbe_normal, (bx_2, by, 100, hoehe), 5)
        pygame.draw.rect(screen, farbe_normal, (bx_3, by, 100, hoehe), 5)
        pygame.draw.rect(screen, farbe_normal, (bx_4, by, 100, hoehe), 5)

        return selcetion

    def button_change(self,bx, by, laenge, hoehe, farbe_normal, farbe_aktiv, text, text_size):
        font = pygame.font.SysFont('''Arial Baltic''', text_size)
        b_l = False
        b_r = False

        #left choice
        if ((mouse()[0] > bx) and (mouse()[0] < bx + 60) and (mouse()[1] > by) and (mouse()[1] < by + hoehe)):
            pygame.draw.rect(screen, farbe_aktiv, (bx, by, 60, hoehe))
            pygame.draw.rect(screen, farbe_normal, (bx, by, 60, hoehe), 5)
            b_l = True

        else:
            pygame.draw.rect(screen, farbe_normal, (bx, by, 60, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx, by, 60, hoehe), 5)

        #right choice
        if ((mouse()[0] > (bx +  laenge - 60)) and (mouse()[0] < bx + laenge) and (mouse()[1] > by) and (mouse()[1] < by + hoehe)):
            pygame.draw.rect(screen, farbe_aktiv, (bx +  laenge - 60, by, 60, hoehe))
            pygame.draw.rect(screen, farbe_normal, (bx +  laenge - 60, by, 60, hoehe), 5)
            b_r = True

        else:
            pygame.draw.rect(screen, farbe_normal, (bx + laenge - 60, by, 60, hoehe))
            pygame.draw.rect(screen, farbe_aktiv, (bx + laenge - 60, by, 60, hoehe), 5)


        if (b_l or b_r):
            pygame.draw.rect(screen, farbe_aktiv, (bx + 65, by, laenge - 65 - 65, hoehe))
        else:
            pygame.draw.rect(screen, farbe_normal, (bx + 65, by, laenge - 65 - 65, hoehe))

        text_surface = font.render(text, True, (0, 0, 0))
        screen.blit(text_surface, ((bx + 65), (by + 10)))

        if b_l:
            return  0
        if b_r:
            return  1

    #Screens
    def breake_screen(self):
        while True:
            screen.fill((0, 0, 0))
            mouse_clickt = False
            for event in pygame.event.get():
                # For Controller
                if event.type == pygame.JOYBUTTONUP:
                    if event.button == 7:
                        return 0

                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if ((event.key == pygame.K_ESCAPE) or (event.key == pygame.K_SPACE)):
                        return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        mouse_clickt = True

            logo()


            button_x = (W / 2 - 250)
            button_y = (H / 2 - 50)

            # Textfeld Pause
            self.textfild(button_x, 250, 500, 60, (0, 155, 155), language.tr.M0(self, 4), 80) #TODO: tr ok

            # Textfeld Vol
            self.textfild(button_x, 340, 500, 65, (0, 155, 155), language.tr.M3(self, 5), 80)  # Textfeld Lautstärke #TODO: tr ok


            sound_bg_vol = self.sound_volume(button_x, 420, 400, 100, (0, 155, 155), (0, 255, 255),
                                             settings.settings.sound_background_vol)  # Sound


            b0 = self.button(button_x, (button_y + 180), 500, 100, (0, 155, 155), (0, 255, 255),
                             language.tr.M0(self, 0), 80) #TODO: tr ok

            b1 = self.button(button_x, (button_y + 310), 500, 100, (0, 155, 155), (0, 255, 255),
                             language.tr.M0(self, 2), 80) #TODO: tr ok

            mouse_cursor()

            if mouse_clickt:
                if b0.collidepoint(mouse()):
                    return 0
                if b1.collidepoint(mouse()):
                    return 1
                # SoundVOl
                if (sound_bg_vol == 1):
                    settings.settings.sound_background_vol = 0.10
                    pygame.mixer.music.set_volume(settings.settings.sound_background_vol)
                if (sound_bg_vol == 2):
                    settings.settings.sound_background_vol = 0.40
                    pygame.mixer.music.set_volume(settings.settings.sound_background_vol)
                if (sound_bg_vol == 3):
                    settings.settings.sound_background_vol = 0.60
                    pygame.mixer.music.set_volume(settings.settings.sound_background_vol)
                if (sound_bg_vol == 4):
                    settings.settings.sound_background_vol = 1
                    pygame.mixer.music.set_volume(settings.settings.sound_background_vol)
            pygame.display.flip()