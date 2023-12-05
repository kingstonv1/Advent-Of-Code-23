lines = open('./puz.txt', 'r').readlines()
lines = [line.strip() for line in lines]

class DoubleBreak(Exception): pass

def part1():    
    total = 0
    first, last = None, None

    for line in lines:
        for char in line:
            if char.isnumeric():
                first = char
                break

        for char in reversed(line):
            if char.isnumeric():
                last = char
                break

        total += int(first + last)

    return total


def part2():
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    first, last = None, None
    total = 0

    for line in lines:
        for i in range(len(line)):
            try:
                if line[i].isnumeric():
                    first = line[i]
                    break

                for num in nums.keys():
                    # if the numeric string is found (by slicing)
                    if line[i:i + len(num)] == num:
                        first = nums[num]
                        raise DoubleBreak
            except:
                break

        for i in reversed(range(len(line))):
            try:
                if line[i].isnumeric():
                    last = line[i]
                    break

                for num in nums.keys():
                    if line[i:i + len(num)] == num:
                        last = nums[num]
                        raise DoubleBreak
            except DoubleBreak:
                break

        total += int(first + last)

    return total


print(part2())
