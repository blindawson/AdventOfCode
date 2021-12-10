input_file = open('../input/02_dive.txt')
dive_instructions = input_file.read().splitlines()


def read_instructions(instruction, x, z):
    [direction, distance] = instruction.split()
    distance = int(distance)
    if direction == 'forward':
        x += distance
    elif direction == 'up':
        z -= distance
    elif direction == 'down':
        z += distance
    else:
        raise ValueError(f'{direction} direction not valid')
    return x, z

x = 0
z = 0
for i in dive_instructions:
    [x, z] = read_instructions(i, x, z)

print(f'Part 1 answer: {x*z}')


def read_instructions_part2(instruction, x, z, aim):
    [direction, distance] = instruction.split()
    distance = int(distance)
    if direction == 'forward':
        x += distance
        z += distance * aim
    elif direction == 'up':
        aim -= distance
    elif direction == 'down':
        aim += distance
    else:
        raise ValueError(f'{direction} direction not valid')
    return x, z, aim


x = 0
z = 0
aim = 0
for i in dive_instructions:
    [x, z, aim] = read_instructions_part2(i, x, z, aim)

print(f'Part 2 answer: {x*z}')
