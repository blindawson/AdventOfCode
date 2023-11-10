from AdventOfCode.support import support
import copy


class Positioning:
    def __init__(self, filename: str, part2: bool = False) -> None:
        decryption_key = 811589153
        self.part2 = part2
        if self.part2:
            original_list = [int(int(x) * decryption_key) for x in support.read_input(filename)]
        else:
            original_list = [int(x) for x in support.read_input(filename)]
        self.og_list = [(index, number) for index, number in enumerate(original_list)]
        self.new_list = copy.deepcopy(self.og_list)
        if part2:
            mix_num = 10
        else: 
            mix_num = 1
        for _ in range(mix_num):
            for n in self.og_list:
                self.move_num(n)

    def __repr__(self) -> str:
        return str(self.new_list)

    def move_num(self, enum: tuple[int, int]):
        current_idx = self.new_list.index(enum)
        move_distance = enum[1]

        self.new_list.pop(current_idx)  # Remove the element
        new_index = (current_idx + move_distance) % len(
            self.new_list
        )  # Calculate the new index
        self.new_list.insert(new_index, enum)  # Insert the element at the new index

    def find_groves(self) -> int:
        grove_sum = 0
        # Find 0 value
        for i, tpl in enumerate(self.new_list):
            if tpl[1] == 0:
                index0 = i
                break  # Break out of the loop once the tuple is found
        for grove_num in [1000, 2000, 3000]:
            # Find 1,000 from 0
            grove_idx = (index0 + grove_num) % len(self.new_list)  # Calculate the index using modulo operator
            grove_sum += self.new_list[grove_idx][1]  # Get the value at the calculated index
        return grove_sum

filename = r"year_2022/tests/test_inputs/20_test_input.txt"
p = Positioning(filename)
p.find_groves()