import sys
f = [int(x) for x in open(sys.argv[1], 'r').read().split('\n')]

for a in f:
    for b in f:
        if a+b == 2020:
            print(a*b)
            exit(0)
