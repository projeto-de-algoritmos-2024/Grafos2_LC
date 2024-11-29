class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Criação do grafo com lista de adjacência
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        
        # Probabilidades máximas iniciais (distâncias)
        max_prob = [0.0] * n
        max_prob[start] = 1.0  # Probabilidade inicial para o nó inicial
        
        # Fila de prioridade (max-heap usando probabilidades negativas)
        pq = [(-1.0, start)]  # (-probabilidade, nó)

        return 0