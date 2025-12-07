import math
import heapq

def dijkstra(adj, src):
    """
    Single-source Dijkstra using a binary heap (heapq).
    adj: adjacency list, adj[u] = list of (v, weight) with non-negative weights.
    src: source vertex index.
    Returns:
        dist: list of shortest distances from src
        parent: predecessor-in-path array (for path reconstruction)
    """
    n = len(adj)
    INF = math.inf
    dist = [INF] * n
    parent = [-1] * n
    dist[src] = 0

    pq = [(0.0, src)] # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue

        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, parent


def all_pairs_shortest_paths_dijkstra(adj):
    """
    All-pairs shortest paths via repeated Dijkstra.
    Returns:
        dist_matrix: n x n matrix where dist_matrix[i][j] is distance i->j
        parents: list of parent arrays, parents[i] is parent array for src i
    """
    n = len(adj)
    dist_matrix = [[math.inf] * n for _ in range(n)]
    parents = []

    for s in range(n):
        dist, parent = dijkstra(adj, s)
        dist_matrix[s] = dist
        parents.append(parent)

    return dist_matrix, parents
