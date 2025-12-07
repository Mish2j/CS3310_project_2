import math

def floyd_warshall(matrix):
    """
    Floyd-Warshall APSP with path reconstruction.
    Input:
        matrix: n x n adjacency matrix of edge weights (inf if no edge, 0 diag)
    Returns:
        dist: n x n matrix of shortest path distances
        next: n x n "next" matrix for path reconstruction
    """
    n = len(matrix)
    INF = math.inf

    # distance and next matrix
    dist = [[matrix[i][j] for j in range(n)] for i in range(n)]
    next = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != INF and i != j:
                next[i][j] = j

    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            if dik == INF:
                continue
            for j in range(n):
                new_dist = dik + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist
                    next[i][j] = next[i][k]

    return dist, next
