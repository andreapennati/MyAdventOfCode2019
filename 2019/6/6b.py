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

grandparents = []
for node in tree.all_nodes():
    if tree.is_ancestor(node.identifier, 'YOU') and tree.is_ancestor(node.identifier, 'SAN'):
        grandparents.append(node.identifier)

common = grandparents[-1:]
m = tree.depth(tree.get_node(common[0]))
you = tree.depth(tree.get_node('YOU'))
san = tree.depth(tree.get_node('SAN'))
print(you-m + san-m-2)
