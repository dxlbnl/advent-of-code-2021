import re

def get_win(boards):
  for board in boards:
    crossed = lambda slice: not list(filter(bool, board[slice]))
    for i in range(5):
      if crossed(slice(i*5, i*5+5)) or crossed(slice(i, None, 5)):
        return board

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
  for b in boards:
    print(b)
  while not get_win(boards):
    draw = next(draws)
    print('drawing', draw)
    cross(boards, draw)

  winner = get_win(boards)
  print('winner', draw * sum(filter(bool, winner)))


    
  # checkwin(boards)
  # print(next(draws), boards)

  