import sys
from functools import reduce

result = 0
for line in open(sys.argv[1], 'r').read().split('\n\n'):
    line = reduce(lambda x,y: x+y,[l.split('\n') for l in line.split(' ')])
    if len(line) > 7 or (len(line) == 7 and not any('cid' in el for el in line)):
        result += 1
print(result)
