from AdventOfCode.support import support


class ClassName:
    def __init__(self, filename, part2=False):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.sum = 0
        for i in self.file_input:
            if part2:
                for num_string, num_num in self.num_dict.items():
                    i = i.replace(num_string, num_string + str(num_num) + num_string)
            nums = [x for x in i if x.isnumeric()]
            num = int(nums[0] + nums[-1])
            self.sum += num

    num_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
