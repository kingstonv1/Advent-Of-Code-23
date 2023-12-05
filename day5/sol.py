lines = open('./puz.txt', 'r').readlines()
lines = [line.strip() for line in lines]


def part1():
    seeds = list(map(int, lines[0][6:].split()))
    maps = []
    temp = []
    ans = float('inf')

    for i in range(2, len(lines)):
        line = lines[i]

        if not line:
            maps.append(temp)
            temp = []
            continue

        if not line[0].isnumeric():
            continue

        temp.append(tuple(map(int, line.split())))

    maps.append(temp)

    for seed in seeds:
        current = seed

        for c in maps:
            for conversion in c:
                if current in range(conversion[1], conversion[1] + conversion[2]):
                    diff = conversion[1] - conversion[0]
                    current -= diff
                    break

        ans = min(current, ans)

    return ans

def part2():
    seeds = set(map(int, lines[0][6:].split()))
    maps = []
    temp = []

    for i in range(2, len(lines)):
        line = lines[i]

        if not line:
            maps.append(temp)
            temp = []
            continue

        if not line[0].isnumeric():
            continue

        temp.append(tuple(map(int, line.split())))

    maps.append(temp)
    

print(part2())
