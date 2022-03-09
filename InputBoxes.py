import pygame

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.colour = (124, 33, 166)
        self.text = text
        self.output = ""
        self.txt_surface = pygame.font.SysFont('didot.ttf', 40).render(text, True, self.colour)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current colour of the input box.
            self.colour = (134, 81, 158) if self.active else (124, 33, 166)

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
                self.txt_surface = pygame.font.SysFont('didot.ttf', 40).render(self.text, True, self.colour)

    def update(self, display):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        self.draw(display)

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(pygame.font.SysFont('didot.ttf', 40).render(self.output, True, self.colour), (self.rect.x+5, self.rect.y+5+self.rect.height))
        # Blit the rect.
        pygame.draw.rect(screen, self.colour, self.rect, 2)
