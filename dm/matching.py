import json
import networkx as nx

with open("data.json", 'r') as f:
    graph = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)

def find_max_matching(G):
    matching = nx.algorithms.matching.max_weight_matching(G)
    return matching


G = nx.Graph()
for i in graph.keys():
    for j in graph[i]:
        G.add_edges_from([(i, j)])      

best = find_max_matching(G)

print(len(best))
for i in best:
    print(id_to_country[i[0]], '-', id_to_country[i[1]])
