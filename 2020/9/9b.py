import sys
from itertools import combinations

with open(sys.argv[1], 'r') as f:
    numbers = [int(i) for i in f.read().splitlines()]

def decrypt(A, S):
    length = 0
    ending_index = -1
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum == S:
                if length < j - i + 1:
                    length = j - i + 1
                    ending_index = j 
    return A[ending_index - length + 1 : ending_index]
    
result = sorted(decrypt(numbers, 18272118))
print(result[0] + result[-1])
    
    