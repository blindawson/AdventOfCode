from AdventOfCode.support import support
import re
import copy
import math


def read_blueprint(blueprint: str) -> dict:
    input_nums = re.findall(r"\d+", blueprint)
    blueprint = {
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
    return blueprint


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

    def collect_resources(self, time_steps: int) -> None:
        self.ore += self.ore_robots * time_steps
        self.clay += self.clay_robots * time_steps
        self.obsidian += self.obsidian_robots * time_steps
        # Dont collect geodes. The robots get all the geodes up front

    def max_robots(self, blueprint: dict) -> dict:
        # Max resource needed per turn
        return {
            "ore": max([blueprint[x]["ore"] for x in blueprint]),
            "clay": blueprint["obsidian robot cost"]["clay"],
            "obsidian": blueprint["geode robot cost"]["obsidian"],
        }

    def next_robot(self, blueprint: dict) -> list[str]:
        actions = []
        if self.obsidian_robots > 0:
            actions.append("geode robot")

        if (self.clay_robots > 0) and (
            self.obsidian_robots <= self.max_robots(blueprint)["obsidian"]
        ):
            actions.append("obsidian robot")

        if self.clay_robots <= self.max_robots(blueprint)["clay"]:
            actions.append("clay robot")

        if self.ore_robots <= self.max_robots(blueprint)["ore"]:
            actions.append("ore robot")

        return actions

    def build_robot(self, robot_type: str, blueprint: dict, time_left: int) -> None:
        if robot_type == "geode robot":
            self.geode_robots += 1
            self.ore -= blueprint["geode robot cost"]["ore"]
            self.obsidian -= blueprint["geode robot cost"]["obsidian"]
            self.geodes += time_left
        elif robot_type == "obsidian robot":
            self.obsidian_robots += 1
            self.ore -= blueprint["obsidian robot cost"]["ore"]
            self.clay -= blueprint["obsidian robot cost"]["clay"]
        elif robot_type == "clay robot":
            self.clay_robots += 1
            self.ore -= blueprint["clay robot cost"]["ore"]
        elif robot_type == "ore robot":
            self.ore_robots += 1
            self.ore -= blueprint["ore robot cost"]["ore"]
        else:
            raise ValueError(f"Unrecognized robot type: {robot_type}")

    def time_needed_before_build(self, robot_type: str, blueprint: dict) -> int:
        if robot_type == "geode robot":
            required_ore = blueprint["geode robot cost"]["ore"]
            available_ore = self.ore
            ore_collection_rate = self.ore_robots
            ore_time_needed = math.ceil(
                (required_ore - available_ore) / ore_collection_rate
            )

            required_obsidian = blueprint["geode robot cost"]["obsidian"]
            available_obsidian = self.obsidian
            obsidian_collection_rate = self.obsidian_robots
            obsidian_time_needed = math.ceil(
                (required_obsidian - available_obsidian) / obsidian_collection_rate
            )

            return max(ore_time_needed, obsidian_time_needed, 0)

        elif robot_type == "obsidian robot":
            required_ore = blueprint["obsidian robot cost"]["ore"]
            available_ore = self.ore
            ore_collection_rate = self.ore_robots
            ore_time_needed = math.ceil(
                (required_ore - available_ore) / ore_collection_rate
            )

            required_clay = blueprint["obsidian robot cost"]["clay"]
            available_clay = self.clay
            clay_collection_rate = self.clay_robots
            clay_time_needed = math.ceil(
                (required_clay - available_clay) / clay_collection_rate
            )

            return max(ore_time_needed, clay_time_needed, 0)

        elif robot_type == "clay robot":
            required_ore = blueprint["clay robot cost"]["ore"]
            available_ore = self.ore
            ore_collection_rate = self.ore_robots
            ore_time_needed = math.ceil(
                (required_ore - available_ore) / ore_collection_rate
            )

            return max(ore_time_needed, 0)

        elif robot_type == "ore robot":
            required_ore = blueprint["ore robot cost"]["ore"]
            available_ore = self.ore
            ore_collection_rate = self.ore_robots
            ore_time_needed = math.ceil(
                (required_ore - available_ore) / ore_collection_rate
            )

            return max(ore_time_needed, 0)

    # What's the maximum geodes possible based on current backpack and time left
    def geode_potential(self, time_left):
        current_geodes = self.geodes
        current_production = self.geode_robots * time_left
        # If we built a new geode robot every minute from now on
        potential_production = int(time_left * (time_left + 1) / 2)
        return current_geodes + current_production + potential_production


class Mining:
    def __init__(self, blueprints: list[dict], time_limit: int = 24) -> None:
        self.blueprints = blueprints
        self.time_limit = time_limit
        self.max_geodes = {key: 0 for key in range(1, len(self.blueprints) + 1)}
        self.mine()
        self.get_quality_level()

    def get_quality_level(self) -> None:
        self.quality_level = 0
        for key, value in self.max_geodes.items():
            self.quality_level += key * value

    def mine(self) -> int:
        for blueprint_num in range(1, len(self.blueprints) + 1):
            blueprint = self.blueprints[blueprint_num - 1]
            self.max_geode = 0
            self.max_geodes[blueprint_num] = self.timestep(
                blueprint, Backpack(), 0, self.time_limit
            )

    def timestep(
        self, blueprint: dict, backpack: Backpack, time: int = 0, time_limit: int = 24
    ) -> int:
        self.max_geode = max(self.max_geode, backpack.geodes)
        if backpack.geode_potential(time_limit - time) > self.max_geode:
            actions = backpack.next_robot(blueprint)
            for action in actions:
                action_time = time
                time_steps = backpack.time_needed_before_build(action, blueprint)
                action_time += time_steps + 1
                time_left = time_limit - action_time

                if ((action == "geode robot") and (time_left > 0)) or (time_left > 2):
                    new_backpack = copy.deepcopy(backpack)
                    new_backpack.collect_resources(time_steps + 1)
                    new_backpack.build_robot(action, blueprint, time_left)

                    self.max_geode = max(
                        self.max_geode,
                        self.timestep(blueprint, new_backpack, action_time, time_limit),
                    )
        return self.max_geode
