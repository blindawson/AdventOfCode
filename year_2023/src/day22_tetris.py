from AdventOfCode.support import support
import numpy as np


class Tetris:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)

        self.blocks = [self.process_input(row) for row in self.file_input]
        self.blocks = sorted(self.blocks, key=lambda x: x["z1"])

        top_stack = self.create_top_of_stack()
        self.settled_blocks = [
            self.settle_block(block, top_stack) for block in self.blocks
        ]

    def process_input(self, row):
        parts = row.split("~")
        x1, y1, z1 = [int(x) for x in parts[0].split(",")]
        x2, y2, z2 = [int(x) for x in parts[1].split(",")]
        return {
            "x1": min(x1, x2),
            "y1": min(y1, y2),
            "z1": min(z1, z2),
            "x2": max(x1, x2),
            "y2": max(y1, y2),
            "z2": max(z1, z2),
        }

    def create_top_of_stack(self):
        max_x = max(x["x2"] for x in self.blocks)
        max_y = max(x["y2"] for x in self.blocks)
        top_stack = np.zeros((max_y + 1, max_x + 1), dtype=int)
        return top_stack

    def block_coordinates(self, block):
        coordinates = []
        for x1 in range(block["x1"], block["x2"] + 1):
            for y1 in range(block["y1"], block["y2"] + 1):
                for z1 in range(block["z1"], block["z2"] + 1):
                    coordinates.append((x1, y1, z1))
        return coordinates

    def overlapping(self, block, top_stack):
        for coordinate in self.block_coordinates(block):
            x, y, z = coordinate
            overlapped = top_stack[(y, x)] == z
            if overlapped:
                return True
        return False

    def lower_block(self, block):
        new_block = block.copy()
        new_block["z1"] -= 1
        new_block["z2"] -= 1
        return new_block

    def update_top_stack(self, block, top_stack):
        for coordinate in self.block_coordinates(block):
            x, y, z = coordinate
            top_stack[(y, x)] = max(top_stack[(y, x)], z)
        return top_stack

    def settle_block(self, block, top_stack):
        lowered_block = self.lower_block(block)
        while not self.overlapping(lowered_block, top_stack):
            block = lowered_block
            lowered_block = self.lower_block(block)
        top_stack = self.update_top_stack(block, top_stack)
        return block

    def disintegrate_blocks(self):
        safely_removed = 1
        falling_blocks = 0
        base_top_stack = self.create_top_of_stack()
        for r, remove_block in enumerate(self.settled_blocks[:-1]):
            safe = True
            above_top_stack = base_top_stack.copy()
            for above_block in self.settled_blocks[r + 1 :]:
                lower_block = self.settle_block(above_block, above_top_stack)
                falling_block = above_block != lower_block
                if falling_block:
                    safe = False
                    falling_blocks += 1
            if safe:
                safely_removed += 1
            base_top_stack = self.update_top_stack(remove_block, base_top_stack)
        return safely_removed, falling_blocks
