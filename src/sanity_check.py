from src.dijkstra_apsp import all_pairs_shortest_paths_dijkstra
from src.floyd_warshall import floyd_warshall
from src.graph_utils import adjacency_list_to_matrix
from src.paths import reconstruct_path_dijkstra, reconstruct_path_floyd

def run_sanity_check():
    # Build a small 4-node directed graph
    # 0 -> 1 (1), 0 -> 2 (4)
    # 1 -> 2 (2), 1 -> 3 (6)
    # 2 -> 3 (3)
    # 3 -> 0 (7)
    adj = [
        [(1, 1), (2, 4)],
        [(2, 2), (3, 6)],
        [(3, 3)],
        [(0, 7)]
    ]

    # APSP by repeated Dijkstra
    dist_dij, parents = all_pairs_shortest_paths_dijkstra(adj)

    # APSP by Floyd–Warshall
    mat = adjacency_list_to_matrix(adj)
    dist_fw, nxt = floyd_warshall(mat)

    print("Distance matrix from repeated Dijkstra:")
    for row in dist_dij:
        print(row)

    print("\nDistance matrix from Floyd-Warshall:")
    for row in dist_fw:
        print(row)

    # Compare
    n = len(adj)
    isValid = True
    for i in range(n):
        for j in range(n):
            if abs(dist_dij[i][j] - dist_fw[i][j]) > 1e-9:
                isValid = False
                print(f"Mismatch at ({i},{j}): "
                      f"Dijkstra={dist_dij[i][j]}, FW={dist_fw[i][j]}")
    print("\nSanity check passed?", isValid)

    # path reconstruction
    src, dst = 0, 3
    print(f"\nExample shortest path from {src} to {dst}:")

    path_from_dijkstra = reconstruct_path_dijkstra(src, dst, parents[src])
    print("  Dijkstra path:", path_from_dijkstra, "dist:", dist_dij[src][dst])

    path_from_fw = reconstruct_path_floyd(src, dst, nxt)
    print("  Floyd-Warshall path:", path_from_fw, "dist:", dist_fw[src][dst])


if __name__ == "__main__":
    run_sanity_check()
