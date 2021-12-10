crab_file = open(r'../input/07_crab_alignment.txt')
crab_coordinates = [int(x) for x in crab_file.read().split(',')]
min_crab_position = min(crab_coordinates)
max_crab_position = max(crab_coordinates)

fuel_costs = []
for position in range(min_crab_position, max_crab_position+1):
    fuel_cost = 0
    for crab_position in crab_coordinates:
        distance = abs(position - crab_position)
        fuel_cost += distance
    fuel_costs.append(fuel_cost)

print(f'Part 1 answer: {min(fuel_costs)}')

fuel_costs = []
for position in range(min_crab_position, max_crab_position+1):
    fuel_cost = 0
    for crab_position in crab_coordinates:
        distance = abs(position - crab_position)
        fuel_cost += (distance + 1) * distance / 2
    fuel_costs.append(fuel_cost)

print(f'Part 2 answer: {min(fuel_costs)}')
