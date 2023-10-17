from AdventOfCode.support import support
import matplotlib.pyplot as plt


class Regolith:
    def __init__(self, filename, part2=False):
        self.file_input = support.read_input(
            filename, flavor="split", split_char=" -> "
        )
        self.rocks = self.read_rocks()
        self.max_rock_ele = max([x[1] for x in self.rocks])
        self.part2 = part2
        self.sand = []
        self.sand_amt = 0
        sand_start_loc = (500, 0)

        new_sand = self.falling_sand(sand_start_loc)
        while new_sand != "abyss":
            self.sand.append(new_sand)
            self.sand_amt += 1
            self.remove_extra_sand(new_sand)
            new_sand = self.falling_sand(sand_start_loc)
            # if self.sand_amt % 10000 == 0:
            #     self.plot_regolith(self.sand + self.rocks)
            #     print(self.sand_amt, len(self.sand), min([sand[1] for sand in self.sand]))

    def read_rocks(self):
        rocks = []
        for row in self.file_input:
            for i in range(len(row) - 1):
                [
                    rocks.append(x)
                    for x in self.draw_rock(eval(row[i]), eval(row[i + 1]))
                ]
        return list(set(rocks))

    def draw_rock(self, coordinate1, coordinate2):
        x1, y1 = coordinate1
        x2, y2 = coordinate2
        if x1 == x2:
            if y1 > y2:
                return [(x1, y) for y in range(y1, y2 - 1, -1)]
            else:
                return [(x1, y) for y in range(y1, y2 + 1)]
        else:
            if x1 > x2:
                return [(x, y1) for x in range(x1, x2 - 1, -1)]
            else:
                return [(x, y1) for x in range(x1, x2 + 1)]

    def falling_sand(self, sand_loc):
        x, y = sand_loc
        drop_locs = [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]
        for sand_loc1 in drop_locs:
            if self.part2:
                if sand_loc1[1] == self.max_rock_ele + 2:
                    self.rocks.append(sand_loc1)
                if (500, 0) in self.sand:
                    return "abyss"
            else:
                if sand_loc1[1] > self.max_rock_ele:
                    return "abyss"
            if sand_loc1 not in self.rocks and sand_loc1 not in self.sand:
                return self.falling_sand(sand_loc1)
        return sand_loc

    def plot_regolith(self, points):
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        plt.scatter(x, y)
        plt.gca().invert_yaxis()
        plt.show()

    def remove_extra_sand(self, new_sand):
        x = new_sand[0]
        y = new_sand[1]
        adj_sands = [
            [(x - 2, y), (x - 1, y), (x, y), (x - 1, y + 1)],
            [(x - 1, y), (x, y), (x + 1, y), (x, y + 1)],
            [(x, y), (x + 1, y), (x + 2, y), (x + 1, y + 1)],
        ]
        for sand_list in adj_sands:
            if sand_list[-1] in self.sand:
                if all(sand in (self.sand + self.rocks) for sand in sand_list):
                    self.sand.remove(sand_list[-1])
