import input_box
import pygame
from screen import templates, mouse_cursor
from fpdf import FPDF
from control_pictures import icon

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN, 1)
W, H = screen.get_size()
active = False

def feedback_screen():


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

    text_surface = font.render("Feedback", True, (0, 255, 255)) #TODO: Text Feedback

    text_rec_res = text_surface.get_rect(center=(p9))

    screen.blit(text_surface, text_rec_res)
    boxen_x = (W / 2) - 400
    input_box1 = input_box.InputBox(boxen_x, 270, 800, 50, (0, 255, 255),"") #Vorschläge
    input_box2 = input_box.InputBox(boxen_x, 400, 800, 50, (0, 255, 255),"") #Fehler
    input_box3 = input_box.InputBox(boxen_x, 530, 800, 50, (0, 255, 255), "") # Rechtshreibfehler

    input_boxes = [input_box1,input_box2, input_box3]
    input_box3.toggel_active()

    done = False
    back_button = templates().button((W / 2) - 250, (H - 150), 500, 100, (0, 155, 155),
                                     (0, 255, 255), "Back", 80)  # TODO: TEXT Return

    while not done:
        # Background
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial",'U', size=12,)
                    pdf.cell(200, 10, txt="Feedback QuGame", ln=1, align="C")

                    pdf.cell(0, 10, txt="Was soll verbessert werden:", ln=2, align="l")
                    '''
                    pdf.cell(500, 10, txt=input_box1.text, ln=3, align="l")
                    pdf.cell(500, 10, txt="Fehler:", ln=4, align="l")
                    pdf.cell(500, 10, txt=input_box2.text, ln=5, align="l")
                    pdf.cell(500, 10, txt="Schreibfehler", ln=6, align="l")
                    pdf.cell(500, 10, txt=input_box3.text, ln=7, align="l")
                    '''

                    pdf.output("Feedback QuGame.pdf")
                    return str(input_box1.text)
                    done = True
            if event.type == pygame.QUIT:
                return str(input_box1.text)
                done = True
            for box in input_boxes:
                box.handle_event(event)

         #Back button
        templates().button((W / 2) - 250, (H - 150), 500, 100, (0, 155, 155),
                           (0, 255, 255), "Erstellen", 80)  # TODO: TEXT Return

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

        text_surface = font.render("Feedback", True, (0, 255, 255))  # TODO: Text Feedback

        text_rec_res = text_surface.get_rect(center=(p9))

        screen.blit(text_surface, text_rec_res)

        #Textfeld
        templates().textfild(boxen_x, 200, 800, 60, (0, 255, 255), "Vorschläge:", 50)  # TODO: Text
        templates().textfild(boxen_x, 330, 800, 60, (0, 255, 255), "Fehlerbeschreibung:", 50)  # TODO: Text
        templates().textfild(boxen_x, 460, 800, 60, (0, 255, 255), "Rechtschreibfehler:", 50)  # TODO: Text

        #imputbox
        for box in input_boxes:
            box.update()

        for box in input_boxes:
            box.draw(screen)

        mouse_cursor()
        pygame.display.update()
        clock.tick(120)

if __name__ == '__main__':
    text  = feedback_screen()
    print(text)
    pygame.quit()