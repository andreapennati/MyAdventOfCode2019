import sys
from itertools import combinations

with open(sys.argv[1], 'r') as f:
    numbers = [int(i) for i in f.read().splitlines()]

start = 0
end = 25
check = numbers[:end]
for num in numbers[end:]:
    
    if not any([sum(n) == num for n in combinations(check, 2)]):
        print(num)
        exit()
            
    start += 1
    end += 1
    check = numbers[start:end]
    
    