lines = open('./puz.txt', 'r').readlines()

def part1():    
    total = 0

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
    total = 0
    lines = open('./sample2.txt', 'r').readlines()

    for line in lines:
        for i in range(len(line)):
            if line[i].isnumeric():
                first = line[i]
                break

            for num in nums.keys():
                # if the numeric string is found (by slicing)
                if line[i:min(i + len(num), len(line))] == num:
                    first = nums[num]
                    break

        for i in reversed(range(len(line))):
            if line[i].isnumeric():
                last = line[i]
                break

            for num in nums.keys():
                if line[max(i - len(num), 0):i + 1] == num:
                    last = nums[num]
                    break
        print(int(first + last))
        total += int(first + last)

    return total


print(part2())
