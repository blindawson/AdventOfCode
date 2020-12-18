input_file = open('day2.txt')
content = input_file.readlines()

ns = 0
ew = 0
bearing = 1  # N=0, E=1, S=2, W=3
for line in content:
    direction = line[0]
    q = int(line[1:])
    if direction == 'N' or ((bearing == 0) and (direction == 'F')):
        ns += q
    elif direction == 'S' or ((bearing == 2) and (direction == 'F')):
        ns -= q
    elif direction == 'E' or ((bearing == 1) and (direction == 'F')):
        ew += q
    elif direction == 'W' or ((bearing == 3) and (direction == 'F')):
        ew -= q
    elif direction == 'L':
        bearing = (bearing - q / 90) % 4
    elif direction == 'R':
        bearing = (bearing + q / 90) % 4

print(abs(ns) + abs(ew))
