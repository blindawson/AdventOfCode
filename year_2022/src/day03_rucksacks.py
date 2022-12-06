import re

input_file = open(r'year_2022/input/03_rucksacks.txt')
content = input_file.read().splitlines()

def priority(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

score = 0
for t in content:
    rucksack_size = int(len(t) / 2)
    rucksack1 = t[:rucksack_size]
    rucksack2 = t[rucksack_size:]
    for c in rucksack1:
        if re.search(c, rucksack2):
            score += priority(c)
            break
print(f'Part 1 Answer: {score}')

score = 0
for i in range(int(len(content) / 3)):
    r0 = content[i*3]
    r1 = content[i*3 + 1]
    r2 = content[i*3 + 2]
    for c in r0:
        if re.search(c, r1) and re.search(c, r2):
            score += priority(c)
            break
print(f'Part 2 Answer: {score}')
