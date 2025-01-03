from support import support


class ClassName:
    def __init__(self, filename):
        self.file_input = list(
            support.read_input(filename, flavor="split_int", split_char=" ")[0]
        )
        self.file_input = [(x, 0) for x in self.file_input]
        self.answer_dict = {}

    def execute_rule(self, n, blink_limit, blink_count=0):
        while blink_count < blink_limit:
            blink_count += 1
            num_len = len(str(n))
            if n == 0:
                n = 1
            elif num_len % 2 == 0:
                self.branch_count += 1
                n_str = str(n)
                n = int(n_str[: int(num_len / 2)])
                n2 = int(n_str[int(num_len / 2) :])
                self.file_input.append((n2, blink_count))
            else:
                n = n * 2024
        # print(n)

    def part1(self, blink_limit):
        self.branch_count = len(self.file_input)
        while self.file_input:
            n = self.file_input.pop(0)
            self.execute_rule(n[0], blink_limit, n[1])
        return self.branch_count


filename = r"year_2024/tests/test_inputs/11_test_input.txt"
# filename = r"year_2024/input/11_stone_multiply.txt"
m = ClassName(filename)
# m.part1(25)
