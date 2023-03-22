def busca_custo_uniforme(grafo, inicio, objetivo):
    visitados = set()
    fila_prioritaria = [(0, inicio, [])]
    while fila_prioritaria:
        (custo, no_atual, caminho) = heapq.heappop(fila_prioritaria)
        if no_atual not in visitados:
            visitados.add(no_atual)
            caminho = caminho + [no_atual]
            if no_atual == objetivo:
                return (caminho, custo)
            for proximo_no, custo_aresta in grafo[no_atual].items():
                if proximo_no not in visitados:
                    novo_custo = custo + custo_aresta
                    heapq.heappush(fila_prioritaria, (novo_custo, proximo_no, caminho))
    return None
    
    
grafo = {'A': {'B': 1, 'C': 5},
     'B': {'C': 2, 'D': 2},
     'C': {'D': 4},
     'D': {}}

inicio = 'A'
objetivo = 'D'

caminho, custo = busca_custo_uniforme(grafo, inicio, objetivo)
print('Caminho:', caminho)
print('Custo:', custo)
