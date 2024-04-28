"""
Para el manejo de uso de memoria se usa el patron de Flyweight
Este permite almacenar los objetos inmutables y se repiten los cuales con los motores

"""


from subsystemEngines.EnginesFacade import EnginesFacade

class Flyweight:
    _engines_facade = EnginesFacade()

    def __init__(self):
        self.engine = None

    def create_engine(self, engine_type):
        self.engine = self._engines_facade.create_engine(engine_type)

  