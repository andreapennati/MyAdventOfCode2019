import sys

f =  open(sys.argv[1], "r")
result = 0
for i in f:
    result += int(int(i) / 3) - 2

print(result)