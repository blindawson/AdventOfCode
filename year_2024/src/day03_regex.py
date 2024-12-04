from support import support
import re


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.file_input = "do()" + "".join(self.file_input)

    def part1(self):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, self.file_input)
        self.matches = [(int(n1), int(n2)) for n1, n2 in matches]
        return sum(n[0] * n[1] for n in self.matches)

    def part2(self):
        pattern = re.compile(r"(do\(\))|(don\'t\(\))|(mul\((\d{1,3}),(\d{1,3})\))")
        matches = re.findall(pattern, self.file_input)
        do_mul = True
        self.matches = []
        for x in matches:
            if x[0] == "do()":
                do_mul = True
            elif x[1] == "don't()":
                do_mul = False
            else:
                if do_mul:
                    self.matches.append([int(x[3]), int(x[4])])
        return sum(n[0] * n[1] for n in self.matches)
