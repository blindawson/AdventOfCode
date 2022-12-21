from support import support
from operator import add

# List of input commands
instructions = support.read_input(r"year_2022/input/09_rope_bridge.txt", flavor="split")


def is_touching(head, tail):
    # true if head and tail are within 1 column and 1 row of each other
    return (abs(head[0] - tail[0]) <= 1) and (abs(head[1] - tail[1]) <= 1)

def pull_tail(head, tail):
    movement = [0, 0]
    # For each axis
    for i in range(2):
        # If head is split from tail move it toward head
        if head[i] > tail[i]:
            movement[i] += 1
        elif head[i] < tail [i]:
            movement[i] -= 1
    return movement
            
def move_head(instruction):
    direction = instruction[0]
    magnitude = int(instruction[1])
    direction_dict = {'L': [-1, 0],
                      'R': [1, 0],
                      'U': [0, 1],
                      'D': [0, -1]}
    return [i * magnitude for i in direction_dict[direction]]
    
def add_list(list1, list2):
    return list(map(add, list1, list2))
    
def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

def part1():
    head = [0, 0]    
    tail = [0, 0]
    locs = [[0, 0]]
    for i in instructions:
        head = add_list(head, move_head(i))
        while not is_touching(head, tail):
            tail = add_list(tail, pull_tail(head, tail))
            locs.append(tail)
    return len(unique(locs))
print(f'Answer 1: {part1()}')

def part2():
    knots = [[0,0]]*10
    locs = [[0, 0]]
    for i in instructions:
        for _ in range(int(i[1])):
            knots[0] = add_list(knots[0], move_head([i[0], 1]))
            for j in range(1, 10):
                while not is_touching(knots[j-1], knots[j]):
                    knots[j] = add_list(knots[j], pull_tail(knots[j-1], knots[j]))
                    locs.append(knots[-1])
        locs = unique(locs)
        # print(f'Instructions {i}, locs {len(locs)}')
    return len(locs)
print(f'Answer 2: {part2()}')