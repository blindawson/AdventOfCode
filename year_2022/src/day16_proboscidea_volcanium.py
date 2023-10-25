import pandas as pd
import re


class Volcano:
    def __init__(self, filename):
        self.file_input = open(filename).read().splitlines()
        self.read_input()

    def read_input(self):
        self.valves = pd.DataFrame(
            [], columns=["Valve", "Flow", "Tunnels", "Checked"]
        ).set_index("Valve")
        pattern = r"Valve (\w+) has flow rate=(\d+); tunnel(?:s)? lead(?:s)? to valve(?:s)? ([\w\s,]+)"
        for row in self.file_input:
            match = re.search(pattern, row)
            self.valves.loc[match.group(1)] = {
                "Flow": int(match.group(2)),
                "Tunnels": match.group(3).split(", "),
				"Checked": False
            }


filename = r"year_2022/tests/test_inputs/16_test_input.txt"
v = Volcano(filename)
print(v.valves)