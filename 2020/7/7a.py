import sys
from collections import defaultdict

graph = defaultdict(list)

def addEdge(graph,u,v):
    for i in v:    
        graph[u].append(i)
    
def find_all_path(start):
    if start == "shiny gold":
        return True
    elif start == "no other":
        return False
    else:
        return any(find_all_path(child) for amount, child in graph[start])

with open(sys.argv[1], 'r') as f:    
    for line in [line.strip('\n').split('bags contain') for line in f.readlines()]:
        line = [line[0].strip(' ')] + [(t[0],t[2:]) for t in [l.replace('bags','').replace('bag','').replace('.','').strip(' ') for l in line[1].split(',')]]
        if not line[1][0].isdigit():
            line[1] = ('0', 'no other')
        addEdge(graph, line[0], line[1:])

print(sum(find_all_path(color) for color in graph)-1)