from AdventOfCode.support import support
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class Maze:
    def __init__(self, filename, part2=False):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.start_yx = (0, 1)
        self.end_yx = (self.file_input.shape[0] - 1, self.file_input.shape[1] - 2)

        if part2:
            self.file_input = np.char.replace(self.file_input, ">", ".")
            self.file_input = np.char.replace(self.file_input, "<", ".")
            self.file_input = np.char.replace(self.file_input, "^", ".")
            self.file_input = np.char.replace(self.file_input, "v", ".")

        self.explored = np.zeros(self.file_input.shape, dtype=int)
        self.explored[self.start_yx] = 1

        self.g = nx.DiGraph(path_length=0)
        self.g.add_node(self.start_yx, explored=False)
        self.g.add_node(self.end_yx, explored=False)

        self.max_length = 0

        # Create Network
        nodes = [self.start_yx]
        while nodes:
            new_nodes = []
            for node in nodes:
                new_nodes += self.build_edges(node)
            nodes = new_nodes
        for node in list(self.g.nodes):
            self.g.nodes[node]["explored"] = False

        self.g.nodes[self.start_yx]["explored"] = True

    def build_edges(self, yx):
        self.g.nodes[yx]["explored"] = True
        adj_node_dists = {}
        for key, value in self.find_adj_nodes(yx).items():
            if key in list(self.g.nodes):
                if not self.g.nodes[key]["explored"]:
                    adj_node_dists[key] = value
            else:
                self.g.add_node(key, explored=False)
                adj_node_dists[key] = value
        new_nodes = []
        for node, path_length in adj_node_dists.items():
            self.add_edge(yx, node, path_length)
            new_nodes.append(node)
        return new_nodes

    def find_adj_nodes(self, yx00):
        adjs0 = self.search_adjacent(yx00)
        adjs1 = {}
        for adj in adjs0:
            path_len = 1
            yx = adj
            new_adjs = self.search_adjacent(yx, yx00)
            while len(new_adjs) == 1:
                path_len += 1
                yx0 = yx
                yx = new_adjs[0]
                new_adjs = self.search_adjacent(yx, yx0)
            adjs1[yx] = path_len
        return adjs1

    def add_edge(self, node1, node2, path_length):
        if (node1, node2) not in list(self.g.edges):
            self.g.add_edge(node1, node2, weight=path_length)
            if not (self.is_perimeter_node(node1) and self.is_perimeter_node(node2)):
                self.g.add_edge(node2, node1, weight=path_length)

    def follow_path(self, yx, graph):
        graph.nodes[yx]["explored"] = True
        adjs = [
            x[1] for x in list(graph.edges(yx)) if not graph.nodes[x[1]]["explored"]
        ]

        for adj in adjs:
            new_graph = graph.copy()
            new_graph.graph["path_length"] += new_graph.edges[yx, adj]["weight"]
            new_graph.nodes[adj]["explored"] = True
            self.follow_path(adj, new_graph.copy())
            if new_graph.nodes[self.end_yx]["explored"]:
                self.max_length = max(self.max_length, new_graph.graph["path_length"])
                print(self.max_length)

    def is_perimeter_node(self, yx):
        adjs = len(self.search_adjacent(yx))
        return adjs <= 3

    def search_adjacent(self, yx, previous_yx=None):
        adjs1 = support.list_neighbors(yx, self.file_input)
        adjs2 = []
        for adj in adjs1:
            adj_char = self.file_input[adj]
            if adj_char == ".":
                if adj != previous_yx:
                    adjs2.append(adj)
        return adjs2

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
        plt.show()
