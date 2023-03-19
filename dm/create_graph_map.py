import json

dic = {}

with open("map.csv") as f:
	for line in f:
		cur = line.split(',')

		dic[int(cur[0])] = cur[1].replace('\n', '')

with open("map.json", 'w') as f:
	json.dump(dic, f)