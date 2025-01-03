from support import support


class ClassName:
    def __init__(self, filename):
        self.file_input = list(
            support.read_input(filename, flavor="split_int", split_char=" ")[0]
        )
        self.file_input = [(x, 0) for x in self.file_input]
        self.answer_dict = {}

    def blink_action(self, n):
        num_len = len(str(n))
        if n == 0:
            n = 1
        elif num_len % 2 == 0:
            n_str = str(n)
            n = [int(n_str[: int(num_len / 2)]), int(n_str[int(num_len / 2) :])]
        else:
            n = n * 2024
        return n

    def execute_rule(self, n, blinks_left, stone_count):
        if (n, blinks_left) in self.answer_dict:
            return self.answer_dict[(n, blinks_left)]
        elif blinks_left > 0:
            ns = self.blink_action(n)
            if isinstance(ns, list):
                stone_count += self.execute_rule(ns[0], blinks_left - 1, stone_count)
                stone_count += self.execute_rule(ns[1], blinks_left - 1, 0)
            else:
                stone_count += self.execute_rule(ns, blinks_left - 1, stone_count)
        else:
            return 1

        self.answer_dict[(n, blinks_left)] = stone_count
        return stone_count

    def part1(self, blinks_left):
        stone_count = 0
        for n in self.file_input:
            stone_count += self.execute_rule(n[0], blinks_left, 0)
        return stone_count
