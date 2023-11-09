from AdventOfCode.support import support
import copy


class EncryptedNum:
    def __init__(self, index, value) -> None:
        self.og_idx = index
        self.new_idx = index
        self.value = value

    def __repr__(self) -> str:
        return f"OG Index: {self.og_idx}, New Index: {self.new_idx}, Value: {self.value}"


class Positioning:
    def __init__(self, filename):
        original_list = [int(x) for x in support.read_input(filename)]
        self.elist = [
            EncryptedNum(index, value) for index, value in enumerate(original_list)
        ]
        self.elist = {index: number for index, number in enumerate(original_list)}
        
    def move_num(self, og_idx):
        n = self.elist
