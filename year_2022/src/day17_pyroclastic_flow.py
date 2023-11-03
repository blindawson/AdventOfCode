from AdventOfCode.support import support
import numpy as np


class Blocks:
    def __init__(
        self, landed_blocks: list[tuple[int, int]] = None, num_blocks: int = 0
    ) -> None:
        if not landed_blocks:
            self.landed = {x: [0] for x in range(1, 8)}
        else:
            self.landed = landed_blocks
        self.num = num_blocks

    def column_len(self) -> list[int]:
        return [len(x) for x in self.landed.values()]
        
    def block_locs(self) -> list[list[int]]:
        return list(self.landed.values())
        
    def max_landed_ele(self):
        max_values = [max(x) for x in self.block_locs()]
        return max(max_values)


class Tetris:
    def __init__(self, filename: str):
        self.wind_pattern = support.read_input(filename, flavor=None, split_char=None)[
            0
        ]
        self.history = []
        self.landed_blocks = Blocks()
        self.side_chamber = [0, 8]
        self.wind_index = 0
        self.block_index = 0

        # Coordinates in (x, y) origin bottom left
        # |..@@@@.|
        # |.......|
        # |.......|
        # |.......|
        # +-------+
        # bottom left + is (0, 0)
        self.falling_blocks = [
            [(0, 0), (1, 0), (2, 0), (3, 0)],
            [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(0, 0), (0, 1), (1, 0), (1, 1)],
        ]

    def pull_wind(self) -> str:
        if self.wind_index < len(self.wind_pattern):
            wind = self.wind_pattern[self.wind_index]
            self.wind_index += 1
            return wind
        self.wind_index = 0
        print(self.landed_blocks.column_len())
        print(self.landed_blocks.block_locs())
        return self.pull_wind()

    def transpose_block(self, block: list[tuple[int, int]], vector: tuple[int, int]):
        new_position = []
        for b in block:
            # print(b, vector)
            new_position.append((b[0] + vector[0], b[1] + vector[1]))
        return new_position

    def add_block(self):
        landed_ele = self.landed_blocks.max_landed_ele()
        # print(self.landed_blocks)
        move_vector = (3, landed_ele + 4)
        if self.block_index < len(self.falling_blocks):
            new_block = self.falling_blocks[self.block_index].copy()
            new_block = self.transpose_block(new_block, move_vector)
            self.block_index += 1
            return new_block
        self.block_index = 0
        return self.add_block()

    def update_landed(self, block: list[tuple[int, int]]):
        for b in block:
            x, y = b[0], b[1]
            self.landed_blocks.landed[x] += [y]
        floor = np.inf
        for column_values in self.landed_blocks.block_locs():
            top_col = max(column_values)
            floor = min(floor, top_col)
        self.landed_blocks.landed = {
            key: [value for value in values if value >= floor]
            for key, values in self.landed_blocks.landed.items()
        }
        self.landed_blocks.num += 1

    def move_block(
        self, block: list[tuple[int, int]], direction: str
    ) -> tuple[list[tuple[int, int]], bool]:
        direction_dict = {"<": (-1, 0), ">": (1, 0), "d": (0, -1)}
        vector = direction_dict[direction]
        new_position = self.transpose_block(block, vector)

        # Check if movement is blocked
        blocked = False
        landed = False
        for b in new_position:
            # Check hitting side of chamber
            if direction != "d":
                for x in self.side_chamber:
                    if b[0] == x:
                        blocked = True
                        break
                if not blocked:
                    if b[1] in self.landed_blocks.landed[b[0]]:
                        blocked = True
                        break
            # Check hitting other block
            else:
                if b[1] in self.landed_blocks.landed[b[0]]:
                    blocked = True
                    landed = True
                    break

        if not blocked:
            block = new_position
        return block, landed

    def drop_blocks(self, num_blocks: int):
        for _ in range(num_blocks):
            b = self.add_block()
            landed = False
            while not landed:
                wind = self.pull_wind()
                b, landed = self.move_block(b, wind)
                b, landed = self.move_block(b, "d")
            self.update_landed(b)
            # print([len(x) for x in self.landed_blocks.values()])
        return self.landed_blocks.max_landed_ele()


filename = r"year_2022/tests/test_inputs/17_test_input.txt"
t = Tetris(filename)
t.drop_blocks(2022)
