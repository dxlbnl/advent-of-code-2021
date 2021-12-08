size = 1000

grid = [0] * size * size

def get_slice(x1, y1, x2, y2):
  start = y1 * size + x1
  end = y2 * size + x2
  step = 1

  if x1 == x2:
    if y1 < y2:
      step = size
      end += 1
    else:
      step = -size
      end -= 1
  elif y1 == y2:
    if x1 < x2:
      end += 1
    else:
      step = -1
      end -= 1
  else:
    if x1 < x2 and y1 < y2:
      step = size + 1
      end += 1
    elif x1 < x2 and y1 > y2:
      step = -size + 1
      end -= 1
    elif x1 > x2 and y1 < y2:
      step = size - 1
      end += 1
    else:
      step = -size - 1
      end -= 1

  return slice(start, end, step)

with open("./inputs/5.txt") as f:
  for line in f.readlines():
    [x1, y1, x2, y2] = [
      int(n)
        for point in line.strip().split(' -> ')
        for n in point.split(',')
    ]

    s = get_slice(x1, y1, x2, y2)
    print((x1, y1), (x2, y2), s)
    grid[s] = [n + 1 for n in grid[s]]

  print(len([n for n in grid if n >= 2]))
  # print('\n'.join([
  #   ''.join([
  #     '{} '.format('.' if not n else n)
  #         for n in grid[l*size:l*size+size]
  #   ]) for l in range(size)
  # ]))