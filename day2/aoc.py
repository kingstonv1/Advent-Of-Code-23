import sys

sys.stdin = open('./aoc.txt', 'r')
maxs = {'red': 12, 'green': 13, 'blue': 14}
total = 0

for i in range(1, 101):
	inp = input()[8:].split()
	flag = True
	temp = {'red': 0, 'green': 0, 'blue': 0}

	for s in range(len(inp)):
		if inp[s].isnumeric():
			color = inp[s + 1]
			color = ''.join([i for i in color if i.isalpha()])
			num = int(inp[s])
			temp[color] = max(temp[color], num)

	total += temp['red'] * temp['blue'] * temp['green']

print(total)
