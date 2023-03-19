import json
import networkx as nx

with open("data.json", 'r') as f:
    graph = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)

def get_stable_set(G, i):
    max_stable_set = {i}
    for node in G.nodes():
        if node not in max_stable_set and all(neigh not in max_stable_set for neigh in G.neighbors(node)):
            max_stable_set.add(node)
    return max_stable_set

G = nx.Graph()
for i in graph.keys():
    for j in graph[i]:
        G.add_edges_from([(i, j)])      

best = get_stable_set(G, 3)
graph.pop('3')
for i in graph:
    cur = get_stable_set(G, i)
    if len(cur) > len(best):
        best = cur

print(len(best))
print([id_to_country[i] for i in best])
