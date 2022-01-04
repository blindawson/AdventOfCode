from support import support
import numpy as np


def dijkstra_algorithm(local_risks):
    grid_size = [len(local_risks), len(local_risks[0])]
    adjacent_coordinates = support.find_nearby_coordinates(local_risks)
    tentative_total_risks = np.zeros(grid_size)
    final_total_risks = np.zeros(grid_size)
    search_order = np.zeros(grid_size)
    visited = np.zeros(grid_size)
    
    
    def find_current_node():
        if (tentative_total_risks == np.zeros(grid_size)).all():
            return 0, 0
        else:
            min_risk_level = np.min(tentative_total_risks[np.nonzero(tentative_total_risks)])
            min_risk_locs = np.where(tentative_total_risks == min_risk_level)
            return min_risk_locs[0][0], min_risk_locs[1][0]
        
            
    def update_tentative_risk(current_node):
        current_x, current_y = current_node
        current_risk = tentative_total_risks[current_x, current_y]
        for adjacent in adjacent_coordinates[current_x, current_y]:
            adj_x, adj_y = adjacent
            if visited[adj_x, adj_y] == 0:
                local_risk = local_risks[adj_x, adj_y]
                if tentative_total_risks[adj_x, adj_y] == 0:
                    tentative_total_risks[adj_x, adj_y] = current_risk + local_risk
                else:
                    tentative_total_risks[adj_x, adj_y] = min(tentative_total_risks[adj_x, adj_y], 
                                                            current_risk + local_risk)


    def set_final_total_risk(current_node):
        current_x, current_y = current_node
        final_total_risks[current_x, current_y] = tentative_total_risks[current_x, current_y]
        visited[current_x, current_y] = 1
        tentative_total_risks[current_x, current_y] = 0
    
    i = 0
    while final_total_risks[-1, -1] == 0:
        # print(i)
        i += 1
        current_node = find_current_node()
        update_tentative_risk(current_node)
        set_final_total_risk(current_node)
    return int(final_total_risks[-1, -1])


local_risks = support.read_input(r'year_2021/input/15_chiton.txt', flavor='int_grid')
local_risks = np.array([np.array(xi) for xi in local_risks])
print(f'Part 1 answer: {dijkstra_algorithm(local_risks)}')


def increase_risk(grid, increase_amount):
    max_risk = 9
    increase_grid = (grid + increase_amount) % max_risk
    increase_grid = np.where(increase_grid == 0, max_risk, increase_grid)
    return increase_grid
    

big_col = np.concatenate((local_risks,
                          increase_risk(local_risks, 1),
                          increase_risk(local_risks, 2),
                          increase_risk(local_risks, 3),
                          increase_risk(local_risks, 4)),
                         axis=0)
big_map = np.concatenate((big_col,
                          increase_risk(big_col, 1),
                          increase_risk(big_col, 2),
                          increase_risk(big_col, 3),
                          increase_risk(big_col, 4)),
                         axis=1)

print(f'Part 2 answer: {dijkstra_algorithm(big_map)}')
