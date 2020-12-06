import sys
from functools import reduce
from collections import defaultdict

answers = defaultdict(list)

with open(sys.argv[1], 'r') as f:
    for index, line in enumerate(f.read().split('\n\n')):
        line = reduce(lambda x,y: x+y, line.split('\n'))
        for l in line:
            if l not in answers[index]:
                answers[index].append(l)

print(sum([len(value) for value in answers.values()]))

