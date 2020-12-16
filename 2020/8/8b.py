import sys
from copy import deepcopy

def increment(a):
    globals()['accumulator'] += int(a)
    globals()['fresh_copy'][globals()['index']][0] = 'stop'
    globals()['index'] += 1

def jump(a):
    globals()['fresh_copy'][globals()['index']][0] = 'stop'
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

for n in range(len(codec)):
    
    fresh_copy = deepcopy(codec)

    if fresh_copy[n][0] == 'nop':
        fresh_copy[n][0] = 'jmp'
    if fresh_copy[n][0] == 'jmp':
        fresh_copy[n][0] = 'nop'
        
    accumulator, index = 0,0
    while(True):
        if fresh_copy[index][0] == 'stop':
            break
        if index == len(fresh_copy)-1:
            print(accumulator)
            exit(0)
        operation[fresh_copy[index][0]](fresh_copy[index][1])
        