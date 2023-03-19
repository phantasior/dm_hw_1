import json

graph = {}

with open("europe.csv") as f:
	for line in f:
		cur = line.split(',')[:2]

		if cur[0] not in graph:
			graph[cur[0]] = []

		if cur[1] not in graph:
			graph[cur[1]] = []

		graph[cur[0]].append(cur[1])
		graph[cur[1]].append(cur[0])

with open("data.json", 'w') as f:
	json.dump(graph, f)