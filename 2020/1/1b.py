import sys
f = [int(x) for x in open(sys.argv[1], 'r').read().split('\n')]

for a in f:
    for b in f:
        for c in f:
            if a+b+c == 2020:
                print(a*b*c)
                exit(0)