import numpy as np
from AdventOfCode.support import support


class Node:
    def __init__(self, y, x, letter):
        self.x = x  # X location in grid
        self.y = y  # Y location in grid
        self.letter = letter  # Letter value of location
        self.score = ord(letter)
        self.nearby = []
        self.cost0 = 0
        self.cost1 = 0
        self.visited = False

    def __str__(self):
        return f" Node at: {self.x}, {self.y}, {self.letter}. Nearby: {[(n.x, n.y) for n in self.nearby]}"


class Dijkstra_grid:
    def __init__(self, grid, part2=False):
        self.grid = np.empty(grid.shape, dtype=object)
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                self.grid[y, x] = Node(y, x, grid[y][x])
        self.current_node = self.find_current_node(find_letter="S")
        self.current_node.score = ord("a")
        self.end_node = self.find_current_node(find_letter="E")
        self.end_node.score = ord("z")
        self.find_reachable_coordinates()
        self.part2 = part2
        self.path_length = self.find_path_length()

    def find_reachable_coordinates(self):
        for y in range(self.grid.shape[0]):
            for x in range(self.grid.shape[1]):
                n = self.grid[y, x]
                nearby_coordinates = [
                    (n.y - 1, n.x),
                    (n.y, n.x - 1),
                    (n.y + 1, n.x),
                    (n.y, n.x + 1),
                ]
                # Remove coordinates beyond the edges of the grid
                nearby_coordinates = support.remove_out_of_bounds_coordinates(
                    nearby_coordinates, self.grid
                )
                # Remove coordinates more than one level above current node
                bad_coordinates = []
                for coordinate in nearby_coordinates:
                    if self.grid[coordinate].score - n.score > 1:
                        bad_coordinates.append(coordinate)
                [nearby_coordinates.remove(c) for c in bad_coordinates]
                nearby_coordinates = [self.grid[c] for c in nearby_coordinates]
                n.nearby = nearby_coordinates

    def find_current_node(self, find_letter=None):
        # Flatten the 2D array into a 1D array of node objects
        flattened_array = self.grid.flatten()

        if find_letter:
            # Pull the letter attribute
            letters = np.array([node.letter for node in flattened_array])

            # Find the node with the minimum non-zero cost0 value
            current_loc = np.where(letters == find_letter)[0][0]

        else:
            # Pull the cost0 attribute
            cost0_values = np.array([node.cost0 for node in flattened_array])

            # Filter out values that are equal to zero
            non_zero_values = cost0_values[cost0_values != 0]

            # Find the minimum non-zero 'cost0' value
            min_cost0 = np.min(non_zero_values)

            # Find the node with the minimum non-zero cost0 value
            current_loc = np.where(cost0_values == min_cost0)[0][0]

        # Convert the 1D index back to the 2D indices
        current_loc_2d = np.unravel_index(current_loc, self.grid.shape)

        # Get the node with the smallest cost0 attribute
        return self.grid[current_loc_2d]

    def update_cost0(self):
        # print(self.current_node)
        for adjacent in self.current_node.nearby:
            if not adjacent.visited:
                if adjacent.cost0 == 0:
                    adjacent.cost0 = self.current_node.cost0 + 1
                else:
                    adjacent.cost0 = min(adjacent.cost0, self.current_node.cost0 + 1)
                if self.part2 and adjacent.score == ord("a"):
                    adjacent.cost0 = 1

    def set_cost1(self):
        self.current_node.cost1 = self.current_node.cost0
        self.current_node.cost0 = 0
        self.current_node.visited = True

    def find_path_length(self):
        i = 0
        while self.end_node.cost1 == 0:
            i += 1
            # print(i)
            if i > 1:
                self.current_node = self.find_current_node()
            self.update_cost0()
            self.set_cost1()
        return int(self.end_node.cost1)

    def print_path(self):
        print(np.array([[node.cost1 for node in row] for row in self.grid]))
