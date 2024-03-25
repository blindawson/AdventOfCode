from AdventOfCode.support import support
import numpy as np


class LineIntersection:
    def __init__(self, filename, test_area):
        """test area is (x1, x2, y1, y2)"""
        self.test_area = test_area
        self.file_input = support.read_input(filename, flavor="split", split_char=" @ ")
        self.read_input()

    def read_input(self):
        for r, row in enumerate(self.file_input):
            pos, vel = row
            pos = [int(x) for x in pos.split(", ")]
            vel = [int(x) for x in vel.split(", ")]
            self.file_input[r] = [pos, vel]

    def line_intersection(self, input1, input2):
        """give me the coordinates of where the lines intersect"""

        # Line input format: [[x1, y1, v1], [vx, vy, vz]]
        line1 = (
            (input1[0][0], input1[0][1]),
            (input1[0][0] + input1[1][0], input1[0][1] + input1[1][1]),
        )
        line2 = (
            (input2[0][0], input2[0][1]),
            (input2[0][0] + input2[1][0], input2[0][1] + input2[1][1]),
        )

        # Line input format: ((x1, y1), (x2, y2))
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            x = np.inf
            y = np.inf
            # print(line1, line2)
        else:
            d = (det(*line1), det(*line2))
            x = det(d, xdiff) / div
            y = det(d, ydiff) / div
        return (x, y)

    def line_dir(self, line_vel: tuple):
        if line_vel[0] <= 0:
            x = "left"
        else:
            x = "right"
        return x

    def xy_in_area(self, xy):
        x, y = xy
        if (
            (x >= self.test_area[0])
            and (x <= self.test_area[1])
            and (y >= self.test_area[2])
            and (y <= self.test_area[3])
        ):
            return True
        else:
            return False

    def directionally_correct(self, line1, line2, xy):
        """Check to see that intersection of two lines happens
        in the future (not the past)"""

        # which direction is intersection xy
        l1toxy = xy[0] - line1[0][0]
        l2toxy = xy[0] - line2[0][0]

        right_dir1 = self.line_dir(line1[1]) == self.line_dir([l1toxy])
        right_dir2 = self.line_dir(line2[1]) == self.line_dir([l2toxy])

        return right_dir1 and right_dir2

    def compare_lines(self):
        pairs = [
            [self.file_input[i], self.file_input[j]]
            for i in range(len(self.file_input))
            for j in range(i + 1, len(self.file_input))
        ]
        ints = 0
        for pair in pairs:
            line1, line2 = pair
            xy = self.line_intersection(line1, line2)
            if self.xy_in_area(xy) and self.directionally_correct(line1, line2, xy):
                # print((line1, line2))
                ints += 1
        return ints

    def intersection_time(self, intersect_pt, line_row, xv, yv):
        line1 = line_row.copy()
        line1[1] = [line1[1][0] - xv, line1[1][1] - yv, line1[1][2]]
        print(line1)
        return (intersect_pt[0] - line1[0][0]) / line1[1][0]

    def part2(self, r):
        for xv in range(-r, r):
            for yv in range(-r, r):
                line1 = self.file_input[0].copy()
                line2 = self.file_input[1].copy()
                line1[1] = [line1[1][0] - xv, line1[1][1] - yv, line1[1][2]]
                line2[1] = [line2[1][0] - xv, line2[1][1] - yv, line2[1][2]]
                xy0 = self.line_intersection(line1, line2)

                xy_match = True
                # for i in range(2, len(self.file_input)-1, 2):
                for i in range(2, len(self.file_input)):
                    line1 = self.file_input[0].copy()
                    line2 = self.file_input[i].copy()
                    line1[1] = [line1[1][0] - xv, line1[1][1] - yv, line1[1][2]]
                    line2[1] = [line2[1][0] - xv, line2[1][1] - yv, line2[1][2]]
                    xy = self.line_intersection(line1, line2)
                    if (xy0 != xy) and (xy != (np.inf, np.inf)):
                        xy_match = False
                        break

                if xy_match:
                    return xv, yv, xy0
        return False, False, False

    def hail_loc(self, row_line, t):
        x, y, z = row_line[0]
        xv, yv, zv = row_line[1]
        return (x + xv * t, y + yv * t, z + zv * t)
