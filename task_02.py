import task_01 as t1
import networkx as nx
from collections import deque

# DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


G = t1.get_graf()
graph = nx.to_dict_of_lists(G)

# Пошук шляхів за допомогою DFS та BFS
start_node = 'Залізничний вокзал'
goal_node = 'Таїрово'

print("Шляхи за допомогою DFS:")
dfs_paths = list(dfs(graph, start_node, goal_node))
for path in dfs_paths:
    print(path)

print("Шляхи за допомогою BFS:")
bfs_paths = list(bfs(graph, start_node, goal_node))
for path in bfs_paths:
    print(path)
