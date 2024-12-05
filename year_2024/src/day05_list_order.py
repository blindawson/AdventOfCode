from support import support
import math


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename)
        self.rules = []
        self.updates = []
        for row in self.file_input:
            if "|" in row:
                self.rules.append(tuple(map(int, row.split("|"))))
            elif "," in row:
                self.updates.append(tuple(map(int, row.split(","))))

    # Check if the update num list is ordered according to the rule
    def check_rule(self, rule, update):
        if rule[0] in update and rule[1] in update:
            follow_rule = update.index(rule[0]) < update.index(rule[1])
        else:
            follow_rule = True
        return follow_rule

    # Check if the update num list is ordered according to all rules
    def check_all_rules(self, update):
        follow_rules = True
        for rule in self.rules:
            if not self.check_rule(rule, update):
                follow_rules = False
                break
        return follow_rules

    def find_mid(self, update):
        mid_idx = math.floor(len(update) / 2)
        return update[mid_idx]

    def dependencies_dict(self, rules, update):
        dep_dict = {n: 0 for n in update}
        rules = self.update_rules(rules, update)
        for rule in rules:
            dep_dict[rule[1]] += 1
        return dep_dict

    def part1(self):
        sum_mids = 0
        for update in self.updates:
            if self.check_all_rules(update):
                sum_mids += self.find_mid(update)
        return sum_mids

    # Return just the relevant rules to a given num_list
    def update_rules(self, rules, num_list):
        new_rules = []
        for rule in rules:
            if rule[0] in num_list and rule[1] in num_list:
                new_rules.append(rule)
        return new_rules

    def kahns_algorithm(self, rules, num_list):
        new_list = []
        num_list = list(num_list)
        while num_list:
            rules = self.update_rules(rules, num_list)
            dep_dict = self.dependencies_dict(rules, num_list)
            queue = [key for key, value in dep_dict.items() if value == 0]

            new_list.append(queue[0])
            dep_dict.pop(queue[0])
            num_list.pop(num_list.index(queue[0]))
        return new_list

    def part2(self):
        sum_mids = 0
        for update in self.updates:
            if not self.check_all_rules(update):
                # kahn algorithm generates new update
                new_update = self.kahns_algorithm(self.rules, update)
                # add the middle number from new update
                sum_mids += self.find_mid(new_update)
        return sum_mids
