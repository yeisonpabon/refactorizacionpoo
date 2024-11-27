class Vehiculo:
    def __init__(self, velocidad, nombre):
        self.velocidad = velocidad
        self.nombre = nombre

    def calcular_tiempo_viaje(self, distancia):
        tiempo = distancia / self.velocidad
        return f"Tiempo de viaje en {self.nombre}: {tiempo:.2f} horas"

carro = Vehiculo(velocidad=80, nombre="carro")
bicicleta = Vehiculo(velocidad=15, nombre="bicicleta")
motocicleta = Vehiculo(velocidad=20, nombre="motocicleta")

vehiculos = [carro, bicicleta, motocicleta]

distancia = 1000
for vehiculo in vehiculos:
    print(vehiculo.calcular_tiempo_viaje(distancia))

