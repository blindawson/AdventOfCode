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
    def __init__(
        self, filename, elephant1, elephant2, part2=False, silver_medal_pressure=0
    ):
        self.part2 = part2
        self.all_valves = []
        self.flow_valves = []
        self.file_input = open(filename).read().splitlines()
        self.read_input()
        self.floyd_warshall_distance()
        self.max_pressure = 0
        self.silver_medal_pressure = silver_medal_pressure
        self.elephant1 = elephant1
        self.elephant2 = elephant2
        elephant1.current_valve = self.find_valve("AA")
        elephant2.current_valve = self.find_valve("AA")

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

    def remaining_valves(self, elephant):
        remaining_valves = []
        for v in self.flow_valves:
            if not v.open:
                if (
                    elephant.current_valve.distance_to_valves[v.name] + 2
                    <= elephant.time
                ):
                    remaining_valves.append(v)
        return remaining_valves

    def open_valve(self, elephant, pressure, next_valve):
        # Move to next valve and open it
        lost_time = elephant.current_valve.distance_to_valves[next_valve.name] + 1
        elephant.time -= lost_time
        next_valve.open = True
        previous_valve = elephant.current_valve.name
        elephant.current_valve = next_valve
        new_pressure = pressure + next_valve.flow_rate * elephant.time
        if new_pressure > self.max_pressure:
            self.max_pressure = new_pressure
            self.best_path_valves = [v.name for v in self.flow_valves if v.open]

        # If there is time, keep going
        remaining_valves = self.remaining_valves(elephant)
        if remaining_valves:
            self.explore_path(
                closed_valves=remaining_valves, pressure=new_pressure, elephant=elephant
            )

        # Move back up the tree
        if self.part2:
            if new_pressure >= self.silver_medal_pressure:
                if elephant != self.elephant2:
                    remaining_valves2 = self.remaining_valves(self.elephant2)
                    if remaining_valves2:
                        self.explore_path(
                            closed_valves=remaining_valves2,
                            pressure=new_pressure,
                            elephant=self.elephant2,
                        )
        elephant.time += lost_time
        elephant.current_valve = self.find_valve(previous_valve)
        next_valve.open = False

    def explore_path(self, closed_valves, pressure=0, elephant=None):
        if not elephant:
            elephant = self.elephant1
        for next_valve in closed_valves:
            self.open_valve(elephant, pressure, next_valve)


def part2(filename):
    # Single elephant
    v = Volcano(filename, Elephant(time=26), Elephant(time=26))
    v.explore_path(v.flow_valves)
    best_path_valves = v.best_path_valves

    # Single elephant
    v = Volcano(filename, Elephant(time=26), Elephant(time=26))
    # Remove valves from best path
    for valve_name in best_path_valves:
        v.flow_valves.remove(v.find_valve(valve_name))
    v.explore_path(v.flow_valves)
    silver_medal_pressure = v.max_pressure

    # Double elephant
    v = Volcano(
        filename,
        Elephant(time=26),
        Elephant(time=26),
        part2=True,
        silver_medal_pressure=silver_medal_pressure,
    )
    v.explore_path(v.flow_valves)
    return v.max_pressure
