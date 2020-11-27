import sys
from treelib import Tree

def add_orbits(tree:Tree, key:str, d:dict):
    for child in d[key]:
        tree.create_node(identifier=child, parent=key)
        if child in d:
            add_orbits(tree, child, d)

file = open(sys.argv[1],'r')
line = file.readline()
d = dict()

while(line):
    m = line.split(')')
    key = m[0]
    value = m[1].strip('\n')
    if key not in d.keys():
        d.setdefault(key, [])
        d[key].append(value)
    else:
        d[key].append(value)
    line = file.readline()

tree = Tree()
tree.create_node(identifier='COM')
add_orbits(tree, 'COM', d)

result = 0
for node in tree.all_nodes():
    result += tree.depth(node)
print(result)



