import json
from igraph import *
graph = Graph()

with open("data.json", 'r') as f:
    graph_dict = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)

for i in graph_dict.keys():
    graph.add_vertex(i)

for i in graph_dict.keys():
    for j in graph_dict[i]:
        graph.add_edge(i, j)

def minimum_vertex_cover():
    cover = []
    stable_set = graph.largest_independent_vertex_sets()[0]
    for vertex in graph.vs:
        if vertex.index in stable_set: continue
        cover.append(graph.vs[vertex.index]["name"])

    return cover


cover = minimum_vertex_cover()
print(len(cover)) # 24
print([id_to_country[i] for i in cover])
# ['Russia', 'Norway', 'Finland', 'Latvia', 'Belarus', 'Poland', 'Slovakia', 
# 'Germany', 'Belgium', 'Austria', 'Hungary', 'Romania', 'Moldova', 'Serbia', 'Switzerland',
# 'North Macedonia', 'Greece', 'Turkey', 'France', 'Italy', 'Croatia', 'Montenegro', 'Spain', 'Kosovo']
