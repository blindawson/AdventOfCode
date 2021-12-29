from numpy.lib.arraypad import _view_roi
from support import support
import numpy as np


local_risks = support.read_input(r'year_2021/input/15_chiton.txt', flavor='int_grid')
local_risks = np.array([np.array(xi) for xi in local_risks])
grid_size = [len(local_risks), len(local_risks[0])]
adjacent_coordinates = support.find_nearby_coordinates(local_risks)
tentative_total_risks = np.zeros(grid_size)
final_total_risks = np.zeros(grid_size)
search_order = np.zeros(grid_size)
visited = np.zeros(grid_size)

tentative_total_risks[0, 0] = local_risks[0, 0]

def find_current_node():
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
    

while final_total_risks[-1, -1] == 0:
    current_node = find_current_node()
    update_tentative_risk(current_node)
    set_final_total_risk(current_node)

print(f'Part 1 answer: {final_total_risks[-1, -1]}')