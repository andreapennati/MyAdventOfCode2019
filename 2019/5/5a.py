import sys

def first(bucket:list, x:int, y:int, z:int, c:int, b:int):
    bucket[z] = choose(x, c) + choose(y, b)

def second(bucket:list, x:int, y:int, z:int, c:int, b:int):
    bucket[z] = choose(x, c) * choose(y, b)

def third(bucket:list, x:int, c:int):
    bucket[x] = int(input())

def fourth(bucket:list, x:int, c:int):
    print(choose(x, c))

old_rules = {
    1: first,
    2: second
}

new_rules = {
    3: third,
    4: fourth
}

def parse(bucket:list, i:int):
    de = bucket[i] % 100
    c = bucket[i] // 100 % 10
    b = bucket[i] // 1000 % 10
    a = bucket[i] // 10000 % 10
    return de, c, b, a

def choose(i:int, select:int):
    if select:
        return i
    else:
        return bucket[i]

bucket = [int(i) for i in open(sys.argv[1], 'r').read().split(',')]
i = 0

while(i < len(bucket)):
    de, c, b, a = parse(bucket, i)

    if de in old_rules:
        x, y, z = bucket[i+1:i+4]
        old_rules[de](bucket,x,y,z,c,b)
        i += 4
    elif de in new_rules:
        x = bucket[i+1]
        new_rules[de](bucket,x,c)
        i += 2
    else:
        break

