"""
SLE-2 / SLE-3: BFS vs DFS graph search system
Course: 02AML204 – Introduction to Artificial Intelligence
"""

from collections import deque
from time import perf_counter

GRAPH = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"],
    "D": ["H", "I"], "E": ["J", "K"], "F": ["L", "M"],
    "G": ["N", "O"], "H": ["P"], "I": ["Q"], "J": ["R"],
    "K": ["S"], "L": ["T"], "M": [], "N": [], "O": [],
    "P": [], "Q": [], "R": [], "S": [], "T": []
}

START, GOAL, RUNS = "A", "T", 10000


def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    expanded = 0

    while queue:
        node, path = queue.popleft()
        expanded += 1
        if node == goal:
            return path, expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, path + [neighbour]))

    return None, expanded


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    expanded = 0

    while stack:
        node, path = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        expanded += 1
        if node == goal:
            return path, expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, expanded


def benchmark(search_function, name):
    start_time = perf_counter()
    path = None
    expanded = 0

    for _ in range(RUNS):
        path, expanded = search_function(GRAPH, START, GOAL)

    elapsed_ms = (perf_counter() - start_time) * 1000
    average_ms = elapsed_ms / RUNS

    print(name)
    print(f"Path: {' -> '.join(path) if path else 'Not found'}")
    print(f"Nodes expanded: {expanded}")
    print(f"Total time for {RUNS:,} runs: {elapsed_ms:.3f} ms")
    print(f"Average time per run: {average_ms:.6f} ms")
    print("-" * 45)

    return elapsed_ms, average_ms, expanded


if __name__ == "__main__":
    print("SLE-2 / SLE-3: BFS vs DFS Graph Search")
    print(f"Graph: {len(GRAPH)} nodes | Start: {START} | Goal: {GOAL}")
    print(f"Benchmark runs: {RUNS:,}")
    print("=" * 45)

    bfs_total, bfs_avg, bfs_nodes = benchmark(bfs, "BFS")
    dfs_total, dfs_avg, dfs_nodes = benchmark(dfs, "DFS")

    print("\nComparison")
    print(f"BFS average: {bfs_avg:.6f} ms/run")
    print(f"DFS average: {dfs_avg:.6f} ms/run")
    print(f"BFS nodes expanded: {bfs_nodes}")
    print(f"DFS nodes expanded: {dfs_nodes}")
