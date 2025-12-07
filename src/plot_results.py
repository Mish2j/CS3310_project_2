import csv
import os
import matplotlib.pyplot as plt


csv_path="data/results.csv"
out_dir="data"
def load_results():
    results = {
        "sparse": {"n": [], "dij": [], "fw": []},
        "dense": {"n": [], "dij": [], "fw": []},
    }

    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n = int(row["n"])
            gtype = row["type"]
            dij = float(row["avg_dijkstra_ms"])
            fw = float(row["avg_floyd_ms"])

            results[gtype]["n"].append(n)
            results[gtype]["dij"].append(dij)
            results[gtype]["fw"].append(fw)

    return results

def plot_result(n_values, dijkstra_times, fw_times, title, filename, out_dir):
    """Reusable helper that plots a single sparse/dense runtime chart."""
    plt.figure()
    plt.plot(n_values, dijkstra_times, marker="o", label="Dijkstra APSP")
    plt.plot(n_values, fw_times, marker="s", label="Floyd-Warshall")
    plt.xlabel("Number of vertices n")
    plt.ylabel("Average runtime (ms)")
    plt.title(title)
    plt.legend()
    plt.grid(True)

    # Save file
    path = os.path.join(out_dir, filename)
    plt.savefig(path, dpi=200)
    plt.show()
    

def plot_results():
    os.makedirs(out_dir, exist_ok=True)
    results = load_results()

    # Sparse
    plot_result(
        n_values=results["sparse"]["n"],
        dijkstra_times=results["sparse"]["dij"],
        fw_times=results["sparse"]["fw"],
        title="Sparse Graphs",
        filename="runtime_sparse.png",
        out_dir=out_dir
    )

    # Dense
    plot_result(
        n_values=results["dense"]["n"],
        dijkstra_times=results["dense"]["dij"],
        fw_times=results["dense"]["fw"],
        title="Dense Graphs",
        filename="runtime_dense.png",
        out_dir=out_dir
    )

    print("Plots saved in", out_dir)


if __name__ == "__main__":
    plot_results()
