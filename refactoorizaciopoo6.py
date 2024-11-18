# Clase base
class Vehiculo:
    def calcular_tiempo_viaje(self, distancia):
        raise NotImplementedError("Las subclases deben implementar este método")

# Clases derivadas
class Coche(Vehiculo):
    def calcular_tiempo_viaje(self, distancia):
        velocidad = 80  
        tiempo = distancia / velocidad
        return f"Tiempo de viaje en coche: {tiempo:.2f} horas"

class Bicicleta(Vehiculo):
    def calcular_tiempo_viaje(self, distancia):
        velocidad = 150  
        tiempo = distancia / velocidad
        return f"Tiempo de viaje en bicicleta: {tiempo:.2f} horas"

class Autobus(Vehiculo):
    def calcular_tiempo_viaje(self, distancia):
        velocidad = 20  
        tiempo = distancia / velocidad
        return f"Tiempo de viaje en autobús: {tiempo:.2f} horas"

# Lista de vehículos
vehiculos = [
    Coche(),
    Bicicleta(),
    Autobus()
]

distancia = 1000
for vehiculo in vehiculos:
    print(vehiculo.calcular_tiempo_viaje(distancia))
