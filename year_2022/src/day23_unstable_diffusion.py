from AdventOfCode.support import support
import numpy as np


class ElfMap:
    def __init__(
        self,
        filename: str,
        rounds: int = 10,
        expansion_rate: int = 50,
        part2: bool = False,
    ):
        self.file_input = np.array(support.read_input(filename, flavor="str_grid"))
        self.expansion_rate = expansion_rate
        self.elf_map = np.empty(self.file_input.shape, dtype=dict)
        for index, item in np.ndenumerate(self.file_input):
            self.elf_map[index] = self.fill_dict(item)
        self.dir_order = 0
        for _ in range(rounds):
            self.expand_map()
            self.move_elves()
        self.part1_answer = self.count_empty_tiles()[0]
        print(f"Empty tiles: {self.part1_answer}")
        if part2:
            self.round = rounds
            self.elf_moved = True
            while self.elf_moved:
                self.expand_map()
                self.move_elves()
                self.round += 1

    def fill_dict(self, hash: str):
        hash_dict = {".": False, "#": True}
        elf_dict = {
            "elf present": hash_dict[hash],
            "next position": None,
        }
        return elf_dict

    def list_ordinal_adjacent(self, pos: tuple[int]):
        return [
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
        ]

    def list_all_adjacent(self, pos: tuple[int]):
        return [
            (pos[0], pos[1] + 1),
            (pos[0], pos[1] - 1),
            (pos[0] + 1, pos[1]),
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1] + 1),
            (pos[0] - 1, pos[1] - 1),
            (pos[0] + 1, pos[1] - 1),
            (pos[0] - 1, pos[1] + 1),
        ]

    def elf_nearby(self, near_spots: list[tuple[int]]) -> bool:
        return any([self.elf_map[x]["elf present"] for x in near_spots])

    def expand_map(self):
        # if elf is on edge of array, expand map
        edges = (
            list(self.elf_map[0, :])
            + list(self.elf_map[-1, :])
            + list(self.elf_map[:, 0])
            + list(self.elf_map[:, -1])
        )
        if any([x["elf present"] for x in edges]):
            new_map = np.empty(
                (
                    self.elf_map.shape[0] + self.expansion_rate * 2,
                    self.elf_map.shape[1] + self.expansion_rate * 2,
                ),
                dtype=dict,
            )
            new_map[:, :] = {
                "elf present": False,
                "next position": None,
            }
            new_map[
                self.expansion_rate : self.expansion_rate + self.elf_map.shape[0],
                self.expansion_rate : self.expansion_rate + self.elf_map.shape[1],
            ] = self.elf_map
            self.elf_map = new_map

    def find_next_move(self, pos: tuple[int]):
        adjacent_groups = {
            "north": [
                (pos[0] - 1, pos[1] - 1),
                (pos[0] - 1, pos[1]),
                (pos[0] - 1, pos[1] + 1),
            ],
            "south": [
                (pos[0] + 1, pos[1] - 1),
                (pos[0] + 1, pos[1]),
                (pos[0] + 1, pos[1] + 1),
            ],
            "west": [
                (pos[0] + 1, pos[1] - 1),
                (pos[0], pos[1] - 1),
                (pos[0] - 1, pos[1] - 1),
            ],
            "east": [
                (pos[0] + 1, pos[1] + 1),
                (pos[0], pos[1] + 1),
                (pos[0] - 1, pos[1] + 1),
            ],
        }
        group_order = [
            ["north", "south", "west", "east"],
            ["south", "west", "east", "north"],
            ["west", "east", "north", "south"],
            ["east", "north", "south", "west"],
        ]

        if not self.elf_nearby(self.list_all_adjacent(pos)):
            return None

        for dir in group_order[self.dir_order]:
            if not self.elf_nearby(adjacent_groups[dir]):
                return adjacent_groups[dir][1]

    def move_elves(self):
        # Find next positions
        any_elf_movement = False
        for index, item in np.ndenumerate(self.elf_map):
            if item["elf present"]:
                next_position = self.find_next_move(index)
                self.elf_map[index]["next position"] = next_position
                if next_position:
                    any_elf_movement = True
        if not any_elf_movement:
            self.elf_moved = False
        # Move next positions
        for index, item in np.ndenumerate(self.elf_map):
            if item["elf present"] and item["next position"]:
                # if next position only in next_positions once.
                next_pos_neighbors = self.list_ordinal_adjacent(item["next position"])
                next_pos_neighbors = support.remove_out_of_bounds_coordinates(
                    next_pos_neighbors, self.elf_map
                )
                neighbor_next_pos = [
                    self.elf_map[x]["next position"] for x in next_pos_neighbors
                ]
                if sum([x == item["next position"] for x in neighbor_next_pos]) == 1:
                    # Move to next position
                    self.elf_map[item["next position"]] = {
                        "elf present": True,
                        "next position": None,
                    }
                    self.elf_map[index] = {
                        "elf present": False,
                        "next position": None,
                    }
        # Rotate direction order
        self.dir_order = (self.dir_order + 1) % 4

    def count_empty_tiles(self) -> list[int, np.array]:
        elf_present_columns = [
            any([y["elf present"] for y in self.elf_map[:, x]])
            for x in range(self.elf_map.shape[1])
        ]

        first_col = elf_present_columns.index(True)
        last_col = len(elf_present_columns) - elf_present_columns[::-1].index(True) - 1

        elf_present_rows = [
            any([x["elf present"] for x in self.elf_map[y, :]])
            for y in range(self.elf_map.shape[0])
        ]

        first_row = elf_present_rows.index(True)
        last_row = len(elf_present_rows) - elf_present_rows[::-1].index(True) - 1

        reduced_map = self.elf_map[first_row : last_row + 1, first_col : last_col + 1]
        empty_count = 0
        for _, item in np.ndenumerate(reduced_map):
            if item["elf present"] == False:
                empty_count += 1

        return empty_count, reduced_map

    def print_map(self) -> None:
        reduced_map = self.count_empty_tiles()[1]
        binary_map = np.zeros(reduced_map.shape, dtype=int)
        for index, item in np.ndenumerate(reduced_map):
            if item["elf present"]:
                binary_map[index] = 1
        print(binary_map)
