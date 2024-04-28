"""

"""

class Logger:
    def __init__(self):
         # Inicializa una lista vacía para almacenar registros de acciones (add, delete, search...)
        self.log = []

    def log_action(self, user, action, vehicle=None):
        self.log.append(f"{user.name} {action} {vehicle.model if vehicle else ''}")

    def get_log(self):
        return self.log