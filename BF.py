# Desarrollado por Brayan Baquero y Juliana Castillo
# Asignatura de Inteligencia Artificial 
# Profesor : Manuel Alexander Cadena 
# Universidad de Cundinamarca
# Ingenieria de Sistemas


def busqueda_profunda(grafo, inicio, objetivo):
    pila = []  
    visitados = set()  
    ruta = [] 
    pila.append(inicio) 
    while pila:
        nodo_actual = pila.pop()  
        visitados.add(nodo_actual) 
        ruta.append(nodo_actual)  
        if nodo_actual == objetivo:
            return ruta  
        vecinos = grafo[nodo_actual]  
        for vecino in vecinos:
            if vecino not in visitados:
                pila.append(vecino)  
    return None 

# Para este ejercicio utilizamos el ejemplo de la clase de Inteligencia Artificial
 
grafo = {
    '1': ['2', '3', '7'],
    '2': ['3'],
    '3': ['4', '5'],
    '6': [],
    '7': ['8', '9'],
    '9': ['10', '11']
}

inicio = '1'
objetivo = '9'

ruta_optima = busqueda_profunda(grafo, inicio, objetivo)
print("Ruta óptima:", ruta_optima)