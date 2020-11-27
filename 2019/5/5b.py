import sys

def one(bucket:list, x:int, y:int, z:int, c:int, b:int):
    global i
    bucket[z] = choose(x, c) + choose(y, b)
    i += 4

def two(bucket:list, x:int, y:int, z:int, c:int, b:int):
    global i
    bucket[z] = choose(x, c) * choose(y, b)
    i += 4

def three(bucket:list, x:int):
    global i
    bucket[x] = int(input())
    i += 2

def four(x:int, c:int):
    global i
    print(choose(x, c))
    i += 2

def five(x:int, y:int, c:int, b:int):
    global i
    if choose(x, c) != 0:
        i = choose(y, b)
    else:
        i += 3

def six(x:int, y:int, c:int, b:int):
    global i
    if choose(x, c) == 0:
        i = choose(y, b)
    else:
        i += 3

def seven(bucket:list, x:int, y:int, z:int, c:int, b:int):
    global i
    if choose(x ,c) < choose(y ,b):
        bucket[z] = 1
    else:
        bucket[z] = 0
    i += 4

def eight(bucket:list, x:int, y:int, z:int, c:int, b:int):
    global i
    if choose(x ,c) == choose(y ,b):
        bucket[z] = 1
    else:
        bucket[z] = 0
    i += 4

operation = {
    1: one,
    2: two
}

position = {
    3: three,
    4: four
}

jump = {
    5: five,
    6: six
}

compare = {
    7: seven,
    8: eight
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
global i
i = 0

while(True):
    de, c, b, a = parse(bucket, i)

    if de in operation:
        x, y, z = bucket[i+1:i+4]
        operation[de](bucket, x, y, z, c, b)
    elif de in position:
        x = bucket[i+1]
        position[de](bucket, x) if de == 3 else position[de](x, c)
    elif de in jump:
        x,y = bucket[i+1:i+3]
        jump[de](x, y, c, b)
    elif de in compare:
        x, y, z = bucket[i+1:i+4]
        compare[de](bucket, x, y, z, c, b)
    else:
        break



