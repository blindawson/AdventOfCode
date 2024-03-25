from AdventOfCode.support import support
import networkx as nx
import math
import matplotlib.pyplot as plt
from itertools import combinations


class Day25:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.process_input()
        self.g = self.create_network()

    def process_input(self):
        input_dict = {}
        for row in self.file_input:
            key = row[0][:-1]
            value = row[1:]
            input_dict[key] = value
        self.file_input = input_dict

    def create_network(self):
        G = nx.Graph()
        for key, values in self.file_input.items():
            for value in values:
                G.add_edge(key, value)
        return G

    def count_networks(self, wire_diagram):
        connected_components = list(nx.connected_components(wire_diagram))
        num_nodes_in_components = [len(component) for component in connected_components]
        return num_nodes_in_components

    def plot_graph(self):
        pos = nx.circular_layout(self.g)  # Define the positions of nodes
        nx.draw(
            self.g,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=2000,
            font_weight="bold",
        )

        # Add edge labels
        labels = nx.get_edge_attributes(self.g, "weight")
        nx.draw_networkx_edge_labels(self.g, pos, edge_labels=labels)

        # Display the graph
        # plt.show()
        return plt

    def cut_wires(self):
        wire_diagram = self.g.copy()
        for wire in nx.minimum_edge_cut(wire_diagram):
            wire_diagram.remove_edge(wire[0], wire[1])
        group_sizes = self.count_networks(wire_diagram)
        return group_sizes
