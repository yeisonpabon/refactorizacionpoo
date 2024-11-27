class Vehiculo:
    def __init__(self, velocidad, nombre):
        self.velocidad = velocidad
        self.nombre = nombre

    def calcular_tiempo_viaje(self, distancia):
        tiempo = distancia / self.velocidad
        return f"Tiempo de viaje en {self.nombre}: {tiempo:.2f} horas"


# Instancias específicas de vehículos
coche = Vehiculo(velocidad=80, nombre="coche")
bicicleta = Vehiculo(velocidad=15, nombre="bicicleta")
autobus = Vehiculo(velocidad=20, nombre="autobús")

# Lista de vehículos
vehiculos = [coche, bicicleta, autobus]

# Cálculo de tiempos de viaje
distancia = 1000
for vehiculo in vehiculos:
    print(vehiculo.calcular_tiempo_viaje(distancia))

