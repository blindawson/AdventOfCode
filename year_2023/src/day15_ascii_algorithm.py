from AdventOfCode.support import support
import numpy as np
import re


class Hash:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=",")[
            0
        ]

    def hash_alg(self, input_str):
        current_value = 0
        for i in input_str:
            ascii = ord(i)
            current_value += ascii
            current_value *= 17
            current_value = current_value % 256
        return current_value

    def add_hash(self):
        sum_hash = 0
        for f in self.file_input:
            sum_hash += self.hash_alg(f)
        return sum_hash

    def build_boxes(self):
        boxes = np.empty(256, dtype=object)
        boxes[:] = [[] for _ in range(256)]
        for f in self.file_input:
            label = re.split("=|-", f)[0]
            box_num = self.hash_alg(label)
            if "-" in f:
                boxes[box_num] = [x for x in boxes[box_num] if label not in x]
            else:
                focal_length = int(re.split("=|-", f)[-1])
                if boxes[box_num] and any([label in x for x in boxes[box_num]]):
                    index = next(
                        (
                            i
                            for i, item in enumerate(boxes[box_num])
                            if item[0] == label
                        ),
                        -1,
                    )
                    boxes[box_num][index] = (label, focal_length)
                else:
                    boxes[box_num].append((label, focal_length))
        return boxes

    def focusing_power(self):
        boxes = self.build_boxes()
        total = 0
        for box_num, box in enumerate(boxes):
            for slot_num, slot in enumerate(box):
                total += (box_num + 1) * (slot_num + 1) * slot[1]
        return total
