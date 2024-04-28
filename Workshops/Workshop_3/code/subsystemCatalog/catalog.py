class Catalog:
    def __init__(self):
        self.vehicles = [] #Inicializa una lista vacia de vehiculos
        self.search_cache = [] #Inicializa una lista vacia de busqueda

    def get_all_vehicles(self): #Metodo para que el usuario pueda ver todos los vehiculos 
        return self.vehicles

    def get_price_by_range(self, min_price, max_price): 
        return [vehicle for vehicle in self.vehicles if min_price <= vehicle.price <= max_price]

    def add_vehicle(self, vehicle): #Metodo que permite que el admin agregue vehiculos a la lista 
        self.vehicles.append(vehicle)

    def delete_vehicle(self, vehicle): #Metodo que permite al admin eliminar vehiculos 
        self.vehicles.remove(vehicle)

    def update_vehicle(self, vehicle): #Metodo que permite al admin pueda actualizar vehiculos 
        # Update vehicle logic here
        pass

    def search_vehicles(self, query): 
        result = [] #Se inicializa una lista de busquedas
        #Hacer una iteracion de la lista de vehiculos
        for vehicle in self.vehicles: 
            if query in vehicle.model or query in vehicle.chassis: #Comprueba si lo que se ha buscado esta en el atributo de modelo "o" chasis
                result.append(vehicle) #Si el modelo o chasis coincide se imprime el vehiculo con esas caracteristicas
        self.search_cache.append(result)
        if len(self.search_cache) > 5:  
            self.search_cache.pop(0) #Si la longitud de la lista es superior a 5 elimina el primer elemento de la lista.
        return result