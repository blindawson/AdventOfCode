import numpy as np
import re


class Valve:
    def __init__(self, name, flow_rate, adjacent_valves):
        self.name = name
        self.flow_rate = flow_rate
        self.adjacent_valves = adjacent_valves
        self.distance_to_valves = {}
        self.open = False

    def __repr__(self) -> str:
        return f"{self.name}: {self.open}"


class Volcano:
    def __init__(self, filename):
        self.all_valves = []
        self.flow_valves = []
        self.file_input = open(filename).read().splitlines()
        self.read_input()
        self.floyd_warshall_distance()
        self.max_pressure = 0

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

    def closed_valves(self):
        return [v for v in self.flow_valves if not v.open]

    def explore_path(self, closed_valves, current_valve, time=30, pressure=0):
        if not closed_valves:
            self.max_pressure = max(self.max_pressure, pressure)
        else:
            for next_valve in closed_valves:
                next_valve.open = True
                remaining_valves = self.closed_valves()
                remaining_time = (
                    time - current_valve.distance_to_valves[next_valve.name] - 1
                )

                if remaining_time > 2:
                    new_pressure = pressure + next_valve.flow_rate * remaining_time
                    self.explore_path(
                        closed_valves=remaining_valves,
                        current_valve=next_valve,
                        time=remaining_time,
                        pressure=new_pressure,
                    )
                    next_valve.open = False
                    a = 1
                else:
                    next_valve.open = False
                    self.max_pressure = max(self.max_pressure, pressure)

    def explore_path_part2(
        self,
        closed_valves,
        current_valve1,
        current_valve2,
        time1=26,
        time2=26,
        pressure=0,
    ):
        if not closed_valves:
            self.max_pressure = max(self.max_pressure, pressure)
        else:
            max_time = max(time1, time2)
            if time1 == max_time:
                for next_valve in closed_valves:
                    next_valve.open = True
                    remaining_valves = self.closed_valves()
                    remaining_time = (
                        time1 - current_valve1.distance_to_valves[next_valve.name] - 1
                    )
                    
                    if remaining_time > 2:
                        new_pressure = pressure + next_valve.flow_rate * remaining_time
                        self.explore_path(
                            closed_valves=remaining_valves,
                            current_valve1=next_valve,
                            current_valve2=current_valve2,
                            time1=remaining_time,
                            time2=time2,
                            pressure=new_pressure,
                        )
                        next_valve.open = False
                    else:
                        next_valve.open = False
                        self.max_pressure = max(self.max_pressure, pressure)

                   


filename = r"year_2022/tests/test_inputs/16_test_input.txt"
# filename = r"year_2022/input/16_proboscidea_volcanium.txt"
v = Volcano(filename)
current_valve = v.find_valve("AA")
v.explore_path(v.flow_valves, current_valve)

# correct_path = [v.find_valve(x) for x in ["DD", "BB", "JJ", "HH", "EE", "CC"]]
# v.explore_path(correct_path, current_valve)
v.max_pressure
