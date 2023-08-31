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
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio = 'A'
objetivo = 'F'

ruta_optima = busqueda_profunda(grafo, inicio, objetivo)
print("Ruta óptima:", ruta_optima)