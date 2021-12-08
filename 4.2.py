import re

def is_win(board):
  crossed = lambda slice: not list(filter(bool, board[slice]))
  for i in range(5):
    if crossed(slice(i*5, i*5+5)) or crossed(slice(i, None, 5)):
      return True
  return False

def cross(boards, draw):
  for board in boards:
    for (i, n) in enumerate(board):
      if n == draw:
        board[i] = None

with open("./inputs/4.txt") as f:
  draws = map(int, f.readline().split(','))
  boards = []
  while f.readline():
    boards.append(
      [
        int(n) for line in (
            f.readline().strip()
              for i in range(5)
          ) if line
          for n in re.split(r'\s+', line)
      ]
    )

  while len(boards) > 1:
    cross(boards, next(draws))
    boards = [board for board in boards if not is_win(board)]

  [last] = boards
  
  while not is_win(last):
    draw = next(draws)
    cross(boards, draw)
    print('drawing', draw)

  print(draw * sum([n for n in last if n]))


  