from support import support
import networkx as nx
import numpy as np


class ClassName:
    def __init__(self, filename):
        self.map = np.array(support.read_input(filename, flavor="str_grid"))
        self.graph = nx.Graph()
        # TODO: create a map showing what has been explored

    def map_grid(self):
        start_position = np.where(self.map == "S")
        start_position = (start_position[0][0], start_position[1][0])
        self.create_nodes(start_position)
        paths = self.find_nearby_paths(start_position)
        # TODO: create path dicts and add to path queue
        # TODO: while path queue is not empty
        # TODO: path is path queue.pop(0)
        # TODO: map surroundings

    def create_nodes(self, location: tuple, start_node=False):
        self.graph.add_node(
            (location, "NS"), location=location, heading="NS", start_node=start_node
        )
        self.graph.add_node(
            (location, "EW"), location=location, heading="EW", start_node=start_node
        )
        self.graph.add_edge((location, "NS"), (location, "EW"), weight=1000)

    def create_path_dict(
        self, location: tuple, heading: str, source_node: nx.nodes, distance: int = 0
    ):
        return {
            "location": location,
            "heading": heading,
            "source node": source_node,
            "distance": distance,
        }

    def find_nearby_paths(self, path_location: tuple) -> list[tuple[int, int]]:
        nearby_spaces = support.list_neighbors(path_location, self.map)
        nearby_spaces = [x for x in nearby_spaces if self.map[x] != "#"]
        # TODO: only take paths that have not been explored
        return nearby_spaces

    def find_heading(self, current_location, new_location):
        location_difference = support.subtract_tuples(new_location, current_location)
        if location_difference == (0, 1):
            return "E"
        elif location_difference == (0, -1):
            return "W"
        elif location_difference == (1, 0):
            return "S"
        elif location_difference == (-1, 0):
            return "N"

    def map_surroundings(self, path_dict: dict):
        # TODO: find nearby paths -> tuples
        # TODO: if nearby path has 3+ neighbors. create nodes and connect to previous node
        # TODO: change those tuples into dicts
        pass

    def part1(self):
        # TODO: find quickest path from start nodes to end nodes.
        pass

    def part2(self):
        pass


filename = r"year_2024/tests/test_inputs/16_test_input.txt"
# filename = r"year_2024/input/16_node_map.txt"
m = ClassName(filename)
support.print_grid(m.map)
