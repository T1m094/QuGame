import pygame
import time
class InputBox:

    def __init__(self, x, y, w, h, color, text):
        font = pygame.font.SysFont('''Arial Baltic''', 40)

        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.score = 1
        # Cursor declare
        self.txt_rect = self.txt_surface.get_rect()
        self.cursor = pygame.Rect(self.txt_rect.topright, (3, self.txt_rect.height + 2))

    def toggel_active(selfs):
        selfs.active = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    # Cursor

                    self.txt_rect.size = self.txt_surface.get_size()
                    self.cursor.topleft = self.txt_rect.topright

                    # Limit characters           -20 for border width
                    if self.txt_surface.get_width() > self.rect.w - 15:
                        self.text = self.text[:-1]
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

        # Blit the  cursor
        if self.active:
            if time.time() % 1 > 0.5:
                # bounding rectangle of the text
                text_rect = self.txt_surface.get_rect(topleft = (self.rect.x + 5, self.rect.y + 10))
                # set cursor position
                self.cursor.midleft = text_rect.midright
                pygame.draw.rect(screen, self.color, self.cursor)

    def update(self):
        # Re-render the text.
        if self.active:
            font = pygame.font.SysFont('''Arial Baltic''', 50)
            self.txt_surface = font.render(self.text, True, self.color)