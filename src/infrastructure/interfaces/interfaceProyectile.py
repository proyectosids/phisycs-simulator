from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

class IPhysicsEngine(ABC):
    @abstractmethod
    def calculate_position(self, time: float, initial_velocity: float, angle: float) -> Tuple[float, float]:
        pass

    @abstractmethod
    def calculate_results(self, trajectory: List[Tuple[float, float]], time: float) -> Dict:
        pass

class IHistorialRepository(ABC):
    @abstractmethod
    def save(self, data: Dict) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass

class IProyectil(ABC):
    @abstractmethod
    def actualizar(self, dt: float) -> bool:
        pass

    @abstractmethod
    def obtener_resultados(self) -> Dict:
        pass