

lines = open('./sample', 'r').readlines()
lines = [line.strip() for line in lines]



def part1():
    count = 0
    hands = [line.split()[0] for line in lines]
    bets = [int(line.split()[1]) for line in lines]
    ranks = [[] for _ in range(7)]
    
    for hand in hands:
        most = max([hand.count(char) for char in hand])
        
        if most == 5:
            ranks[0].append(hand)
        elif most ==  4:
            ranks[1].append(hand)
        elif most == 3:
           counts = [hand.count(char) for char in hand]
           if 2 in set(counts) and 3 in set(counts):
               ranks[2].append(hand)
           else:
               ranks[3].append(hand)
        elif most == 2:
            counts = [hand.count(char) for char in hand]
            if counts.count(2) == 4:
                ranks[4].append(hand)
            else:
                ranks[5].append(hand)
        else:
            ranks[6].append(hand)
    
    srtd = []

    for _ in range(len(hands)):
        for rank in ranks:
            while rank:
                if len(rank) == 1:
                    srtd.append(rank[0])
                    rank = []
                    continue
                
                order = "AKQJT98765432"
                rank_max = rank[0]
                
                for hand in rank:
                    for char in range(len(hand)):
                        if order.find(hand[char]) < order.find(rank_max[char]):
                            rank_max = hand
                            break
                
                srtd.append(rank_max)
                rank.remove(rank_max)
    print(ranks)

    print(srtd)
    return count


def part2():
    count = 0



    return count



print(part1())
