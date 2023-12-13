from AdventOfCode.support import support


class Mirage:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor="split", split_char=" ")
        self.next_num = 0
        self.prev_num = 0
        for row in self.file_input:
            a, b = self.row_diffs(row)
            self.prev_num += a
            self.next_num += b

    def row_diffs(self, row):
        row = [int(x) for x in row]
        diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        if not set(diffs) == {0}:
            prev_num, next_num = self.row_diffs(diffs)
            row[0] -= prev_num
            row[-1] += next_num
        return row[0], row[-1]
