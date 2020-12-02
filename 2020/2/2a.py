import sys

def isValid(_min, _max, char, password):
    count = 0
    for i in range(0, len(password)):
        if password[i] == char:
            count += 1
    return count >= _min and count <= _max

f = open(sys.argv[1], 'r')

valid_password = f.readline().strip('\n').split(' ')

result = 0
while(len(valid_password) == 3):
    if isValid(int(valid_password[0].partition('-')[0]), int(valid_password[0].partition('-')[2]), valid_password[1][0], valid_password[2]):
        result += 1
    valid_password = f.readline().strip('\n').split(' ')
print(result)