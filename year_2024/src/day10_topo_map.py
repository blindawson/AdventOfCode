from support import support
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class ClassName:
    def __init__(self, filename):
        self.file_input = np.array(support.read_input(filename, flavor="int_grid"))
        self.graph = nx.DiGraph()

        indices = np.where(self.file_input == 0)
        for i, j in zip(*indices):
            self.graph.add_node((i, j), value=0)

        for n in range(9):
            nodes_with_value_n = [
                node for node, data in self.graph.nodes(data=True) if data["value"] == n
            ]
            for node in nodes_with_value_n:
                adj_nodes = support.list_ordinal_adjacent(node)
                for a in adj_nodes:
                    out_of_bounds = support.point_out_of_bounds(
                        a[0], a[1], self.file_input
                    )
                    if not out_of_bounds:
                        increment_by_one = (
                            self.file_input[a[0], a[1]] - 1 == self.file_input[node]
                        )
                        if increment_by_one:
                            self.graph.add_edge(node, a)
                            self.graph.nodes[a]["value"] = n + 1

    def display_graph(self):
        pos = {node: (node[1], -node[0]) for node in self.graph.nodes()}
        labels = nx.get_node_attributes(self.graph, "value")

        plt.figure(figsize=(8, 8))
        nx.draw(
            self.graph,
            pos,
            with_labels=True,
            labels=labels,
            node_size=500,
            node_color="lightblue",
            font_size=10,
            font_color="black",
        )
        plt.show()

    def part1(self):
        count = 0
        for node, data in self.graph.nodes(data=True):
            if data["value"] == 0:
                reachable_nodes = nx.descendants(self.graph, node)
                for reachable_node in reachable_nodes:
                    if self.graph.nodes[reachable_node]["value"] == 9:
                        count += 1
        return count

    def part2(self):
        count = 0
        for node, data in self.graph.nodes(data=True):
            if data["value"] == 0:
                for target_node, target_data in self.graph.nodes(data=True):
                    if target_data["value"] == 9:
                        paths = list(
                            nx.all_simple_paths(
                                self.graph, source=node, target=target_node
                            )
                        )
                        count += len(paths)
        return count
