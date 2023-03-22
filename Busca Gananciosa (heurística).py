import heapq

def busca_gananciosa(grafo, inicio, objetivo, heuristica):
    visitados = set()
    fila_prioritaria = [(heuristica(inicio, objetivo), inicio, [])]

    while fila_prioritaria:
        (custo, no_atual, caminho) = heapq.heappop(fila_prioritaria)

        if no_atual == objetivo:
            return caminho + [no_atual]

        if no_atual not in visitados:
            visitados.add(no_atual)

            for (proximo_no, custo) in grafo[no_atual].items():
                if proximo_no not in visitados:
                    novo_custo = heuristica(proximo_no, objetivo)
                    heapq.heappush(fila_prioritaria, (novo_custo, proximo_no, caminho + [no_atual]))

    return None
  
  
grafo = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

# Busca gananciosa utilizando a distância em linha reta entre os nós
# O objetivo é chegar no nó 'F' partindo do nó 'A'
distancias = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 1,
    'E': 1,
    'F': 0
}

busca_gananciosa(grafo, 'A', 'F', lambda no, objetivo: distancias[objetivo])
