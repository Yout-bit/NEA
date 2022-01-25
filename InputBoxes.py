import pygame

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (124, 33, 166)
        self.text = text
        self.output = ""
        self.txt_surface = pygame.font.SysFont('didot.ttf', 40).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = (134, 81, 158) if self.active else (124, 33, 166)

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.output = self.text
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = pygame.font.SysFont('didot.ttf', 40).render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(pygame.font.SysFont('didot.ttf', 40).render(self.output, True, self.color), (self.rect.x+5, self.rect.y+5+self.rect.height))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)
