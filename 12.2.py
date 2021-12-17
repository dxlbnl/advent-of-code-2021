import string
from collections import defaultdict

connections = defaultdict(list)

def step(position, path, visited_twice = False):
  if position == 'end':
    return [path]

  paths = []
  for point in connections[position]:
    visits = len([p for p in path if p == point])

    if point.islower() and (visited_twice and visits == 1 or visits == 2):
      continue

    paths += step(point, path + (point, ), visited_twice or (point.islower() and visits == 1))

  return paths

with open("./inputs/12.txt") as f:
  for line in f:
    [a, b] = line.strip().split('-')

    if b != 'start' and a != 'end':
      connections[a].append(b)
    if a != 'start' and b != 'end':
      connections[b].append(a)
  print(connections)
  
  paths = { str(','.join(l)) for l in step('start', ('start', )) }
  print('\n'.join(sorted(paths)))
  print(len(paths))


  