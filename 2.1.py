
with open("./inputs/2.txt") as f:
    depth = 0
    position = 0
    for line in f:
        [cmd, amount] = line.strip().split(' ')
        if cmd == 'forward':
            position += int(amount)
        elif cmd == 'down':
            depth += int(amount)
        elif cmd == 'up':
            depth -= int(amount)

    print(position * depth)