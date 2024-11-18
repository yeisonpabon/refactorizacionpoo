class Reporte:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    def generar_reporte(self):
        return f"Título: {self.titulo}\nContenido: {self.contenido}"

class GuardarReporte:
    @staticmethod
    def guardar_en_archivo(reporte, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(reporte.generar_reporte())

# Ejemplo de uso
reporte = Reporte("Mi Reporte", "Este es el contenido.")
GuardarReporte.guardar_en_archivo(reporte, "reporte.txt")
