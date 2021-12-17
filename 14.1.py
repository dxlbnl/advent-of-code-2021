
from os import remove


with open("./inputs/14.txt") as f:
  polymer = f.readline().strip()
  insertion_ops = {}

  print(polymer)
  for line in f:
    if line.strip():
      [search, insert] = line.strip().split(' -> ')
      insertion_ops[search] = insert

  for step in range(10):
    insertions = []
    for search in insertion_ops:
      if search in polymer:
        index = 0
        while True:
          index = polymer.find(search, index) + 1
          if not index: break

          insertions.append((index, insertion_ops[search]))
    insertions.sort()

    removed = 0
    new_polymer = ''
    for (index, insert) in insertions:
      new_polymer += polymer[:index - removed] + insert
      polymer = polymer[index - removed:]
      removed = index
      
    polymer = new_polymer + polymer

  
  frequencies = sorted([(polymer.count(e), e) for e in {e for e in polymer} ])
  print(frequencies)

  print(frequencies[-1][0] - frequencies[0][0])


  