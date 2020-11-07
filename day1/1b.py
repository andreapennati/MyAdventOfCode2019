import sys

f =  open(sys.argv[1], "r")
result = 0
for i in f:
    flag = int(int(i) / 3) - 2
    while(flag > 0):
        result += flag
        flag = int(flag / 3) - 2
        
print(result)