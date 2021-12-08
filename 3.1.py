
with open("./inputs/3.txt") as f:
    counts = [0,0,0,0,0,0,0,0,0,0,0,0]
    for line in f:
        bits = map(lambda b: 1 if int(b) else -1, line.strip())
        counts = map(sum, zip(bits, counts))
    counts = list(counts)
    gamma = int(''.join(map(lambda n: str(0 if n<0 else 1), counts)), 2)
    epsilon = 0xFFF ^ gamma
    print(epsilon * gamma)