import math
from .interfaceProyectile import IPhysicsEngine
from typing import Dict, List, Tuple

class PhysicsEngine(IPhysicsEngine):
    def __init__(self, gravity: float = 9.8):
        self.gravity = gravity

    def calculate_position(self, time: float, initial_velocity: float, angle: float) -> Tuple[float, float]:
        angle_rad = math.radians(angle)
        vx = initial_velocity * math.cos(angle_rad)
        vy = initial_velocity * math.sin(angle_rad)
        
        x = vx * time
        y = vy * time - 0.5 * self.gravity * time * time
        
        return (x, y)

    def calculate_results(self, trajectory: List[Tuple[float, float]], time: float, screen_height: float = None) -> Dict:
        # Debug: Print the trajectory y-coordinates to diagnose the 710 issue
        y_coords = [p[1] for p in trajectory]
        print(f"Trajectory y-coordinates: {y_coords}")
        print(f"Raw max y-coordinate: {max(y_coords)}")

        # If screen_height is provided, assume y-coordinates are in screen space (y=0 at top, increasing downward)
        # Convert to simulation space (y=0 at ground, positive upward)
        if screen_height is not None:
            # Convert: y_simulation = screen_height - y_screen
            y_simulation = [screen_height - y for y in y_coords]
            print(f"Converted simulation y-coordinates: {y_simulation}")
            altura_maxima = max(y_simulation) if y_simulation else 0.0
        else:
            # Assume y-coordinates are already in simulation space
            altura_maxima = max(y_coords) if y_coords else 0.0

        # Ensure altura_maxima is non-negative (should be >= 0 in simulation space)
        altura_maxima = max(0.0, altura_maxima)

        # Debug: Print the computed maximum height
        print(f"Calculated Altura máxima: {altura_maxima}")

        return {
            "Tiempo de vuelo": round(time, 2),
            "Alcance": round(trajectory[-1][0] - trajectory[0][0], 2),
            "Altura máxima": round(altura_maxima, 2)
        }