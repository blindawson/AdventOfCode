from support import support


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(
            filename, flavor="split_int", split_char=" "
        )[0]

    def execute_rule(self, n, blink_limit, blink_count=0):
        if blink_count < blink_limit:
            blink_count += 1
            num_len = len(str(n))
            if n == 0:
                output = [1]
            elif num_len % 2 == 0:
                self.branch_count += 1
                n_str = str(n)
                output = [
                    int(x)
                    for x in [n_str[: int(num_len / 2)], n_str[int(num_len / 2) :]]
                ]
            else:
                output = [n * 2024]

            for i in output:
                self.execute_rule(i, blink_limit, blink_count)
        print(n)

    def part1(self, blink_limit):
        self.branch_count = len(self.file_input)
        for n in self.file_input:
            self.execute_rule(n, blink_limit)
        return self.branch_count


filename = r"year_2024/tests/test_inputs/11_test_input.txt"
# filename = r"year_2024/input/11_stone_multiply.txt"
m = ClassName(filename)
# m.part1(6)
