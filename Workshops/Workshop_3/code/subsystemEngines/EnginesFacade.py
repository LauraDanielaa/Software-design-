"""
 Engines Facade proporciona una interfaz simplificada para crear y configurar objetos Engine

"""
from subsystemEngines.factories import EngineFactory

class EnginesFacade:
    def __init__(self): #Constructor de la clase
        self.engine_factory = EngineFactory()

    def get_engine(self, engine_type, price_engine):
        engine = self.engine_factory.create_engine(engine_type)
        engine.set_price(price_engine)
        return engine