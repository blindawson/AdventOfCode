from support import support
import re
import math
import matplotlib.pyplot as plt


class ClassName:
    def __init__(self, filename, width: int, height: int, seconds: int):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.width = width
        self.height = height
        self.seconds = seconds
        for i in range(len(self.file_input)):
            self.read_input(i)
        self.quadrants_y = (
            (0, math.floor(height / 2) - 1),
            (math.ceil(height / 2), height - 1),
        )
        self.quadrants_x = (
            (0, math.floor(width / 2) - 1),
            (math.ceil(width / 2), width - 1),
        )
        self.quadrant_totals = {}

    def read_input(self, input_row_num):
        pattern = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
        match = pattern.match(self.file_input[input_row_num])

        self.file_input[input_row_num] = {
            "p": (int(match.group(1)), int(match.group(2))),
            "v": (int(match.group(3)), int(match.group(4))),
        }

    def find_new_position(self, input_row, seconds):
        input_dict = self.file_input[input_row]
        new_x = (input_dict["p"][0] + input_dict["v"][0] * seconds) % self.width
        new_y = (input_dict["p"][1] + input_dict["v"][1] * seconds) % self.height
        self.file_input[input_row]["new position"] = (new_x, new_y)

    def assign_quadrant(self, input_row):
        input_dict = self.file_input[input_row]
        for qy in self.quadrants_y:
            for qx in self.quadrants_x:
                if (
                    qx[0] <= input_dict["new position"][0] <= qx[1]
                    and qy[0] <= input_dict["new position"][1] <= qy[1]
                ):
                    self.file_input[input_row]["quadrant"] = (qx, qy)

    def tally_quadrant_totals(self, input_row):
        if "quadrant" in self.file_input[input_row]:
            quadrant = self.file_input[input_row]["quadrant"]
            if quadrant in self.quadrant_totals:
                self.quadrant_totals[quadrant] += 1
            else:
                self.quadrant_totals[quadrant] = 1

    def part1(self, seconds):
        for input_row in range(len(self.file_input)):
            self.find_new_position(input_row, seconds)
            self.assign_quadrant(input_row)
            self.tally_quadrant_totals(input_row)
        return math.prod(self.quadrant_totals.values())

    # just keep looking at the plots until a tree appears at 6446 seconds
    def display_robots(self):
        for timestep in range(10000):
            seconds = 285 + timestep * 101
            self.part1(seconds)
            new_positions = [x["new position"] for x in self.file_input]

            x_coords = [pos[0] for pos in new_positions]
            y_coords = [pos[1] for pos in new_positions]
            std_dev_x = math.sqrt(
                sum((x - sum(x_coords) / len(x_coords)) ** 2 for x in x_coords)
                / len(x_coords)
            )
            std_dev_y = math.sqrt(
                sum((y - sum(y_coords) / len(y_coords)) ** 2 for y in y_coords)
                / len(y_coords)
            )

            if std_dev_x < 19.5:
                print(f"Seconds: {seconds}")
                print(f"Standard Deviation of X: {round(std_dev_x)}")
                print(f"Standard Deviation of Y: {round(std_dev_y)}")
                plt.gca().invert_yaxis()
                x_coords = [pos[0] for pos in new_positions]
                y_coords = [pos[1] for pos in new_positions]

                plt.scatter(x_coords, y_coords)
                plt.xlabel("X Coordinate")
                plt.ylabel("Y Coordinate")
                plt.title("New Positions")
                plt.grid(True)
                plt.show()
                pause = input("Press enter to continue or 'q' to quit: ")
                if pause.lower() == "q":
                    break
