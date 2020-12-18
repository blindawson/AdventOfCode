import copy

input_file = open('day2.txt')
content0 = input_file.readlines()
for i, row in enumerate(content0):
    content0[i] = list(row)
    try:
        content0[i].remove('\n')
    except ValueError:
        continue
content1 = copy.deepcopy(content0)

ct = 0
no_change = False
while not no_change:
    ct += 1
    print(ct)
    for i, row in enumerate(content0):
        for j, seat in enumerate(row):
            if seat == '.':
                content1[i][j] = seat
            else:
                near = []
                for ii in range(-1, 2):
                    for jj in range(-1, 2):
                        look_dist = 1
                        while True:
                            if ((ii == 0) and (jj == 0)) or ((i+ii*look_dist < 0) or (j+jj*look_dist < 0)):
                                break
                            else:
                                try:
                                    nearij = content0[i + ii*look_dist][j + jj*look_dist]
                                    if nearij == '.':
                                        look_dist += 1
                                    else:
                                        near.append(nearij)
                                        break
                                except IndexError:
                                    break

            if (seat == 'L') and (near.count('#') == 0):
                content1[i][j] = '#'
            elif (seat == '#') and (near.count('#') >= 5):
                content1[i][j] = 'L'
            else:
                content1[i][j] = seat
    if content0 == content1:
        no_change = True
    content0 = copy.deepcopy(content1)

occupied = 0
for x in content0:
    occupied += x.count('#')
print(occupied)

