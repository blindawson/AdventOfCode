from support import support


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(
            filename, flavor="split_int", split_char=" "
        )

    def part1(self):
        safe_reports = 0
        for report in self.file_input:
            diff0 = report[1] - report[0]
            if abs(diff0) > 0:
                safe_report = True
                for n1, n2 in zip(report[:-1], report[1:]):
                    diff = n2 - n1
                    same_increase_decrease_bool = diff / diff0 > 0
                    diff_quantity_bool = abs(diff) >= 1 and abs(diff) <= 3
                    if not same_increase_decrease_bool:
                        safe_report = False
                        break
                    if not diff_quantity_bool:
                        safe_report = False
                        break
                safe_reports += int(safe_report)
        return safe_reports

    def part2(self):
        pass


filename = r"year_2024/tests/test_inputs/02_test_input.txt"
# filename = r"year_2024/input/02_list_compare.txt"
m = ClassName(filename)
m.file_input
