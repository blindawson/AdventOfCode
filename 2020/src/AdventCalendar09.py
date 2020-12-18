import numpy as np
import itertools

input_file = open('day2.txt')
content = [int(x) for x in input_file.readlines()]
content.append(min(content) - 1)
content.append(max(content) + 3)
content.sort()

print(content)
step = list(np.subtract(content[1:], content[:-1]))
print(step)

print(step.count(1) * step.count(3))

total_combos = 1
while True:
    try:
        next3_idx = step.index(3, 1)
    except ValueError:
        break
    # print(next3_idx)
    subset = content[:next3_idx+1]
    # print(subset)

    valid_combos = 0
    for i in range(len(subset)-1):
        coms = list(itertools.combinations(subset[1:-1], i))
        for c in coms:
            c = list(c)
            c.append(subset[0])
            c.append(subset[-1])
            c.sort()
            # print(c)
            diffs = list(np.subtract(c[1:], c[:-1]))
            # print(diffs)
            if max(diffs) <= 3:
                valid_combos += 1
    total_combos = total_combos * valid_combos
    print(valid_combos)

    del(content[:next3_idx+1])
    del(step[:next3_idx+1])
    try:
        while step[0] == 3:
            del(content[0])
            del(step[0])
    except IndexError:
        break

print(total_combos)