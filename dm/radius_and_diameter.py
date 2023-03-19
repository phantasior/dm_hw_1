import json
from collections import deque

def bfs(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    queue = deque([start])
    while queue:
        current_vertex = queue.popleft()

        for neighbor in graph[current_vertex]:
            if distances[neighbor] == float('infinity'):
                distances[neighbor] = distances[current_vertex] + 1
                queue.append(neighbor)

    return distances

def get_graph_radius(graph):
    min_diameter = float('infinity')

    for vertex in graph:
        distances = bfs(graph, vertex)
        max_distance = max(distances.values())
        if max_distance < min_diameter:
            min_diameter = max_distance

    return min_diameter

def get_radius(graph, radius):
    nodes = []

    for vertex in graph:
        distances = bfs(graph, vertex)
        max_distance = max(distances.values())
        if max_distance == radius:
            nodes.append(vertex)

    return nodes

with open("data.json", 'r') as f:
    graph = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)



radius = get_graph_radius(graph)
nodes = get_radius(graph, radius)

print("Radius:", radius)
for i in nodes:
    print(id_to_country[i], end = ', ')

print()
print()

def get_graph_diameter(graph):
    min_diameter = float('-infinity')

    for vertex in graph:
        distances = bfs(graph, vertex)
        max_distance = max(distances.values())
        if max_distance >= min_diameter:
            min_diameter = max_distance

    return min_diameter

def get_diameter(graph, diameter):
    nodes = []

    for vertex in graph:
        distances = bfs(graph, vertex)
        max_distance = max(distances.values())
        if max_distance == diameter:
            nodes.append(vertex)

    return nodes


diameter = get_graph_diameter(graph)
nodes = get_diameter(graph, diameter)

print("Diameter:", diameter)
for i in nodes:
    print(id_to_country[i], end = ', ')

print()
print()