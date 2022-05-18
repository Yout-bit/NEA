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
            #If the user clicked on the box, toggles whether its active or not, else deactivtes the box
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            # Change the current colour of the input box when active
            self.colour = (134, 81, 158) if self.active else (124, 33, 166)

        #When the user presses a key and the box is active
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.output = self.text
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                #Update the screen text when the text is changed
                self.txt_surface = pygame.font.SysFont('didot.ttf', 40).render(self.text, True, self.colour)

    def update(self, display):
        self.draw(display)

    def draw(self, screen):
        #Draws: the box, the text beeing entered, and the output text
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        screen.blit(pygame.font.SysFont('didot.ttf', 40).render(self.output, True, self.colour), (self.rect.x+5, self.rect.y+5+self.rect.height))
        pygame.draw.rect(screen, self.colour, self.rect, 2)
