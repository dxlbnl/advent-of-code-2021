import re

with open("./inputs/13.txt") as f:
  dots = set()
  
  for line in f:
    line = line.strip()
    if line:
      [x, y] = [int(x) for x in line.split(',')]
      dots.add((x,y))
    else:
      break
  
  width = max({ dot[0] for dot in dots }) + 1
  height = max({ dot[1] for dot in dots }) + 1

  grid = [[False for i in range(width)] for i in range(height)]

  for (x, y) in dots:
    grid[y][x] = True
  
  display = lambda grid: print("~\n{}\n~".format('\n'.join([''.join(['#' if dot else '.' for dot in line]) for line in grid])))
  # display(grid)
  print('size', width, height)

  for line in f:
    (label, position) = re.search(r'(\w+)=(\d+)', line).groups()
    if label == 'y':
      y = int(position)
      print('Y flipped', y)

      # Copy bottom part into grid
      for (i, line) in enumerate(grid[y+1:]):
        j = y-i-1

        if j<0: break

        grid[i+y+1] = grid[j] = [top or bottom for (top, bottom) in zip(grid[j], line)]

      # Crop grid
      grid = grid[:max(y, height-y-1)]
      height = len(grid)


    if label == 'x':
      x = int(position)
      print('X flipped', x, )
      
      if x < width - x:
        # Copy left into right
        fill = [False]*(width - 2*x - 1)
        for line in grid:
          line[::] = [left or right for (left, right) in zip(fill + line[:x], line[x+1::][::-1])]

      else:
        # Copy right into left
        fill = [False]*(x - (width - x) + 1)
        for line in grid:
          line[::] = [left or right for (left, right) in zip(line[:x], fill + line[x+1::][::-1])]
      width = len(grid[0])

      
    
    # display(grid)
  display(grid)
  print(sum([len([dot for dot in line if dot]) for line in grid]))


  