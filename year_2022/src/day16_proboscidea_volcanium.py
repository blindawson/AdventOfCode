import numpy as np
import re


class Valve:
    def __init__(self, name, flow_rate, adjacent_valves):
        self.name = name
        self.flow_rate = flow_rate
        self.adjacent_valves = adjacent_valves
        self.distance_to_valves = {}
        self.open = False
        self.visited = 0

    def __repr__(self) -> str:
        return f"{self.name}: {self.flow_rate}, {self.open}"


class Elephant:
    def __init__(self, time=30, current_valve=None):
        self.time = time
        self.current_valve = current_valve

    def __repr__(self) -> str:
        return f"{self.time}, {self.current_valve.name}"


class Volcano:
    def __init__(self, filename, elephant1, elephant2, part2=False):
        self.part2 = part2
        self.all_valves = []
        self.flow_valves = []
        self.file_input = open(filename).read().splitlines()
        self.read_input()
        self.floyd_warshall_distance()
        self.max_pressure = 0
        self.elephant1 = elephant1
        self.elephant2 = elephant2
        elephant1.current_valve = self.find_valve("AA")
        elephant2.current_valve = self.find_valve("AA")
        # self.correct_path = [
        #     self.find_valve(x) for x in ["DD", "BB", "JJ", "HH", "EE", "CC"]
        # ]
        self.correct_path = [
            self.find_valve(x) for x in ["DD", "JJ", "BB", "HH", "CC", "EE"]
        ]

    def read_input(self):
        # Read input file with regular expression
        pattern = r"Valve (\w+) has flow rate=(\d+); tunnel(?:s)? lead(?:s)? to valve(?:s)? ([\w\s,]+)"
        for row in self.file_input:
            match = re.search(pattern, row)
            v = Valve(
                name=match.group(1),
                flow_rate=int(match.group(2)),
                adjacent_valves=match.group(3).split(", "),
            )
            self.all_valves.append(v)
            if v.flow_rate > 0:
                self.flow_valves.append(v)
        # Set distances between valves
        for valve in self.all_valves:
            for valve2 in self.all_valves:
                # If valve is the same, distance is 0
                if valve == valve2:
                    valve.distance_to_valves[valve2.name] = 0
                # Else set distance as infinite
                else:
                    valve.distance_to_valves[valve2.name] = np.inf
            # For adjacent valves, set distance to 1
            for adjacent_valve in valve.adjacent_valves:
                valve.distance_to_valves[adjacent_valve] = 1

    # Find distances between all valves
    def floyd_warshall_distance(self):
        for i in self.all_valves:
            for j in self.all_valves:
                for k in self.all_valves:
                    i.distance_to_valves[j.name] = min(
                        i.distance_to_valves[j.name],
                        i.distance_to_valves[k.name] + k.distance_to_valves[j.name],
                    )
                    j.distance_to_valves[i.name] = min(
                        j.distance_to_valves[i.name],
                        j.distance_to_valves[k.name] + k.distance_to_valves[i.name],
                    )

    def find_valve(self, valve_name):
        for valve in self.all_valves:
            if valve.name == valve_name:
                return valve

    def remaining_valves(self, current_valve, time):
        remaining_valves = []
        for v in self.flow_valves:
            if not v.open:
                if current_valve.distance_to_valves[v.name] < time:
                    remaining_valves.append(v)
        return remaining_valves
        # return [v for v in self.correct_path if not v.open]

    def open_valve(self, elephant, pressure, next_valve):
        # Move to next valve
        lost_time = elephant.current_valve.distance_to_valves[next_valve.name]
        elephant.time -= lost_time
        previous_valve = elephant.current_valve.name
        elephant.current_valve = next_valve

        # If there is time, keep going
        if elephant.time >= 2:
            next_valve.open = True
            next_valve.visited += 1
            elephant.time -= 1
            new_pressure = pressure + next_valve.flow_rate * elephant.time
            self.explore_path(
                closed_valves=self.remaining_valves(elephant.current_valve, elephant.time),
                pressure=new_pressure,
            )

            # Move back up the tree
            elephant.time += lost_time + 1
            elephant.current_valve = self.find_valve(previous_valve)
            next_valve.open = False

        else:
            elephant.time += lost_time
            elephant.current_valve = self.find_valve(previous_valve)
            self.max_pressure = max(self.max_pressure, pressure)

    def explore_path(self, closed_valves, pressure=0):
        if not closed_valves:
            self.max_pressure = max(self.max_pressure, pressure)
        else:
            for next_valve in closed_valves:
                if self.part2 and (self.elephant1.time >= self.elephant2.time):
                    self.open_valve(self.elephant1, pressure, next_valve)
                else:
                    self.open_valve(self.elephant2, pressure, next_valve)
                    
    def explore_path_part2(self, closed_valves, pressure=0):
        if not closed_valves:
            self.max_pressure = max(self.max_pressure, pressure)
        else:
            for next_valve in closed_valves:
                if self.part2 and (self.elephant1.time >= self.elephant2.time):
                    self.open_valve(self.elephant1, pressure, next_valve)
                else:
                    self.open_valve(self.elephant2, pressure, next_valve)


filename = r"year_2022/tests/test_inputs/16_test_input.txt"
# filename = r"year_2022/input/16_proboscidea_volcanium.txt"

# Part 1
# v = Volcano(filename, Elephant(), Elephant())
# v.explore_path_part2(v.flow_valves)

# Part 2
# v = Volcano(filename, Elephant(time=26), Elephant(time=26), part2=True)
# v.explore_path(v.correct_path)
