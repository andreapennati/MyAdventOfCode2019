import sys

def increment(a):
    globals()['accumulator'] += int(a)
    globals()['codec'][globals()['index']][0] = 'stop'
    globals()['index'] += 1

def jump(a):
    globals()['codec'][globals()['index']][0] = 'stop'
    globals()['index'] += int(a)

def nop(a):
    globals()['index'] += 1

operation = {
    'acc': increment,
    'jmp': jump,
    'nop': nop
}

with open(sys.argv[1], 'r') as f:
    codec = list(map(lambda x: x.split(' '), f.read().split('\n')))

accumulator, index = 0,0
while(True):
    if codec[index][0] == 'stop':
        break
    operation[codec[index][0]](codec[index][1])
print(accumulator)
        