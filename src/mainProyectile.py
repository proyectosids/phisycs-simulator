from application.containerProyectile import Container
from presentation.vistaProyectile import Simulador

if __name__ == "__main__":
    container = Container()
    sim = Simulador(container)
    sim.ejecutar()