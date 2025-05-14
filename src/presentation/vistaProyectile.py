import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from infrastructure.frameworks.proyectile import Proyectil
from application.containerProyectile import Container
import requests

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

class Simulador:
    def __init__(self, container: Container):
        self.container = container
        self.API_URL = "http://localhost:5000/api/simulations"
        # Defer pygame.init() to ejecutar to ensure display is ready
        self.ancho, self.alto = 1350, 840
        self.clock = pygame.time.Clock()
        self.proyectil = None
        self.mostrar_rastro = False
        self.resultados = None
        self.simulacion_activa = False
        self.proyectil_finalizado = False
        self.mostrar_historial = False
        self.historial_data = []
        self.historial_scroll = 0
        self.max_items_visible = 8
        self.panel_y = self.alto - 120
        self.panel_altura = 120
        self.suelo_y = self.panel_y

    def initialize_resources(self):
        # Initialize display and resources
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto), pygame.RESIZABLE)
        pygame.display.set_caption("Simulador de Proyectiles")
        self.fondo = pygame.image.load("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrioNew/assets/img/fondoProyectile.png")
        self.fondo = pygame.transform.scale(self.fondo, (self.ancho, self.alto)) 
        self.imagen_trayectoria = pygame.image.load("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrioNew/assets/img/p2.png")
        ancho_imagen = int(self.ancho * 0.20)
        alto_imagen = int(ancho_imagen * (220/240))
        self.imagen_trayectoria = pygame.transform.scale(self.imagen_trayectoria, (ancho_imagen, alto_imagen))
        self.pos_imagen_trayectoria = (-60, 600)
        self.imagen_proyectil = pygame.image.load("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrioNew/assets/img/Ball.png")
        self.imagen_proyectil = pygame.transform.scale(self.imagen_proyectil, (35, 25))
        self.click_sound = pygame.mixer.Sound("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrioNew/assets/music/Click.mp3")
        self.hover_sound = pygame.mixer.Sound("C:/Users/carli/Documents/Proyectos/SimuladorCuerposEquilibrioNew/assets/music/Desplazamiento.mp3")
        try:
            self.font = pygame.font.Font("C:/Windows/Fonts/segoeui.ttf", 28)
        except:
            self.font = pygame.font.SysFont("Arial", 28)
        self.panel_control = pygame.Rect(1, self.panel_y, self.ancho - 40, self.panel_altura)
        slider_x = 150
        slider_ancho = int(self.ancho * 0.2)
        text_x = slider_x + slider_ancho + 20
        self.slider_angulo = Slider(
            self.pantalla, slider_x, self.panel_y + 20, slider_ancho, 15,
            min=0, max=90, step=1, initial=45, colour=(180, 180, 180), handleColour=(100, 100, 255)
        )
        self.texto_angulo = TextBox(
            self.pantalla, text_x, self.panel_y + 20, 60, 25,
            fontSize=16, colour=(240, 240, 240), borderColour=(180, 180, 180), textColour=(0, 0, 0), radius=5
        )
        self.slider_velocidad = Slider(
            self.pantalla, slider_x, self.panel_y + 55, slider_ancho, 15,
            min=10, max=100, step=1, initial=50, colour=(180, 180, 180), handleColour=(100, 100, 255)
        )
        self.texto_velocidad = TextBox(
            self.pantalla, text_x, self.panel_y + 55, 60, 25,
            fontSize=16, colour=(240, 240, 240), borderColour=(180, 180, 180), textColour=(0, 0, 0), radius=5
        )
        boton_ancho = 110
        boton_alto = 35
        espacio = 20
        x_inicio = text_x + 100
        self.botones = {
            "Start": Button("Start", (x_inicio, self.panel_y + 30), (boton_ancho, boton_alto), 
                            self.font, self.hover_sound, self.click_sound),
            "Historial": Button("Historial", (x_inicio + boton_ancho + espacio, self.panel_y + 30), 
                               (boton_ancho, boton_alto), self.font, self.hover_sound, self.click_sound),
            "Guardar": Button("Guardar", (x_inicio + (boton_ancho + espacio) * 2, self.panel_y + 30), 
                              (boton_ancho, boton_alto), self.font, self.hover_sound, self.click_sound),
            "Rastro": Button("Rastro", (x_inicio + (boton_ancho + espacio) * 3, self.panel_y + 30), 
                             (boton_ancho, boton_alto), self.font, self.hover_sound, self.click_sound),
            "Resultados": Button("Resultados", (x_inicio + (boton_ancho + espacio) * 4, self.panel_y + 30), 
                                 (boton_ancho, boton_alto), self.font, self.hover_sound, self.click_sound),
            "Regresar": Button("Regresar", (x_inicio + (boton_ancho + espacio) * 5, self.panel_y + 30), 
                               (boton_ancho, boton_alto), self.font, self.hover_sound, self.click_sound)
        }
        self.mostrar_resultados = False
        self.resultados_guardados = False

    def cargar_historial(self):
        try:
            response = requests.get(f"{self.API_URL}?type=projectile")
            if response.status_code == 200:
                self.historial_data = response.json()
            else:
                print("Error al cargar el historial")
        except Exception as e:
            print(f"Error al conectar con la API: {str(e)}")

    def dibujar_ventana_historial(self):
        if not self.mostrar_historial:
            return
        s = pygame.Surface((self.ancho, self.alto))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.pantalla.blit(s, (0, 0))
        ventana_ancho = int(self.ancho * 0.6)
        ventana_alto = int(self.alto * 0.7)
        ventana_x = (self.ancho - ventana_ancho) // 2
        ventana_y = (self.alto - ventana_alto) // 2
        ventana_rect = pygame.Rect(ventana_x, ventana_y, ventana_ancho, ventana_alto)
        pygame.draw.rect(self.pantalla, (240, 240, 240), ventana_rect)
        pygame.draw.rect(self.pantalla, (180, 180, 180), ventana_rect, 2)
        fuente = pygame.font.Font(None, 40)
        titulo = fuente.render("Historial de Simulaciones", True, (0, 0, 0))
        titulo_rect = titulo.get_rect(center=(ventana_x + ventana_ancho // 2, ventana_y + 30))
        self.pantalla.blit(titulo, titulo_rect)
        fuente_items = pygame.font.Font(None, 26)
        item_altura = 70
        item_padding = 10
        y_pos = ventana_y + 70
        max_items = min(self.max_items_visible, (ventana_alto - 150) // item_altura)
        for i in range(self.historial_scroll, min(self.historial_scroll + max_items, len(self.historial_data))):
            sim = self.historial_data[i]
            item_rect = pygame.Rect(ventana_x + 20, y_pos, ventana_ancho - 40, item_altura - item_padding)
            mouse_pos = pygame.mouse.get_pos()
            if item_rect.collidepoint(mouse_pos):
                pygame.draw.rect(self.pantalla, (200, 200, 255), item_rect)
            pygame.draw.rect(self.pantalla, (180, 180, 180), item_rect, 1)
            texto = f"Velocidad: {sim['data']['initialVelocity']} m/s, Ángulo: {sim['data']['angle']}°"
            texto2 = f"Altura máx: {sim['data']['maxHeight']}m, Alcance: {sim['data']['range']}m"
            self.pantalla.blit(fuente_items.render(texto, True, (0, 0, 0)), (item_rect.x + 10, item_rect.y + 10))
            self.pantalla.blit(fuente_items.render(texto2, True, (0, 0, 0)), (item_rect.x + 10, item_rect.y + 35))
            y_pos += item_altura
        boton_nav_ancho = 120
        boton_nav_alto = 40
        boton_y = ventana_y + ventana_alto - 60
        if self.historial_scroll > 0:
            boton_ant_rect = pygame.Rect(ventana_x + ventana_ancho // 2 - boton_nav_ancho - 20, boton_y, boton_nav_ancho, boton_nav_alto)
            pygame.draw.rect(self.pantalla, (100, 100, 255), boton_ant_rect, border_radius=8)
            texto_ant = fuente_items.render("Anterior", True, (255, 255, 255))
            texto_ant_rect = texto_ant.get_rect(center=boton_ant_rect.center)
            self.pantalla.blit(texto_ant, texto_ant_rect)
        if self.historial_scroll + max_items < len(self.historial_data):
            boton_sig_rect = pygame.Rect(ventana_x + ventana_ancho // 2 + 20, boton_y, boton_nav_ancho, boton_nav_alto)
            pygame.draw.rect(self.pantalla, (100, 100, 255), boton_sig_rect, border_radius=8)
            texto_sig = fuente_items.render("Siguiente", True, (255, 255, 255))
            texto_sig_rect = texto_sig.get_rect(center=boton_sig_rect.center)
            self.pantalla.blit(texto_sig, texto_sig_rect)
        boton_cerrar_rect = pygame.Rect(ventana_x + ventana_ancho - 40, ventana_y + 15, 30, 30)
        pygame.draw.rect(self.pantalla, (255, 100, 100), boton_cerrar_rect, border_radius=15)
        texto_x = fuente_items.render("X", True, (255, 255, 255))
        texto_x_rect = texto_x.get_rect(center=boton_cerrar_rect.center)
        self.pantalla.blit(texto_x, texto_x_rect)
        self.rect_boton_cerrar = boton_cerrar_rect
        self.rect_boton_anterior = boton_ant_rect if self.historial_scroll > 0 else None
        self.rect_boton_siguiente = boton_sig_rect if self.historial_scroll + max_items < len(self.historial_data) else None
        self.rect_items_historial = []
        y_pos = ventana_y + 70
        for i in range(self.historial_scroll, min(self.historial_scroll + max_items, len(self.historial_data))):
            self.rect_items_historial.append(pygame.Rect(ventana_x + 20, y_pos, ventana_ancho - 40, item_altura - item_padding))
            y_pos += item_altura

    def restaurar_simulacion(self, simulacion):
        self.slider_velocidad.setValue(simulacion['data']['initialVelocity'])
        self.slider_angulo.setValue(simulacion['data']['angle'])
        self.mostrar_historial = False
        self.proyectil = Proyectil(50, self.suelo_y - 10, simulacion['data']['initialVelocity'], simulacion['data']['angle'], self.container.physics_engine)
        self.simulacion_activa = True
        self.proyectil_finalizado = False

    def guardar_en_api(self, resultados: dict) -> None:
        try:
            datos = {
                "type": "projectile",
                "data": {
                    "initialVelocity": self.slider_velocidad.getValue(),
                    "angle": self.slider_angulo.getValue(),
                    "flightTime": resultados["Tiempo de vuelo"],
                    "maxHeight": resultados["Altura máxima"],
                    "range": resultados["Alcance"]
                }
            }
            response = requests.post(self.API_URL, json=datos)
            if response.status_code == 201:
                print("Simulación guardada exitosamente en la API")
            else:
                print(f"Error al guardar en la API: {response.status_code}")
        except Exception as e:
            print(f"Error al conectar con la API: {str(e)}")

    def dibujar_interfaz(self):
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.imagen_trayectoria, self.pos_imagen_trayectoria)
        pygame.draw.line(self.pantalla, (180, 180, 180), (10, self.suelo_y), (self.ancho - 10, self.suelo_y), 2)
        pygame.draw.rect(self.pantalla, (220, 220, 220), self.panel_control, border_radius=15)
        pygame.draw.rect(self.pantalla, (180, 180, 180), self.panel_control, 2, border_radius=15)
        fuente = pygame.font.Font(None, 28)
        texto_ang = fuente.render("Ángulo:", True, (60, 60, 60))
        texto_vel = fuente.render("Velocidad:", True, (60, 60, 60))
        self.pantalla.blit(texto_ang, (50, self.panel_y + 20))
        self.pantalla.blit(texto_vel, (30, self.panel_y + 55))
        self.texto_angulo.setText(f"{int(self.slider_angulo.getValue())}°")
        self.texto_velocidad.setText(f"{int(self.slider_velocidad.getValue())} m/s")
        for button in self.botones.values():
            button.draw(self.pantalla)
        if self.mostrar_resultados and self.resultados:
            resultado_rect = pygame.Rect(20, 20, 400, 140)
            pygame.draw.rect(self.pantalla, (50, 50, 50, 180), resultado_rect, border_radius=15)
            pygame.draw.rect(self.pantalla, (200, 200, 200), resultado_rect, 2, border_radius=15)
            font = pygame.font.Font(None, 28)
            titulo_res = font.render("RESULTADOS DE LA SIMULACIÓN", True, (255, 255, 255))
            self.pantalla.blit(titulo_res, (40, 35))
            textos = [
                f"Tiempo de vuelo: {self.resultados['Tiempo de vuelo']}s",
                f"Alcance: {self.resultados['Alcance']}m",
                f"Altura máxima: {self.resultados['Altura máxima']}m"
            ]
            for i, texto in enumerate(textos):
                render = font.render(texto, True, (255, 255, 255))
                self.pantalla.blit(render, (40, 70 + i * 30))
        if self.proyectil:
            self.pantalla.blit(self.imagen_proyectil, (self.proyectil.x, self.proyectil.y))

    def dibujar_simulacion(self):
        if self.proyectil and (self.mostrar_rastro or self.proyectil_finalizado) and len(self.proyectil.trayectoria) > 1:
            for i in range(1, len(self.proyectil.trayectoria)):
                p1 = self.proyectil.trayectoria[i-1]
                p2 = self.proyectil.trayectoria[i]
                pygame.draw.line(self.pantalla, (100, 200, 100), 
                               (int(p1[0]), int(p1[1])),
                               (int(p2[0]), int(p2[1])), 3)

    def manejar_eventos(self, eventos):
        for event in eventos:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.VIDEORESIZE:
                self.ancho, self.alto = event.w, event.h
                self.pantalla = pygame.display.set_mode((self.ancho, self.alto), pygame.RESIZABLE)
                self.panel_y = self.alto - 120
                self.suelo_y = self.panel_y
                self.initialize_resources()  # Reinitialize resources on resize
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.mostrar_historial:
                    if self.rect_boton_cerrar.collidepoint(pos):
                        self.mostrar_historial = False
                    elif self.rect_boton_anterior and self.rect_boton_anterior.collidepoint(pos):
                        self.historial_scroll -= self.max_items_visible
                    elif self.rect_boton_siguiente and self.rect_boton_siguiente.collidepoint(pos):
                        self.historial_scroll += self.max_items_visible
                    else:
                        for i, rect in enumerate(self.rect_items_historial):
                            if rect.collidepoint(pos):
                                self.restaurar_simulacion(self.historial_data[self.historial_scroll + i])
                                break
                else:
                    for name, button in self.botones.items():
                        if button.handle_event(event):
                            if name == "Start":
                                self.proyectil = Proyectil(50, self.suelo_y - 10, self.slider_velocidad.getValue(), 
                                                          self.slider_angulo.getValue(), self.container.physics_engine)
                                self.simulacion_activa = True
                                self.proyectil_finalizado = False
                            elif name == "Historial":
                                self.mostrar_historial = True
                                self.cargar_historial()
                            elif name == "Guardar" and self.proyectil:
                                resultados = self.proyectil.obtener_resultados()
                                self.guardar_en_api(resultados)
                            elif name == "Rastro":
                                self.mostrar_rastro = not self.mostrar_rastro
                            elif name == "Resultados":
                                self.mostrar_resultados = not self.mostrar_resultados
                                if self.proyectil:
                                    self.resultados_guardados = True
                            elif name == "Regresar":
                                return False
            else:
                for button in self.botones.values():
                    button.handle_event(event)
        pygame_widgets.update(eventos)
        return True

    def ejecutar(self):
        pygame.init()  # Initialize Pygame at the start
        self.initialize_resources()  # Initialize display and resources
        corriendo = True
        while corriendo:
            eventos = pygame.event.get()
            corriendo = self.manejar_eventos(eventos)
            self.dibujar_interfaz()
            self.dibujar_simulacion()
            if self.proyectil and self.simulacion_activa:
                if not self.proyectil.actualizar(0.1):
                    self.resultados = self.proyectil.obtener_resultados()
                    self.simulacion_activa = False
                    self.proyectil_finalizado = True
                    print("\nResultados de la simulación:")
                    for clave, valor in self.resultados.items():
                        print(f"{clave}: {valor}")
                    self.resultados_guardados = False
            if self.mostrar_historial:
                self.dibujar_ventana_historial()
            pygame_widgets.update(eventos)
            pygame.display.flip()
            self.clock.tick(60)