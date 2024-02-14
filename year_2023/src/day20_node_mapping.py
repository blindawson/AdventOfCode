from AdventOfCode.support import support


class FlipFlop:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations
        self.on = False

    def pulse(self, freq, from_name):
        _ = from_name
        if freq == "high":
            self.on = self.on
            out_pulse = freq
            destinations = []
        else:
            if self.on:
                out_pulse = "low"
            else:
                out_pulse = "high"
            self.on = not self.on
            destinations = self.destinations
        return self.name, out_pulse, destinations


class Conjunction:
    def __init__(self, name, in_modules, destinations):
        self.name = name
        self.destinations = destinations
        self.in_modules = {x: "low" for x in in_modules}

    def pulse(self, freq, from_name):
        self.in_modules[from_name] = freq
        if all(value == "high" for value in self.in_modules.values()):
            out_pulse = "low"
        else:
            out_pulse = "high"
        return self.name, out_pulse, self.destinations


class Broadcast:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def pulse(self, freq, from_name):
        _ = from_name
        return self.name, freq, self.destinations


class ClassName:
    def __init__(self, filename, push_button_total=1000):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.push_button_total = push_button_total
        self.config = {}
        self.modules = {}
        self.low_to_rx = 0
        self.part2_list = []
        for row in self.file_input:
            module_name, destination_modules = row.split("->")
            module_name = module_name[:-1]
            destination_modules = destination_modules[1:].split(", ")
            self.config[module_name] = destination_modules
        for row in self.file_input:
            module_name, destination_modules = row.split("->")
            module_name = module_name[:-1]
            destination_modules = destination_modules[1:].split(", ")

            if module_name.startswith("%"):
                self.modules[module_name[1:]] = FlipFlop(
                    module_name[1:], destination_modules
                )
            elif module_name.startswith("&"):
                in_modules = []
                for key, value in self.config.items():
                    if module_name[1:] in value:
                        in_modules.append(key[1:])
                self.modules[module_name[1:]] = Conjunction(
                    module_name[1:], in_modules, destination_modules
                )
            else:
                self.modules[module_name[1:]] = Broadcast(
                    module_name[1:], destination_modules
                )

    def push_button(self):
        pulse_sum = {"low": 0, "high": 0}
        pulses = [("button", "low", ["roadcaster"])]
        any_destination = any([x[2] for x in pulses])
        low_to_rx = False

        while any_destination:
            new_pulses = []
            for pulse in pulses:
                pulse_origin, pulse_type, destinations = pulse
                for destination in destinations:
                    pulse_sum[pulse_type] += 1
                    if "jz" in self.modules.keys():
                        if any(
                            [
                                x == "high"
                                for x in self.modules["jz"].in_modules.values()
                            ]
                        ):
                            # print(self.modules["jz"].in_modules)
                            low_to_rx = [
                                key
                                for key, value in self.modules["jz"].in_modules.items()
                                if value == "high"
                            ]
                    if destination in self.modules.keys():
                        new_pulses.append(
                            self.modules[destination].pulse(pulse_type, pulse_origin)
                        )
            pulses = new_pulses
            any_destination = any([x[2] for x in pulses])

        return pulse_sum, low_to_rx

    def push_buttons(self):
        self.pulse_list = []
        for i in range(self.push_button_total):
            pulse_sum, low_to_rx = self.push_button()
            self.pulse_list.append(pulse_sum)

            if low_to_rx:
                print(i + 1, low_to_rx)
                self.part2_list.append(i + 1)
        low_pulses = sum([x["low"] for x in self.pulse_list])
        high_pulses = sum([x["high"] for x in self.pulse_list])
        return low_pulses * high_pulses


filename = r"year_2023/input/20_node_mapping.txt"
m = ClassName(filename, 10000)
m.push_buttons()
