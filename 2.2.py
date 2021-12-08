
with open("./inputs/2.txt") as f:
    aim = 0
    depth = 0
    position = 0
    for line in f:
        [cmd, amount] = line.strip().split(' ')
        amount = int(amount)
        if cmd == 'forward':
            position += amount
            depth += aim * amount
        elif cmd == 'down':
            aim += amount
        elif cmd == 'up':
            aim -= amount

    print(position * depth)