import numpy as np

target_area = {'x': (117, 164),
               'y': (-140, -89)}
target_center = [np.mean(target_area['x']), 
                 np.mean(target_area['y'])]

def move_probe(position, velocity):
    return tuple(np.add(position, velocity))
    

def update_velocity(velocity):
    if velocity[0] > 0:
        velocity[0] -= 1
    elif velocity[0] < 0:
        velocity[0] += 1
    velocity[1] -= 1
    return velocity
    
    
def check_in_target(position, target):
    return (position[0] >= target['x'][0] and
            position[0] <= target['x'][1] and
            position[1] >= target['y'][0] and
            position[1] <= target['y'][1])
    
    
def check_below_target(position, target):
    return position[1] < target['y'][0]
    
    
def check_at_target_height(position, target):
    return (position[1] >= target['y'][0] and 
            position[1] <= target['y'][1])
    
    
def shoot_at_target(x_velocity, y_velocity):
    velocity = [x_velocity, y_velocity].copy()
    position = [0, 0]
    below_target = False
    in_target = False
    min_dist_to_target = np.inf
    max_y_position = position[1]
    positions = []
    
    while not below_target and not in_target:
        position = move_probe(position, velocity)
        velocity = update_velocity(velocity)
        in_target = check_in_target(position, target_area)
        below_target = check_below_target(position, target_area)
        dist_to_target = (abs(position[0] - target_center[0]) + 
                          abs(position[1] - target_center[1]))
        min_dist_to_target = min([min_dist_to_target, dist_to_target])
        max_y_position = max([max_y_position, position[1]])
        positions.append(position)
    return positions, velocity, in_target, min_dist_to_target, max_y_position

x_velocities = []
min_distances = []
yvel = 0
xvel = 1    
x_velocities.append(xvel)
min_distances.append(shoot_at_target(xvel, yvel)[3])
xvel +=1 
x_velocities.append(xvel)
min_distances.append(shoot_at_target(xvel, yvel)[3])

max_y_that_hits = -1
total_hits = 0
for yvel in range(-140, 140):
    in_target = False
    for xvel in range(15, 165):
        _, _, in_target, _, max_y_position = shoot_at_target(xvel, yvel)        
        if in_target:
            max_y_that_hits = [xvel, yvel, max_y_position]
            total_hits += 1

print(max_y_that_hits)
print(f'Part 1 answer: {max_y_that_hits[2]}')
print(f'Part 2 answer: {total_hits}')