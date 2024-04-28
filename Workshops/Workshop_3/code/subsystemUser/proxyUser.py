"""
Crear una clase de proxyUser para usar el patron de proxy, el cual nos permitirá hacer una indireccion de la clase de catalogo por parte del Usuario
La clase ProxyUser puede implementar un mecanismo de almacenamiento en caché para guardar los resultados de búsquedas y mejorar el rendimiento
"""

class ProxyUser:
    def __init__(self, catalog, user): #Constructor con us parametros de la clase Catalog y User 
        self.catalog = catalog
        self.user = user

    def add_vehicle(self, vehicle):
        if self.user.rol == "Admin":
            self.catalog.add_vehicle(vehicle)
        else: #Si esta tratando de ingresar un usuario comun no puede agregar vehiculos 
            raise PermissionError("Only Admins can add vehicles")

    def delete_vehicle(self, vehicle):
        if self.user.rol == "Admin":
            self.catalog.delete_vehicle(vehicle)
        else:
            raise PermissionError("Only Admins can delete vehicles")

    def update_vehicle(self, vehicle):
        if self.user.rol == "Admin":
            self.catalog.update_vehicle(vehicle)
        else:
            raise PermissionError("Only Admins can update vehicles")

    def search_vehicles(self, query): #Accion realizada por el usuario comun 
        return self.catalog.search_vehicles(query)