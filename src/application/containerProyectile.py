from infrastructure.interfaces.interfaceProyectile import IPhysicsEngine, IHistorialRepository
from infrastructure.interfaces.physicsProyectile import PhysicsEngine
from .historialProyectile import Historial

class Container:
    def __init__(self):
        self._physics_engine = None
        self._historial = None

    @property
    def physics_engine(self) -> IPhysicsEngine:
        if self._physics_engine is None:
            self._physics_engine = PhysicsEngine()
        return self._physics_engine

    @property
    def historial(self) -> IHistorialRepository:
        if self._historial is None:
            self._historial = Historial()
        return self._historial