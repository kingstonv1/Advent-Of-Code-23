lines = open('./sample.txt', 'r').readlines()
lines = [line.strip() for line in lines]

def part1():
    count = 0

    for line in lines:
        line = line[9:]
        lns = line.split('|')
        winners = list(map(int, lns[0].split()))
        have = list(map(int, lns[1].split()))

        c = 0
        for winner in winners:
            c += have.count(winner)
        
        count += 2 ** (c - 1) if c != 0 else 0
    
    return count


def part2():
    count = len(lines)
    wins = [0 for _ in range(len(lines))]
    mult = [1 for _ in range(len(lines))]

    for i in range(len(lines)):
        line = lines[i][9:]
        lns = line.split('|')
        winners = list(map(int, lns[0].split()))
        have = list(map(int, lns[1].split()))

        c = 0

        for winner in winners:
            c += have.count(winner)

        wins[i] += c

    for i in range(len(wins)):
        win = wins[i]
        
        for x in range(win):
            mult[i + x] += 1

    for i in range(len(wins)):
        count += wins[i] * mult[i]

    return count

print(part2())
