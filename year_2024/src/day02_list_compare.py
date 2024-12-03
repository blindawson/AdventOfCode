import copy

from support import support


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(
            filename, flavor="split_int", split_char=" "
        )
        self.file_input = [list(tup) for tup in self.file_input]

    def test_report(self, report_line):
        diff0 = report_line[1] - report_line[0]
        error_index = 0
        if abs(diff0) > 0:
            safe_report = True
            for n1, n2, idx in zip(
                report_line[:-1], report_line[1:], range(len(report_line) - 1)
            ):
                diff = n2 - n1
                same_increase_decrease_bool = diff / diff0 > 0
                diff_quantity_bool = abs(diff) >= 1 and abs(diff) <= 3
                if not same_increase_decrease_bool:
                    error_index = idx
                    safe_report = False
                    break
                if not diff_quantity_bool:
                    error_index = idx
                    safe_report = False
                    break
        else:
            safe_report = False
        return safe_report, error_index

    def part1(self):
        safe_reports = 0
        for report_line in self.file_input:
            self.test_report(report_line)
            safe_reports += int(self.test_report(report_line)[0])
        return safe_reports

    def part2(self):
        safe_reports = 0
        for report_line in self.file_input:
            print(report_line)
            safe_report, error_index = self.test_report(report_line)
            if not safe_report:
                report_line1 = report_line.copy()
                report_line1.pop(0)
                safe_report, _ = self.test_report(report_line1)
            if not safe_report:
                report_line1 = report_line.copy()
                report_line1.pop(error_index + 1)
                safe_report, _ = self.test_report(report_line1)
            if not safe_report:
                report_line2 = report_line.copy()
                report_line2.pop(error_index)
                safe_report, _ = self.test_report(report_line2)
            print(safe_report)
            safe_reports += int(safe_report)
        return safe_reports


filename = r"year_2024/tests/test_inputs/02_test_input.txt"
# filename = r"year_2024/input/02_list_compare.txt"
m = ClassName(filename)
# m.part2()
m.test_report([27, 24, 25, 26, 28, 31, 34])
