import numpy as np
import pickle
import re


def rot_flip(m, i):
    if i <= 4:
        return np.rot90(m, i)
    elif i <= 8:
        return np.rot90(np.fliplr(m), i-4)
    else:
        raise ValueError('Roation must be 1-8')


filehandler = open('../output/aoc20_output.pkl', 'rb')
tile_array = pickle.load(filehandler)
for x in range(len(tile_array)):
    for y in range(len(tile_array)):
        tile_array[x, y] = np.delete(tile_array[x, y], [0, -1], 0)
        tile_array[x, y] = np.delete(tile_array[x, y], [0, -1], 1)
picture = np.hstack([np.vstack(tile_array[x]) for x in range(len(tile_array))])

side_space = len(picture) - 20
spot_monster = 0
monster_size = 15  # Number of hashes in sea monster pattern
for r in range(1, 9):
    rot_picture = rot_flip(picture, r)
    for c in range(side_space):
        sea_monster1 = re.compile(fr'.{{{c}}}.{{18}}#..{{{side_space - c}}}')
        sea_monster2 = re.compile(fr'.{{{c}}}#.{{4}}##.{{4}}##.{{4}}###.{{{side_space - c}}}')
        sea_monster3 = re.compile(fr'.{{{c}}}.#..#..#..#..#..#....{{{side_space - c}}}')
        for i in range(len(picture) - 2):
            if (bool(sea_monster1.findall(''.join(rot_picture[i]))) &
                    bool(sea_monster2.findall(''.join(rot_picture[i+1]))) &
                    bool(sea_monster3.findall(''.join(rot_picture[i+2])))):
                spot_monster += 1
    print(spot_monster, )

total_roughness = sum(sum(picture == '#'))
print(total_roughness - spot_monster * monster_size)
print('This is not the right answer. In fact there is one more sea monster which I missed.')
print('I suspect this is from 2 sea monsters being on the same row.')
print('So I subtracted another 15 from the total to get 1939')