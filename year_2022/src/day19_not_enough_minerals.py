from AdventOfCode.support import support
import re
import copy
import random


class Blueprints:
    def __init__(self, filename: str) -> None:
        self.blueprints = []
        for b in support.read_input(filename):
            input_nums = re.findall(r"\d+", b)
            blueprint = {
                "num": int(input_nums[0]),
                "ore robot cost": {"ore": int(input_nums[1])},
                "clay robot cost": {"ore": int(input_nums[2])},
                "obsidian robot cost": {
                    "ore": int(input_nums[3]),
                    "clay": int(input_nums[4]),
                },
                "geode robot cost": {
                    "ore": int(input_nums[5]),
                    "obsidian": int(input_nums[6]),
                },
            }
            self.blueprints.append(blueprint)
        self.count = len(self.blueprints)

    # Return the blueprint based on it's number in the input file
    def blueprint(self, n: int):
        return self.blueprints[n - 1]


class Backpack:
    def __init__(self) -> None:
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geodes = 0

        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0

    def collect_resources(self) -> None:
        self.ore += self.ore_robots
        self.clay += self.clay_robots
        self.obsidian += self.obsidian_robots
        # Dont collect geodes. The robot gave all the geodes up front

    def avalaible_actions(self, blueprint: dict) -> list[str]:
        actions = []
        if (self.ore >= blueprint["geode robot cost"]["ore"]) and (
            self.obsidian >= blueprint["geode robot cost"]["obsidian"]
        ):
            actions.append("geode robot")

        if (self.ore >= blueprint["obsidian robot cost"]["ore"]) and (
            self.clay >= blueprint["obsidian robot cost"]["clay"]
        ):
            actions.append("obsidian robot")

        if self.ore >= blueprint["clay robot cost"]["ore"]:
            actions.append("clay robot")

        if self.ore >= blueprint["ore robot cost"]["ore"]:
            actions.append("ore robot")

        actions.append("do nothing")

        random.shuffle(actions)
        return actions

    def build_robot(self, robot_type: str, blueprint: dict, time_left: int) -> None:
        new_backpack = copy.deepcopy(self)
        if robot_type == "geode robot":
            new_backpack.geode_robots += 1
            new_backpack.ore -= blueprint["geode robot cost"]["ore"]
            new_backpack.obsidian -= blueprint["geode robot cost"]["obsidian"]
            new_backpack.geodes += time_left
        elif robot_type == "obsidian robot":
            new_backpack.obsidian_robots += 1
            new_backpack.ore -= blueprint["obsidian robot cost"]["ore"]
            new_backpack.clay -= blueprint["obsidian robot cost"]["clay"]
        elif robot_type == "clay robot":
            new_backpack.clay_robots += 1
            new_backpack.ore -= blueprint["clay robot cost"]["ore"]
        elif robot_type == "ore robot":
            new_backpack.ore_robots += 1
            new_backpack.ore -= blueprint["ore robot cost"]["ore"]
        elif robot_type == "do nothing":
            pass
        else:
            raise ValueError(f"Unrecognized robot type: {robot_type}")
        return new_backpack

    # What's the maximum geodes possible based on current backpack and time left
    def geode_potential(self, time_left):
        current_geodes = self.geodes
        current_production = self.geode_robots * time_left
        # If we built a new geode robot every minute from now on
        potential_production = int(time_left * (time_left + 1) / 2)
        return current_geodes + current_production + potential_production


class Mining:
    def __init__(self, blueprints: Blueprints, time_limit: int = 24) -> None:
        self.blueprints = blueprints
        self.time_limit = time_limit
        self.max_geodes = {key: 0 for key in range(1, blueprints.count + 1)}
        self.mine()

    def mine(self) -> int:
        for blueprint_num in range(1, self.blueprints.count + 1):
            blueprint = self.blueprints.blueprint(blueprint_num)
            self.max_geode = 0
            self.max_geodes[blueprint_num] = self.timestep(
                blueprint, Backpack(), 0, self.time_limit
            )

    def timestep(
        self, blueprint: dict, backpack: Backpack, time: int = 0, time_limit: int = 24
    ) -> int:
        time_left = time_limit - time
        while (time < time_limit) and (
            backpack.geode_potential(time_left) > self.max_geode
        ):
            time += 1
            time_left = time_limit - time
            actions = backpack.avalaible_actions(blueprint)
            backpack.collect_resources()
            self.max_geode = max(self.max_geode, backpack.geodes)
            for action in actions:
                new_backpack = backpack.build_robot(action, blueprint, time_left)
                self.max_geode = max(
                    self.max_geode,
                    self.timestep(blueprint, new_backpack, time, time_limit),
                )
        return self.max_geode
