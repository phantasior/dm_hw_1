import json
from countryinfo import CountryInfo
import geopy.distance

with open("data.json", 'r') as f:
    graph_dict = json.load(f)    

with open("map.json", 'r') as f:
    id_to_country = json.load(f)

def get_dist(a, b):
	return geopy.distance.geodesic(a, b).km

graph = []

for i in graph_dict:
	for j in graph_dict[i]:
		country1 = CountryInfo(id_to_country[i])
		country2 = CountryInfo(id_to_country[j])
		graph.append([int(i), int(j), get_dist(country1.capital_latlng(), country2.capital_latlng())])

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
 
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(graph):
    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
 
    parent = []
    rank = []
 
    for node in range(len(graph)):
        parent.append(node)
        rank.append(0)

    while i < len(graph) - 1 and e < len(graph)-1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
 
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
 
    return result


mst = kruskal_mst(graph)
for i in mst:
	a, b, w = i
	print(id_to_country[str(a)], id_to_country[str(b)])


# Slovakia Austria
# Slovenia Croatia
# republic of macedonia Albania
# Liechtenstein Switzerland
# Slovakia Hungary
# Belgium Luxembourg
# Lithuania Belarus
# Netherlands Belgium
# Serbia Bosnia and Herzegovina
# Italy San Marino
# czech republic Austria
# Latvia Lithuania
# Belgium France
# Austria Slovenia
# Estonia Latvia
# czech republic Germany
# Croatia Bosnia and Herzegovina
# Serbia republic of macedonia
# Germany Denmark
# Romania Moldova
# Lithuania Poland
# Finland Sweden
# Ukraine Moldova
# Norway Sweden
# Belarus Ukraine
# Switzerland France
# Romania Serbia
# republic of macedonia Greece
# Italy Slovenia
# Spain Portugal
# Austria Liechtenstein
# Russia Belarus
# France Monaco
# Greece Turkey
# Russia Finland
# France Spain
# Bulgaria Turkey