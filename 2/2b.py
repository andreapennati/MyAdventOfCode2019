import sys

bucket = [int(i) for i in open(sys.argv[1], 'r').read().split(',')]

def add_bucket(bucket:list ,x:int ,y:int ,z:int):
    bucket[z] = bucket[x] + bucket[y]

def mul_bucket(bucket:list ,x:int ,y:int ,z:int):
    bucket[z] = bucket[x] * bucket[y]

dispatcher = {
    1: add_bucket,
    2: mul_bucket
}

def calculate(bucket, s, t):
    bucket[1] = s
    bucket[2] = t
    i = 0
    for i in range(0, len(bucket), 4):
        op, x, y, z = bucket[i:i+4]
        if op in dispatcher:
            dispatcher[op](bucket,x,y,z)
        else: break
    return bucket[0]

for s in range(100):
    for t in range(0,100):
        if calculate(bucket[:], s, t) == 19690720:
            print(100*s+t)