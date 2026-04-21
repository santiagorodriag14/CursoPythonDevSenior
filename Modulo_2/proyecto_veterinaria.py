from abc import ABC, abstractmethod

class Persona(ABC):
    def mostrar_rol(self):
        pass


class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad

    def mostrar_rol(self):
        return f"{self.nombre} es un veterinario especializado en {self.especialidad}"

    def atender_mascota(self, mascota):
        return f"{self.nombre} está atendiendo a {mascota.nombre}"


class Recepcionista(Persona):
    def mostrar_rol(self):
        return f"{self.nombre} es un recepcionista"


class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascotas = []

    def mostrar_rol(self):
        return f"{self.nombre} es un cliente"

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    
    def mostrar_mascotas(self):
        print(f"Cliente: {self.nombre} tiene las siguientes mascotas:")
        for mascota in self.mascotas:
            print(f"{mascota.nombre} ({mascota.especie})")
                
