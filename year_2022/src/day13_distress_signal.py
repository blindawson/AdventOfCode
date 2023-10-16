import numpy as np
from AdventOfCode.support import support


class PacketPair:
    def __init__(self, packet1, packet2, packet_index):
        self.packet1 = packet1
        self.packet2 = packet2
        self.packet_index = packet_index
        self.right_order = self.check_order(self.packet1, self.packet2)

    def check_order(self, p1, p2, right_order=None):
        for v1, v2 in zip(p1, p2):
            # print(v1, v2)
            if isinstance(v1, int) and isinstance(v2, int):
                if v1 < v2:
                    right_order = True
                    break
                if v1 > v2:
                    right_order = False
                    break
            elif isinstance(v1, list) and isinstance(v2, list):
                right_order = self.check_order(v1, v2)
                if right_order is not None:
                    break
            else:
                if isinstance(v1, int):
                    v1 = [v1]
                if isinstance(v2, int):
                    v2 = [v2]
                right_order = self.check_order(v1, v2)
                if right_order is not None:
                    break
        if right_order is None:
            if len(p1) < len(p2):
                return True
            elif len(p1) > len(p2):
                return False
            else:
                return None
        else:
            return right_order

    def __str__(self):
        return f"Packet {self.packet_index}"


def right_order_sum(input_filename):
    signal_inputs = support.read_input(input_filename)
    right_order_index = []
    signal_index = 0
    for i in range(0, len(signal_inputs), 3):
        signal_index += 1
        p = PacketPair(eval(signal_inputs[i]), eval(signal_inputs[i + 1]), signal_index)
        if p.right_order:
            right_order_index.append(p.packet_index)
    print(right_order_index)
    return sum(right_order_index)
