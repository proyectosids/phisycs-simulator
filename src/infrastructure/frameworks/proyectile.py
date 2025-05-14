from typing import Dict, List, Tuple
from infrastructure.interfaces.interfaceProyectile import IProyectil, IPhysicsEngine

class Proyectil(IProyectil):
    def __init__(self, x: float, y: float, velocidad: float, angulo: float, physics_engine: IPhysicsEngine):
        self.x = x
        self.y = y  # y inicial es 500 (línea base)
        self.velocidad = velocidad
        self.angulo = angulo
        self.tiempo = 0
        self.trayectoria = [(x, y)]  # Punto inicial
        self.physics_engine = physics_engine
        self.posicion_inicial_y = y  # Guardamos la posición inicial en Y
        self.simulacion_terminada = False

    def actualizar(self, dt: float) -> bool:
        # Si la simulación ya terminó, no actualizamos más
        if self.simulacion_terminada:
            return False
            
        self.tiempo += dt
        delta_x, delta_y = self.physics_engine.calculate_position(self.tiempo, self.velocidad, self.angulo)
        
        # Calculamos las nuevas posiciones
        self.x = self.trayectoria[0][0] + delta_x  # Usamos la posición inicial en X
        self.y = self.posicion_inicial_y - delta_y  # Restamos delta_y porque en pygame Y aumenta hacia abajo
        
        # Verificamos si tocó el suelo
        if self.y >= self.posicion_inicial_y:  # Si llegó o superó la línea base
            self.y = self.posicion_inicial_y  # Aseguramos que no baje del suelo
            self.simulacion_terminada = True
            return False
            
        self.trayectoria.append((self.x, self.y))
        return True

    def obtener_resultados(self) -> Dict:
        return self.physics_engine.calculate_results(self.trayectoria, self.tiempo)