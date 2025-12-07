from src.sanity_check import run_sanity_check
from src.benchmark import benchmark_algorithms

def main():
    print("=== Sanity check ===")
    run_sanity_check()

    print("\n=== Benchmarking ===")
    n_values = list(range(10, 210, 10))
    benchmark_algorithms(
        n_values=n_values,
        edge_prob_sparse=0.05,
        edge_prob_dense=0.5,
        runs_per_n=3,
        output_path="data/results.csv"
    )

    print("\nBenchmark complete. Results in data/results.csv")

if __name__ == "__main__":
    main()
