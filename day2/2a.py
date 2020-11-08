import sys

bucket = [int(i) for i in open(sys.argv[1], 'r').read().split(',')]
bucket[1] = 12
bucket[2] = 2
for i in range(0, len(bucket), 4):
    op, x, y, z = bucket[i:i+4]
    if op == 1:
        bucket[z] = bucket[x] + bucket[y]
    elif op == 2:
        bucket[z] = bucket[x] * bucket[y]
    else: break
print(bucket)