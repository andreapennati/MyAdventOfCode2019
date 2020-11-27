D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def get_path():
  p = (0,0)
  result = set()
  steps = dict()
  f = input().split(',')
  s = 0
  for cmd in f:
    for i in range(int(cmd[1:])):
      p = tuple(map(lambda x,y: x + y, p, D[cmd[0]]))
      result.add(p)
      s += 1
      if not p in steps:
        steps[p] = s
  return result,steps

a, a_steps = get_path()
b, b_steps = get_path()
result = set()
for el in a.intersection(b):
  result.add(a_steps[el] + b_steps[el])

print(sorted(result)[0])