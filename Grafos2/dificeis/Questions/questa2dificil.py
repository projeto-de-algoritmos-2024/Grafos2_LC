class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(list)
        
        # Construindo o grafo
        for u, v, w in edges:
            graph[u].append((v, w + 1))
            graph[v].append((u, w + 1))