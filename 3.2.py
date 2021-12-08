
def count(numbers):
    counts = [0,0,0,0,0,0,0,0,0,0,0,0]
    for number in numbers:
        bits = map(lambda b: 1 if int(b) else -1, number)
        counts = map(sum, zip(bits, counts))
    return list(counts)


with open("./inputs/3.txt") as f:
    numbers = [line.strip() for line in f]

    oxygen_search = list(numbers)
    bit = 0
    while len(oxygen_search) != 1:
        common = count(oxygen_search)[bit] >= 0
        oxygen_search = list(filter(lambda n: bool(int(n[bit])) == common, oxygen_search))
        print(common, bit,oxygen_search)

        bit += 1
    
    co2_search = list(numbers)
    bit = 0
    while len(co2_search) != 1:
        common = count(co2_search)[bit] >= 0
        co2_search = list(filter(lambda n: bool(int(n[bit])) != common, co2_search))
        print(common, bit, len(co2_search))

        bit += 1
    print(int(co2_search[0], 2) * int(oxygen_search[0], 2))
    