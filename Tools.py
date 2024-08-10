import pygame

from ColorPalette import *

class CreateSurface:
    def __init__(self, screen, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.screen = screen

        self.surface = pygame.Surface((self.width, self.height))
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.x = self.x
        self.surface_rect.y = self.y

    def DrawSurface(self):
        self.surface.fill(self.color)
        self.screen.blit(self.surface, self.surface_rect)

class CreateLabel:
    def __init__(self, text, color, font, fontsize, AntiAliasing, x, y):
        self.text = text
        self.color = color
        self.size = fontsize
        self.AntiAliasing = AntiAliasing
        self.font = pygame.font.Font(f"Fonts/{font}", self.size)
        self.surface = self.RenderFont()
        self.surface_rect = self.surface.get_rect()
        self.surface_rect.topleft = (x, y)

    def RenderFont(self):
        return (self.font.render(self.text, self.AntiAliasing, self.color))
    
    def DrawLabel(self, screen):
        # pygame.draw.rect(screen, "Green", self.surface_rect, 2, 5)
        screen.blit(self.surface, self.surface_rect)

class Button:
    def __init__(self, screen, text, width, height, pos, elevation, font, onclick):
        self.screen = screen
        self.font = font
        self.onClick = onclick
        # Core Attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamicElevation = elevation
        self.original_y_pos = pos[1]
        # Top Rect
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_rect.center = pos
        self.top_color = collegeNavy

        # Bottom Rect
        self.bottom_rect = pygame.Rect(pos, (width, elevation))
        self.bottom_color = BroncosNavy

        # Text
        self.text_surf = self.font.render(text, True, white)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
    
    def draw(self):
        # Elevation Logic
        self.top_rect.y = self.original_y_pos - self.dynamicElevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamicElevation

        pygame.draw.rect(self.screen, self.bottom_color, self.bottom_rect, border_radius=20)
        pygame.draw.rect(self.screen, self.top_color, self.top_rect, border_radius= 20)
        self.screen.blit(self.text_surf, self.text_rect)

        self.check_Click()

    def check_Click(self):
        mouse_pos = pygame.mouse.get_pos()
        if (self.top_rect.collidepoint(mouse_pos)):
            self.top_color = Lust
            if(pygame.mouse.get_pressed()[0]):
                self.dynamicElevation = 0
                self.pressed = True
            else:
                self.dynamicElevation = self.elevation
                if self.pressed == True:
                    self.onClick()
                    self.pressed = False
        else:
            self.dynamicElevation = self.elevation
            self.top_color = collegeNavy