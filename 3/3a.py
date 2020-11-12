D = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

def get_path():
  p = (0,0)
  result = set()
  f = input().split(',')
  for cmd in f:
    for i in range(int(cmd[1:])):
      p = tuple(map(lambda x,y: x + y, p, D[cmd[0]]))
      result.add(p)
  return result

a = get_path()
b = get_path()
print(min(abs(x)+abs(y) for x, y in a.intersection(b)))