from screen import *
def about_screen(mouse_presses):
    screen.fill((0,0,0))
    button_x = (W / 2 - 250)
    button_y = (H / 2 - 50)

    font = pygame.font.SysFont('''Arial Baltic''', 80)
    font_2 = pygame.font.SysFont('''Arial Baltic''', 40)

    # Print Frame
    #     1                                  5
    # p1______p2                     p5__________p6
    # |        \   2     p9        4 /            |
    # |6        \p3_________________/p4           |8
    # |                  3                        |
    # |p7_________________ 7______________________| p8

    h = -200
    p1 = [(W / 2) - 450, (H / 4) + h]
    p2 = [(W / 2) - 200, (H / 4) + h]
    p3 = [(W / 2) - 150, (H / 4) + 50 + h]
    p4 = [(W / 2) + 150, (H / 4) + 50 + h]
    p5 = [(W / 2) + 200, (H / 4) + h]
    p6 = [(W / 2) + 450, (H / 4) + h]
    p7 = [(W / 2) - 450, H + h + 180]
    p8 = [(W / 2) + 450, H + 180 + h]
    p9 = [(W / 2), (H / 4) + h]

    # Line 1
    pygame.draw.line(screen, (0, 255, 255), p1, p2, 5)
    # Line 2
    pygame.draw.line(screen, (0, 255, 255), p2, p3, 5)
    # Line 3
    pygame.draw.line(screen, (0, 255, 255), p3, p4, 5)
    # Line 4
    pygame.draw.line(screen, (0, 255, 255), p4, p5, 5)
    # Line 5
    pygame.draw.line(screen, (0, 255, 255), p5, p6, 5)
    # Line 6
    pygame.draw.line(screen, (0, 255, 255), p1, p7, 10)
    # Line 7
    pygame.draw.line(screen, (0, 255, 255), p7, p8, 10)
    # Line 8
    pygame.draw.line(screen, (0, 255, 255), p6, p8, 10)

    text_surface = font.render(str(language.tr().M0(6)), True, (0, 255, 255))
    text_rec_res = text_surface.get_rect(center=(p9))
    screen.blit(text_surface, text_rec_res)

    #Content Text
    text = ["QuGame","_____","Sound:","Backgroundmusic Menu", "https://www.musicfox.com/info/kostenlose-gemafreie-musik.php","Timeoutmusic:","https://mixkit.co/free-sound-effects","Itemssounds:","https://soundbible.com/","Yellow Item:","Andreas Bruch","Backgroundmusic Game created by:","Dario Boschetto"," ","developt by:", "Timo Heinz"]

    pos_y = (H / 4) + 50 - 150
    pos_x = ((W / 2) - 435)

    for x in range(len(text)):
        text_rend = font_2.render(str(text[x]), True, (0, 255, 255))
        screen.blit(text_rend, (pos_x, pos_y))
        pos_y += 50

    b0 = templates().button(button_x, (button_y + 450), 500, 100, (0, 155, 155), (0, 255, 255), language.tr().M0(0),
                     80)

    mouse_cursor()

    if mouse_presses:
        if b0.collidepoint(mouse()):
            return 0