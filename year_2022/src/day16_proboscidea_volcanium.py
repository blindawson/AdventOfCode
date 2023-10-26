import numpy as np
import re
from itertools import permutations


class Valve:
	def __init__(self, name, flow_rate, adjacent_valves):
		self.name = name
		self.flow_rate = flow_rate
		self.adjacent_valves = adjacent_valves
		self.distance_to_valves = {}
		# self.open = False

	def __repr__(self) -> str:
		return f"{self.name}: {self.flow_rate}, {self.distance_to_valves}"


class Volcano:
	def __init__(self, filename):
		self.all_valves = []
		self.flow_valves = []
		self.file_input = open(filename).read().splitlines()
		self.read_input()
		self.floyd_warshall_distance()
		self.max_pressure = 0

	def read_input(self):
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
		for valve in self.all_valves:
			for valve2 in self.all_valves:
				if valve == valve2:
					valve.distance_to_valves[valve2.name] = 0
				else:
					valve.distance_to_valves[valve2.name] = np.inf
			for adjacent_valve in valve.adjacent_valves:
				valve.distance_to_valves[adjacent_valve] = 1

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

	def explore_path(self, closed_valves, current_valve, time=30, pressure=0):
		if not closed_valves:
			self.max_pressure = max(self.max_pressure, pressure)
		else:
			for next_valve in closed_valves:
				# Move to next_valve
				remaining_time = (
					time - current_valve.distance_to_valves[next_valve.name]
				)

				if remaining_time > 2:
					# Open valve
					remaining_time -= 1
					remaining_valves = [v for v in closed_valves if v != next_valve]
					new_pressure = pressure + next_valve.flow_rate * remaining_time
					self.explore_path(
						closed_valves=remaining_valves,
						current_valve=next_valve,
						time=remaining_time,
						pressure=new_pressure,
					)
				else:
					self.max_pressure = max(self.max_pressure, pressure)

	# def max_pressure(self):
	# 	paths = list(permutations(self.flow_valves))
	# 	max_pressure = 0
	# 	for path in paths:
	# 		max_pressure = max(max_pressure, self.explore_path(path, self.find_valve("AA")))
	# 	return max_pressure


# filename = r"year_2022/tests/test_inputs/16_test_input.txt"
filename = r'year_2022/input/16_proboscidea_volcanium.txt'
v = Volcano(filename)
v.flow_valves


time = 30
pressure = 0
current_valve = v.find_valve("AA")
v.explore_path(v.flow_valves, current_valve)
