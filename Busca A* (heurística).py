from heapq import heappush, heappop

def a_estrela(grafo, inicio, objetivo, heuristica):
    fila_prioritaria = [(0, inicio)]
    visitados = set()
    caminho = {}
    custo_atual = {inicio: 0}

    while fila_prioritaria:
        (custo, nodo) = heappop(fila_prioritaria)
        if nodo == objetivo:
            return construir_caminho(caminho, inicio, objetivo)

        visitados.add(nodo)
        for vizinho, peso in grafo[nodo].items():
            if vizinho in visitados:
                continue
            custo_atual_vizinho = custo_atual[nodo] + peso
            if vizinho not in custo_atual or custo_atual_vizinho < custo_atual[vizinho]:
                custo_atual[vizinho] = custo_atual_vizinho
                prioridade = custo_atual_vizinho + heuristica(vizinho, objetivo)
                heappush(fila_prioritaria, (prioridade, vizinho))
                caminho[vizinho] = nodo

    return None

def construir_caminho(caminho, inicio, objetivo):
    if objetivo not in caminho:
        return None

    atual = objetivo
    caminho_total = [atual]
    while atual != inicio:
        atual = caminho[atual]
        caminho_total.append(atual)
    caminho_total.reverse()

    return caminho_total
  
  
  
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'C': -1, 'D': 1},
    'C': {'D': 2},
    'D': {'B': -4, 'E': 3},
    'E': {}
}

# Busca A* utilizando a distância em linha reta entre os nós como heurística
# O objetivo é chegar no nó 'E' partindo do nó 'A'
distancias = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 1,
    'E': 0
}

def heuristica(nodo, objetivo):
    return distancias[nodo]

caminho = busca_a_estrela(grafo, 'A', 'E', heuristica)
print(caminho)  # Resultado esperado: ['A', 'C', 'D', 'E']
