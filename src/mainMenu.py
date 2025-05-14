import pygame
import sys
from pygame import gfxdraw
from infrastructure.frameworks.simulator import PhysicsSimulator
from application.containerProyectile import Container
from presentation.vistaProyectile import Simulador

class Button:
    def __init__(self, text, pos, size, font, hover_sound, click_sound):
        self.text = text
        self.pos = pos
        self.size = size
        self.font = font
        self.hover_sound = hover_sound
        self.click_sound = click_sound
        self.rect = pygame.Rect(pos, size)
        self.bg_color = (0, 0, 0, 0)
        self.text_color = (180, 180, 180)
        self.hover_text_color = (255, 255, 255)
        self.active = False
        self.sound_played = False
        self.glow_alpha = 0

    def draw(self, screen):
        surface = pygame.Surface(self.size, pygame.SRCALPHA)
        if self.active:
            self.glow_alpha = min(self.glow_alpha + 15, 100)
        else:
            self.glow_alpha = max(self.glow_alpha - 15, 0)
            
        if self.glow_alpha > 0:
            surface.fill((*self.bg_color[:3], self.glow_alpha))
        
        screen.blit(surface, self.rect)
        
        text_color = self.hover_text_color if self.active else self.text_color
        text_surface = self.font.render(self.text, True, text_color)
        
        if self.active:
            glow_surface = self.font.render(self.text, True, (100, 100, 255))
            for offset in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
                screen.blit(glow_surface, 
                          (self.rect.x + (self.size[0] - text_surface.get_width()) // 2 + offset[0],
                           self.rect.y + (self.size[1] - text_surface.get_height()) // 2 + offset[1]))
        
        screen.blit(text_surface, 
                   (self.rect.x + (self.size[0] - text_surface.get_width()) // 2,
                    self.rect.y + (self.size[1] - text_surface.get_height()) // 2))

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            was_active = self.active
            self.active = self.rect.collidepoint(event.pos)
            
            if self.active and not was_active and not self.sound_played:
                self.hover_sound.set_volume(0.3)
                self.hover_sound.play()
                self.sound_played = True
            elif not self.active:
                self.sound_played = False
                
        if event.type == pygame.MOUSEBUTTONDOWN and self.active:
            self.click_sound.set_volume(0.5)
            self.click_sound.play()
            return True
        return False

class BrightnessControl:
    def __init__(self, pos, size, initial_brightness=1.0):
        self.pos = pos
        self.size = size
        self.brightness = initial_brightness
        self.rect = pygame.Rect(pos, size)
        self.slider_rect = pygame.Rect(
            pos[0] + (size[0] - 20) * initial_brightness,
            pos[1],
            20,
            size[1]
        )
        self.dragging = False
        self.visible = False

    def draw(self, screen):
        if not self.visible:
            return
            
        pygame.draw.rect(screen, (50, 50, 50), self.rect, border_radius=10)
        
        filled_rect = pygame.Rect(
            self.rect.x,
            self.rect.y,
            self.slider_rect.x - self.rect.x + 10,
            self.rect.height
        )
        pygame.draw.rect(screen, (100, 149, 237), filled_rect, border_radius=10)
        
        pygame.draw.rect(screen, (255, 255, 255), self.slider_rect, border_radius=5)
        
        font = pygame.font.SysFont("Arial", 20)
        percentage = int(self.brightness * 100)
        text = font.render(f"{percentage}%", True, (255, 255, 255))
        screen.blit(text, (self.rect.right + 10, self.rect.y))

    def handle_event(self, event):
        if not self.visible:
            return
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                self.update_position(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.update_position(event.pos[0])
            
    def update_position(self, x):
        self.slider_rect.x = max(self.rect.x, min(x - self.slider_rect.width // 2,
                                                 self.rect.right - self.slider_rect.width))
        self.brightness = (self.slider_rect.x - self.rect.x) / (self.rect.width - self.slider_rect.width)

class MainMenu:
    def __init__(self):
        self.running = True
        self.initialize_pygame()

    def initialize_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1350, 840))
        pygame.display.set_caption("Physics Simulator")
        self.background = pygame.image.load("../assets/img/fondo_menu.png")
        self.background = pygame.transform.scale(self.background, (1350, 840))
        self.main_logo = pygame.image.load("../assets/img/logo.png")
        self.main_logo = pygame.transform.scale(self.main_logo, (500, 400))
        self.author_logo = pygame.image.load("../assets/img/author_logo.png")
        self.author_logo = pygame.transform.scale(self.author_logo, (150, 100))
        self.click_sound = pygame.mixer.Sound("../assets/music/Click.mp3")
        self.hover_sound = pygame.mixer.Sound("../assets/music/Desplazamiento.mp3")
        try:
            self.font = pygame.font.Font("C:/Windows/Fonts/segoeui.ttf", 60)
        except:
            self.font = pygame.font.SysFont("Arial", 60)
        button_width = 250
        button_spacing = 60
        start_y = 400
        self.buttons = [
            Button("Tension Solver", ((1350 - button_width) // 2, start_y + 45), (button_width, 50), 
                   self.font, self.hover_sound, self.click_sound),
            Button("Projectile Motion", ((1350 - button_width) // 2, start_y + button_spacing + 60), 
                   (button_width, 50), self.font, self.hover_sound, self.click_sound),
            Button("Brillo", ((1350 - button_width) // 2, start_y + button_spacing * 2 + 75), 
                   (button_width, 50), self.font, self.hover_sound, self.click_sound),
            Button("Exit", ((1350 - button_width) // 2, start_y + button_spacing * 3 + 90), 
                   (button_width, 50), self.font, self.hover_sound, self.click_sound)
        ]
        self.brightness_control = BrightnessControl(
            (800, 600),  # Positioned to the right of "Brillo" button, below its bottom edge
            (150, 20)    # Width 150 pixels, height 20 pixels
        )
        pygame.event.clear()

    def run_tension_solver(self):
        try:
            sim = PhysicsSimulator()
            sim.run()
        except Exception as e:
            print(f"Tension Solver error: {e}")

    def run_projectile_motion(self):
        try:
            container = Container()
            sim = Simulador(container)
            sim.ejecutar()
        except Exception as e:
            print(f"Projectile Motion error: {e}")
        finally:
            pygame.event.clear()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                for button in self.buttons:
                    if button.handle_event(event):
                        if button.text == "Exit":
                            self.running = False
                        elif button.text == "Brillo":
                            self.brightness_control.visible = not self.brightness_control.visible
                        elif button.text == "Tension Solver":
                            current_brightness = self.brightness_control.brightness
                            pygame.event.clear()
                            self.run_tension_solver()
                            self.initialize_pygame()
                            self.brightness_control.brightness = current_brightness
                        elif button.text == "Projectile Motion":
                            current_brightness = self.brightness_control.brightness
                            pygame.event.clear()
                            self.run_projectile_motion()
                            self.initialize_pygame()
                            self.brightness_control.brightness = current_brightness
                self.brightness_control.handle_event(event)
            self.screen.blit(self.background, (0, 0))
            dark_overlay = pygame.Surface((1350, 840))
            dark_overlay.fill((0, 0, 0))
            dark_overlay.set_alpha(int(150 * (1.0 - self.brightness_control.brightness)))
            self.screen.blit(dark_overlay, (0, 0))
            logo_rect = self.main_logo.get_rect(center=(1350 // 2, 200))
            self.screen.blit(self.main_logo, logo_rect)
            author_logo_rect = self.author_logo.get_rect(bottomright=(1330, 820))
            self.screen.blit(self.author_logo, author_logo_rect)
            for button in self.buttons:
                button.draw(self.screen)
            self.brightness_control.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    menu = MainMenu()
    menu.run()