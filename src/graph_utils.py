import random
import math

def generate_random_strongly_connected_digraph(
    n,
    edge_prob=0.2,
    min_w=1,
    max_w=10,
    seed=None
):
    """
    Generate a random strongly connected directed graph with:
      - n vertices labeled 0..n-1
      - edge probability edge_prob for each ordered pair (u,v), u != v
      - weights in [min_w, max_w]
    Returns adjacency list: adj[u] = list of (v, weight)
    """
    if seed is not None:
        random.seed(seed)

    adj = [[] for _ in range(n)]

    def add_edge(u, v, w):
        adj[u].append((v, w))

    # Ensure strong connectivity with a random cycle
    perm = list(range(n))
    random.shuffle(perm)
    for i in range(n):
        u = perm[i]
        v = perm[(i + 1) % n]
        w = random.randint(min_w, max_w)
        add_edge(u, v, w)

    # Add additional random edges
    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if random.random() < edge_prob:
                w = random.randint(min_w, max_w)
                add_edge(u, v, w)

    return adj


def adjacency_list_to_matrix(adj):
    """
    Convert adjacency list to adjacency matrix of edge weights.
    dist[i][j] = weight of edge i->j, or +inf if no edge (0 on diagonal).
    """
    n = len(adj)
    INF = math.inf
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j, w in adj[i]:
            if w < dist[i][j]:
                dist[i][j] = w
    return dist
