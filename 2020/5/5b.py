import sys
from math import floor, ceil

def getRow(rules, start, end):
    if end - start == 1 and (rules[0] == 'F' or rules[0] == 'L'):
        return start
    elif end - start == 1 and (rules[0] == 'B' or rules[0] == 'R'):
        return end

    if rules[0] == 'F' or rules[0] == 'L':
        return getRow(rules[1:], start, floor((start + end) / 2))
    else:
        return getRow(rules[1:], ceil((start + end) / 2), end)

result = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        cmd = line.strip('\n')
        result.append(getRow(cmd[:7], 0, 127) * 8 + getRow(cmd[-3:], 0, 7))

result = sorted(result)
for i in range(0, len(result)):
    if result[i+1] - result[i] != 1:
        print(result[i] + 1)
        break

