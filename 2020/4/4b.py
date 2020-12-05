import sys, re
from functools import reduce

def birth_year(year):
    return len(year) == 4 and 1920 <= int(year) <= 2002

def issue_year(year):
    return len(year) == 4 and 2010 <= int(year) <= 2020

def exp_year(year):
    return len(year) == 4 and 2020 <= int(year) <= 2030

def height(height):
    return ('in' in height and 59 <= int(height[:-2]) <= 79) or ('cm' in height and 150 <= int(height[:-2]) <= 193)

def hair_color(hair):
    return bool(re.search('#([a-f]|[0-9])([a-f]|[0-9])([a-f]|[0-9])([a-f]|[0-9])([a-f]|[0-9])([a-f]|[0-9])', hair))

def eye_color(eye):
    return eye in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def passport(id):
    return sum(n.isdigit() for n in id) == 9

def country_id(id):
    return True


validator = {
    'byr': birth_year,
    'iyr': issue_year,
    'eyr': exp_year,
    'hgt': height,
    'hcl': hair_color,
    'ecl': eye_color,
    'pid': passport,
    'cid': country_id

}


result = 0
for line in open(sys.argv[1], 'r').read().split('\n\n'):
    line = reduce(lambda x,y: x+y,[l.split('\n') for l in line.split(' ')])
    for att in line:
        flag = int(validator[att[:3]](att[4:]))

        if not flag:
            break

    if flag and (len(line) > 7 or (len(line) == 7) and not any('cid' in el for el in line)):
        result += 1
print(result)
