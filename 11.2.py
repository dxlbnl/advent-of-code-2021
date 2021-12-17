with open("./inputs/11.txt") as f:
  displaygrid = lambda: print("\n".join([''.join([str(c) for c in grid[y*width:y*width+width]]) for y in range(height)]))

  width = 0
  height = 0
  grid = []

  for line in f:
    l = [int(c) for c in line.strip()]
    width = len(l)
    height += 1
    grid += l

  indices = list(range(width * height))
  
  def flash(i, flashed, stack=''):
    if i in flashed: return

    x = i%width
    y = i//width
    flashed.add(i)
    s1 = slice(max(0, x-1)+(y-1)*width,min(width, x+2)+(y-1)*width) if y > 0 else slice(0,0)
    s2 = slice(max(0, x-1)+y*width,min(width, x+2)+y*width)
    s3 = slice(max(0, x-1)+(y+1)*width,min(width, x+2)+(y+1)*width) if y < height else slice(0,0)

    # print('flash', i, (x,y), grid[i])
    # print('\t', stack)
    # print('\t', [(x%width,x//width) for x in indices[s1] + indices[s2] + indices[s3]])
    
    grid[s1] = [c+1 for c in grid[s1]]
    grid[s2] = [c+1 for c in grid[s2]]
    grid[s3] = [c+1 for c in grid[s3]]

    for i in indices[s1] + indices[s2] + indices[s3]:
      if grid[i] > 9 and i not in flashed:
        flash(i, flashed, '{}->{}'.format(stack, i))

  insync = lambda: len(set(grid)) == 1
  day = 0
  while not insync():
    day += 1
    grid = [c+1 for c in grid]
    flashed = set()
    for (i, c) in enumerate(grid):
      if c > 9:
        flash(i, flashed, '{}'.format(i))

    grid = [0 if c > 9 else c for c in grid]

    print('-'*10)
    print('day {}'.format(day+1))
    displaygrid()
  print('total days', day)


  