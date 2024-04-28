"""
Creacion del patron de Facade que actúa como una fachada que oculta la complejidad de crear y gestionar objetos Vehículo y sus motores
El usuario no tendra que interactuar con la complejidad 
"""
from vehicles import Vehicle 
from subsystemEngines.EnginesFacade import EnginesFacade #importando desde otra carpeta 
from FlyweightVehicles import Flyweight

class VehiclesFacade: 
    def __init__(self): 
        self.engines_facade = EnginesFacade()
        self.vehicles = []

    def create_vehicle(self, engine_type):
        vehicle = Vehicle(self.engines_facade)
        vehicle.create_engine(engine_type)
        self.vehicles.append(vehicle)
