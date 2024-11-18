def procesar_cadena(dato):
    print(f"Procesando cadena: {dato}")

def procesar_entero(dato):
    print(f"Procesando entero: {dato}")

def procesar_lista(dato):
    print("Procesando lista:")
    for elemento in dato:
        print(f" - {elemento}")

def procesar_datos(dato):
    procesadores = {
        str: procesar_cadena,  # Si el tipo es cadena, usa procesar_cadena
        int: procesar_entero,  # Si el tipo es entero, usa procesar_entero
        list: procesar_lista   # Si el tipo es lista, usa procesar_lista
    }
    
    procesador = procesadores.get(type(dato), lambda x: print("¡Tipo de dato desconocido!"))
    
    procesador(dato)

# Ejemplos de uso

procesar_datos("Hola")
procesar_datos(123)
procesar_datos([1, 2, 3])

procesar_datos(3.14)
