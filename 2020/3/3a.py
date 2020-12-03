import sys

path = [line.strip() for line in open(sys.argv[1], 'r')]

def run(right, down):
    result, index = 0, right
    for p in path[down::down]:
        if p[index] == '#':
            result += 1
        index = (index+right) % len(p)
    return int(result)

print(run(3,1))

