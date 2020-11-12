import sys

def add_bucket(bucket:list ,x:int ,y:int ,z:int):
    bucket[z] = bucket[x] + bucket[y]

def mul_bucket(bucket:list ,x:int ,y:int ,z:int):
    bucket[z] = bucket[x] * bucket[y]

dispatcher = {
    1: add_bucket,
    2: mul_bucket
}

bucket = [int(i) for i in open(sys.argv[1], 'r').read().split(',')]
bucket[1] = 12
bucket[2] = 2
for i in range(0, len(bucket), 4):
    op, x, y, z = bucket[i:i+4]
    if op in dispatcher:
        dispatcher[op](bucket,x,y,z)
    else:
        break
print(bucket)