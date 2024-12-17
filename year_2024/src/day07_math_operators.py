from support import support
import itertools


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="None", split_char=None)
        for i, row in enumerate(self.file_input):
            row = row.split(": ")
            self.file_input[i] = (int(row[0]), [int(x) for x in row[1].split(" ")])

        self.operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else "undefined",
            "|": lambda a, b: int(str(a) + str(b)),
        }

    def check_inputs(self):
        results = [x[0] for x in self.file_input]
        inputs = []
        len_range = [9999, 0]
        for row in self.file_input:
            inputs += row[1]
            len_range[0] = min(len_range[0], len(row[1]))
            len_range[1] = max(len_range[1], len(row[1]))
        print(f"results from {min(results)} to {max(results)}")
        print(f"inputs from {min(inputs)} to {max(inputs)}")
        print(f"inputs lengths range is {len_range}")

    def test_row(self, row, operations):
        result = row[0]
        inputs = row[1]
        operator_list_len = len(inputs) - 1
        operator_list = [
            "".join(x) for x in itertools.product(operations, repeat=operator_list_len)
        ]
        for operator_combo in operator_list:
            subtotal = inputs[0]
            for i, o in zip(inputs[1:], operator_combo):
                if subtotal > result:
                    break
                subtotal = self.operations[o](subtotal, i)
            if subtotal == result:
                return result
        return 0

    def part1(self):
        sum_results = 0
        operations = "+*"
        for row in self.file_input:
            sum_results += self.test_row(row, operations)
        return sum_results

    def part2(self):
        sum_results = 0
        operations = "+*|"
        for row in self.file_input:
            sum_results += self.test_row(row, operations)
        return sum_results
