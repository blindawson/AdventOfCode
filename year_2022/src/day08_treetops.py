from support import support
import numpy as np

trees = support.read_input(r'year_2022/input/08_treetops.txt', flavor='int_grid')
trees = np.array([np.array(xi) for xi in trees])

vis = np.ones_like(trees)

def is_vis(loc):
    y, x = loc
    dir_dict = {'w': trees[y, :x],
                'e': trees[y, x+1:],
                'n': trees[:y, x],
                's': trees[y+1:, x]}
    vis_count = 0
    for d in dir_dict:
        if all(dir_dict[d] < trees[y, x]):
            vis_count += 1
    return vis_count

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        vis[i, j] = is_vis([i, j])
        
print(f'Part 1 Answer: {(vis > 0).sum()}')

def view(loc, direction):
    y, x = loc
    m, n = trees.shape
    range_dict = {'w': [[y], range(x-1, 0-1, -1)],
                  'e': [[y], range(x+1, n, 1)],
                  'n': [range(y-1, 0-1, -1), [x]],
                  's': [range(y+1, m, 1), [x]],}
    r = range_dict[direction]
    vis_dist = 0
    for a in r[0]:
        for b in r[1]:
            vis_dist += 1
            if trees[a, b] >= trees[y, x]:
                return vis_dist
    return vis_dist
    
vis = np.ones_like(trees)
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        for r in ['w', 'e', 'n', 's']:
            vis[i, j] *= view([i, j], r)
print(f'Part 2 Answer: {vis.max()}')