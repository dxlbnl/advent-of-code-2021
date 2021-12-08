
with open("./inputs/8.txt") as f:
  simple_count = 0
  for line in f:
    [signal, output] = [
      part.strip().split(' ') for part in line.split('|')
    ]
    simple_count += len([value for value in output if len(value) == 2 or len(value) == 4 or len(value) == 3 or len(value) == 7])
    print(output, simple_count)
    


  