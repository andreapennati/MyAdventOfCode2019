import sys

def isValid(p1, p2, char, password):
    if password[p1-1] == char and password[p2-1] == char:
        return False
    return password[p1-1] == char or password[p2-1] == char

f = open(sys.argv[1], 'r')

valid_password = f.readline().strip('\n').split(' ')

result = 0
while(len(valid_password) == 3):
    if isValid(int(valid_password[0].partition('-')[0]), int(valid_password[0].partition('-')[2]), valid_password[1][0], valid_password[2]):
        result += 1
    valid_password = f.readline().strip('\n').split(' ')
print(result)