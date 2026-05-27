# TRABAJO-DE-FARLEY-PALACIOS-MOYA-
TRABAJO  DE CALCULO 
# Problema 4 - Videoteca Digital

# Matriz: [Título, Año, Calificación, Género]

videoteca = [
    ["Interestelar", 2014, 9, "Ciencia Ficción"],
    ["Avatar", 2009, 8, "Acción"],
    ["Joker", 2019, 9, "Drama"],
    ["Toy Story 4", 2019, 8, "Animación"],
    ["The Batman", 2022, 9, "Acción"],
    ["Encanto", 2021, 8, "Animación"],
    ["Duna", 2021, 9, "Ciencia Ficción"]
]

# Función para contar títulos que cumplen condiciones
def contar_titulos(matriz, calificacion_minima, anio_limite):
    
    contador = 0

    for titulo in matriz:
        
        anio = titulo[1]
        calificacion = titulo[2]

        # Condición:
        # Calificación >= umbral
        # Y año >= año límite
        
        if calificacion >= calificacion_minima and anio >= anio_limite:
            contador += 1

    return contador


# Datos de prueba
calificacion_minima = 8
anio_limite = 2019

# Llamado de la función
resultado = contar_titulos(videoteca, calificacion_minima, anio_limite)

# Mostrar resultado
print("Cantidad de títulos que cumplen los criterios:", resultado)
