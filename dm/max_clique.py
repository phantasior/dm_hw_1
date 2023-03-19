import json

def bron_kerbosch(R, P, X, graph, max_clique):
    if not P and not X:
        if len(R) > len(max_clique):
            max_clique.clear()
            max_clique.extend(R)
        return

    for v in P.copy():
        bron_kerbosch(R + [v], [n for n in P if n in graph[v]], [n for n in X if n in graph[v]], graph, max_clique)
        P.remove(v)
        X.append(v)

def find_max_clique(graph):
    max_clique = []
    bron_kerbosch([], list(graph.keys()), [], graph, max_clique)
    return max_clique



with open("data.json", 'r') as f:
    graph = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)

clique = [id_to_country[i] for i in find_max_clique(graph)]
print(clique) # ['Russia', 'Latvia', 'Litva', 'Belarus']