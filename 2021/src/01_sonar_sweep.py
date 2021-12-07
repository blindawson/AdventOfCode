input_file = open(r'../input/01_sonar_sweep.txt')
content = input_file.read().splitlines()
content = [int(c) for c in content]

depth_increase = 0
for c in range(1, len(content)):
    if content[c] > content[c-1]:
        depth_increase += 1

print(f'Part 1 answer: {depth_increase}')

depth_increase = 0
for c in range(3, len(content)):
    group_1 = sum(content[c-3:c])
    group_2 = sum(content[c-2:c+1])
    if group_2 > group_1:
        depth_increase += 1

print(f'Part 2 answer: {depth_increase}')
