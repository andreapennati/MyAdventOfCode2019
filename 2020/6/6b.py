import sys
from collections import defaultdict

answers = defaultdict(list)

with open(sys.argv[1], 'r') as f:
    for index, line in enumerate(f.read().split('\n\n')):
        for l in line.split('\n'):
            answers[index].append(list(l))

print(sum([len(set(value[0]).intersection(*value)) for value in answers.values()]))

