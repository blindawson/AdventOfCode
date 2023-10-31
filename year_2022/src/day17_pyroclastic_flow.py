from AdventOfCode.support import support
import copy


class Tetris:
    def __init__(self, filename: str):
        self.wind_pattern = support.read_input(filename, flavor=None, split_char=None)[
            0
        ]
        self.landed_blocks = [(x, 0) for x in range(7)]
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
        return self.pull_wind()

    def transpose_block(self, block: list[tuple[int, int]], vector: tuple[int, int]):
        new_position = []
        for b in block:
            # print(b, vector)
            new_position.append((b[0] + vector[0], b[1] + vector[1]))
        return new_position

    def add_block(self):
        landed_ele = self.max_landed_ele()
        move_vector = (3, landed_ele + 4)
        if self.block_index < len(self.falling_blocks):
            new_block = self.falling_blocks[self.block_index].copy()
            new_block = self.transpose_block(new_block, move_vector)
            self.block_index += 1
            return new_block
        self.block_index = 0
        return self.add_block()

    def max_landed_ele(self):
        return max([b[1] for b in self.landed_blocks])

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
            # Check out of bounds left/right
            for x in self.side_chamber:
                if b[0] == x:
                    blocked = True
            # Check hitting other block
            for i in self.landed_blocks:
                if b == i:
                    blocked = True
                    if direction == "d":
                        landed = True

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
            self.landed_blocks += b
        return self.max_landed_ele()


# filename = r"year_2022/tests/test_inputs/17_test_input.txt"
# t = Tetris(filename)
# t.drop_blocks(10)
