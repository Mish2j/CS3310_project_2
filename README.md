# **APSP Algorithms**

This project implements and compares two all-pairs shortest-path algorithms:

* **Repeated Dijkstra’s Algorithm**
* **Floyd–Warshall Algorithm**

## **How to Run**

### **1. Run the sanity check + benchmarks**

From the project root:

```
python main.py
```

This will:

* Verify correctness on a small example
* Generate random graphs of various sizes
* Benchmark both algorithms
* Save results to `data/results.csv`

### **2. Generate the runtime plots**

After benchmarking:

```
python -m src.plot_results
```

Plots will be saved in:

```
data/runtime_sparse.png
data/runtime_dense.png
```
