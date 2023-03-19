import json

with open("data.json", 'r') as f:
    graph_dict = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)

def get_dist(a, b):
    return geopy.distance.geodesic(a, b).km

def prufer_code(tree):
    degree = [0] * (len(tree) + 1)
    for edge in tree:
        degree[edge[0]] += 1
        degree[edge[1]] += 1
    
    leaf = min(i for i in range(1, len(degree)) if degree[i] == 1)
    
    code = []
    for i in range(len(degree) - 2):
        # Find the neighbor of the smallest leaf node with the smallest label
        neighbor = min(v for v in tree if leaf in v and degree[v[0]] == 1 and degree[v[1]] == 1)
        # Add the label of the neighbor to the code
        code.append(neighbor[0] if neighbor[1] == leaf else neighbor[1])
        # Decrement the degree of the two vertices connected by the neighbor
        degree[neighbor[0]] -= 1
        degree[neighbor[1]] -= 1
        # Remove the smallest leaf node from the tree
        degree[leaf] = 0
        if degree[neighbor[0]] == 0:
            leaf = neighbor[0]
        else:
            leaf = neighbor[1]
    
    return code
