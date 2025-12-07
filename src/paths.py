def reconstruct_path_dijkstra(src, dest, parent):
    """
    Reconstruct shortest path src->dest given parent array from Dijkstra.
    Returns list of vertices [src, ..., dest]; or [] if no path.
    """
    path = []
    cur = dest
    while cur != -1 and cur != src:
        path.append(cur)
        cur = parent[cur]
    if cur == -1:
        # no path
        return []
    path.append(src)
    path.reverse()
    return path


def reconstruct_path_floyd(u, v, nxt):
    """
    Reconstruct shortest path u->v using Floyd-Warshall next matrix.
    Returns list of vertices [u, ..., v]; or [] if no path.
    """
    if nxt[u][v] is None:
        # no path
        return []  
    path = [u]
    while u != v:
        u = nxt[u][v]
        path.append(u)
    return path
