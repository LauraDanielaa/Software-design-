# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y5fOnFk1p8GJ5NFHGsbduET7LWkK_uNc
"""

class Motor:

    def __init__(self, nombre: str, tipo_del_motor: str, potencia: int, peso: float):

        self.nombre = nombre
        self.tipo_del_motor = tipo_del_motor
        self.potencia = potencia
        self.peso = peso

    def __str__(self):
        return f"Nombre: {self.nombre}   Tipo del motor: {self.tipo_del_motor} Potencia: {self.potencia}   peso: {self.peso}"

class Vehicle:

    def __init__(self, chasis: str, modelo: str, ano: int, motor: Motor):

        self.__chasis = chasis
        self.__modelo = modelo
        self.__ano = ano
        self.__consumo_gas = None
        self.__motor = motor
        self._calcular_consumo_gas()

        #obtener la informacion de los atributos de la clase Vehiculo

def get_chasis(self) -> str:

        return self.__chasis

def get_modelo(self) -> str:

        return self.__modelo

def get_ano(self) -> int:

        return self.__ano

def get_consumo_gas(self) -> float:

        return self.__consumo_gas

def get_motor(self) -> Motor:

        return self.__motor

def __str__(self):
        return f"Chassis: {self.__chasis}  Model: {self.__modelo}   Year: {self.__ano}   Consumption: {self.__consumo_gas}    Engine: {self.__motor}"

#Metodo para calcular el consumo de combustible

def _calcular_consumo_gas(self):

        calculo_gas = (
            (1.1 * self.__engine.potency)
            + (0.2 * self.__engine.weight)
            - (0.3 if self.__chassis == "A" else 0.5)
        )
        self.__consumo_gas = calculo_gas

class Car(Vehicle):

    def __init__(self, chasis, modelo, ano, motor):
        super().__init__(chasis, modelo, ano, motor)

class Truck(Vehicle):
    def __init__(self, chasis, modelo, ano, motor):
        super().__init__(chasis, modelo, ano, motor)

class Yatch(Vehicle):
    def __init__(self, chasis, modelo, ano, motor):
        super().__init__(chasis, modelo, ano, motor)

class Motorcycle(Vehicle):
    def __init__(self, chasis, modelo, ano, motor):
        super().__init__(chasis, modelo, ano, motor)


        """ Crear un menu para el usuario """

print("Bienvenido usuario, que desea crear: \n 1. Crear un motor\n 2. Crear un carro\n 3. Crear un camion\n 4. Crear un yate\n 5. Crear una Moto\n 6. Exit")

enginees = {}
vehicles = []


def option_1():
    """This function lets create a new engine"""
    nombre = input("Please, write a name to identify the engine:")
    tipo_del_motor = input("Please, write the type of engine:")
    potencia = int(input("Please, write the potency in a integer value for the engine:"))
    peso = float(input("Please, write the weight in a decimal value for the engine:"))
    new_motor = Motor(nombre, tipo_del_motor, potencia, peso)
    enginees[nombre] = new_motor


def create_vehiculo(tipo_vehiculo: str):

    motor_ = input(f"Please, write the name of the engine for the {vehicle_type}:")
    modelo = input(f"Please, write the model for the {vehicle_type}:")
    ano = int(input(f"Please, write the year for the {vehicle_type}:"))
    chasis = input(f"Please, write the chassis (A or B) for the {vehicle_type}:")
    motor = enginees[motor_]
    if vehicle_type == "car":
        vehicles.append(Car(chasis, modelo, ano, motor))
    elif vehicle_type == "truck":
        vehicles.append(Truck(chasis, modelo, ano, motor))
    elif vehicle_type == "yatch":
        vehicles.append(Yatch(chasis, modelo, ano, motor))
    elif vehicle_type == "motorcycle":
        vehicles.append(Motorcycle(chasis, modelo, ano, motor))


def menu():
    """This function represents the menu of the application."""

    print("Bienvenido usuario, que desea crear: \n 1. Crear un motor\n 2. Crear un carro\n 3. Crear un camion\n 4. Crear un yate\n 5. Crear una Moto\n 6. Exit")
option = int(input("Ingrese una opción: "))
while option != 8:
    if option == 1:
        print("creando motor")
    elif option == 2:
        print("Creando carro")
    elif option == 3:
        print("Creando moto")
    elif option == 4:
        print("Viendo todos los vehiculos")
    else:
         print("Opcion no valida")


    option= int(input("Ingrese una opcion"))


    option = int(input())


if __name__ == "__main__":
    menu()