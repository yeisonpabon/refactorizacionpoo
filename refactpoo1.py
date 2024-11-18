def calcular_area_circulo(radio):
    return 3.14159 * radio * radio

def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

class Forma:
    def area(self):
        raise NotImplementedError("Las subclases deben implementar este método")

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio * self.radio

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Rectangulo(Forma):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

# Ejemplo de uso
formas = [Circulo(5), Cuadrado(4), Rectangulo(3, 6)]

for forma in formas:
    print(f"Área: {forma.area()}")
