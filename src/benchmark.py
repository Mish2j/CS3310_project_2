import os
import time

from src.graph_utils import generate_random_strongly_connected_digraph, adjacency_list_to_matrix
from src.dijkstra_apsp import all_pairs_shortest_paths_dijkstra
from src.floyd_warshall import floyd_warshall


def benchmark_algorithms(
    n_values,
    edge_prob_sparse=0.05,
    edge_prob_dense=0.5,
    runs_per_n=5,
    min_w=1,
    max_w=10,
    output_path="../data/results.csv"
):
    """
    For each n in n_values:
      - generate 'runs_per_n' random sparse and dense graphs
      - run APSP via repeated Dijkstra and Floyd-Warshall
      - record average runtime in milliseconds

    Write a CSV file with columns:
        n,type,avg_dijkstra_ms,avg_floyd_ms
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        f.write("n,type,avg_dijkstra_ms,avg_floyd_ms\n")

        for n in n_values:
            for graph_type, p in [("sparse", edge_prob_sparse),
                                  ("dense", edge_prob_dense)]:
                total_time_dij = 0.0
                total_time_fw = 0.0

                for _ in range(runs_per_n):
                    adj = generate_random_strongly_connected_digraph(
                        n, edge_prob=p, min_w=min_w, max_w=max_w)
                    mat = adjacency_list_to_matrix(adj)

                    t0 = time.perf_counter()
                    _dist_dij, _parents = all_pairs_shortest_paths_dijkstra(adj)
                    t1 = time.perf_counter()

                    t2 = time.perf_counter()
                    _dist_fw, _nxt = floyd_warshall(mat)
                    t3 = time.perf_counter()
                
                    total_time_dij += (t1 - t0)
                    total_time_fw += (t3 - t2)

                avg_dij_ms = (total_time_dij / runs_per_n) * 1000.0
                avg_fw_ms = (total_time_fw / runs_per_n) * 1000.0

                line = f"{n},{graph_type},{avg_dij_ms:.4f},{avg_fw_ms:.4f}\n"
                f.write(line)
                print(line, end="")


# if __name__ == "__main__":
#     n_values = list(range(10, 210, 10))
#     benchmark_algorithms(
#         n_values=n_values,
#         edge_prob_sparse=0.05,
#         edge_prob_dense=0.5,
#         runs_per_n=3,
#         output_path="../data/results.csv"
#     )
