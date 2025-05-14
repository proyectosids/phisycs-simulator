import json
from datetime import datetime
from typing import Dict, List
from infrastructure.interfaces.interfaceProyectile import IHistorialRepository

class Historial(IHistorialRepository):
    def __init__(self, archivo: str = "historial.json"):
        self.archivo = archivo

    def save(self, datos: Dict) -> None:
        try:
            historial = self.get_all()
        except FileNotFoundError:
            historial = []
        
        datos["Fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        historial.append(datos)

        with open(self.archivo, "w") as file:
            json.dump(historial, file, indent=4)
        print("Simulación guardada en el historial.")

    def get_all(self) -> List[Dict]:
        try:
            with open(self.archivo, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def mostrar_historial(self) -> None:
        historial = self.get_all()
        if not historial:
            print("No hay historial de simulaciones.")
            return
            
        print("\n=== Historial de Simulaciones ===")
        for i, entrada in enumerate(historial, 1):
            print(f"\nSimulación {i}:")
            for clave, valor in entrada.items():
                print(f"  {clave}: {valor}")