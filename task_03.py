import task_01 as t1
import networkx as nx

# Створення графа
G = t1.get_graf(is_weigted=True)

# Алгоритм Дейкстри
shortest_path = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))

# Виведення найкоротших шляхів
for start in G.nodes():
    for end in G.nodes():
        if start != end:
            print(f"Найкоротший шлях від {start} до {end}: {shortest_path[start][end]}")
