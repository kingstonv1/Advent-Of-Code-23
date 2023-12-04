lines = open('./puz.txt', 'r').readlines()
lines = [line.strip() + '.' for line in lines]


def part1():
    count = 0
    nums = dict()
    coords = dict()

    for x in range(len(lines)):
        str_buf = ''
        coords_buf = []

        # initial pass to record numbers and coords to check
        for y in range(len(lines[x])):
            char = lines[x][y]

            if char.isnumeric():
                str_buf += char
                coords_buf.append((x, y))
            else:
                if not str_buf:
                    continue

                coords[tuple(coords_buf)] = int(str_buf)
                str_buf, coords_buf = '', []

    added = set()

    # second pass to count symbol-adjacent nums
    for i in range(len(lines)):
        for z in range(len(lines[x])):
            if lines[i][z] in '1234567890.':
                continue

            for coord_set in coords.keys():
                if coord_set in added:
                    continue
                
                for x, y in coord_set:
                    if x in range(i - 1, i + 2) and y in range(z - 1, z + 2):
                        count += coords[coord_set]
                        added.add(coord_set)
                        break

    return count

def part2():
    count = 0

    for x in range(len(lines)):
        str_buf = ''
        coords_buf = []

        # initial pass to record numbers and coords to check
        for y in range(len(lines[x])):
            char = lines[x][y]

            if char.isnumeric():
                str_buf += char
                coords_buf.append((x, y))
            else:
                if not str_buf:
                    continue

                coords[tuple(coords_buf)] = int(str_buf)
                str_buf, coords_buf = '', []
 
    return count

print(part2())
