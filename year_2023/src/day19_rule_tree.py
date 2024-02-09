from AdventOfCode.support import support
import re


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.workflows = self.parse_workflows()
        self.parts = self.parse_parts()
        self.rules = self.rule_map()

        rules_complete = False
        while not rules_complete:
            rules_complete = True
            remove_rules = []
            for rules_idx in range(len(self.rules)):
                rule = self.rules[rules_idx]
                if self.update_rule(rule):
                    remove_rules.append(rules_idx)
                    rules_complete = False
            [self.rules.pop(x) for x in remove_rules[::-1]]

    def parse_workflows(self):
        workflows = {}
        for row in self.file_input:
            if not row:
                break
            name, row = row[:-1].split("{")
            workflows[name] = row
        return workflows

    def parse_parts(self):
        parts = []
        for row in self.file_input:
            if row and row[0] == "{":
                nums = [int(x) for x in re.findall(r"\d+", row)]
                parts.append({"x": nums[0], "m": nums[1], "a": nums[2], "s": nums[3]})
        return parts

    def follow_workflow(self, part, workflow):
        workflow = re.split("[{:,]", workflow)
        for i in workflow:
            if "<" in i:
                cat, num = i.split("<")
                rule_result = part[cat] < int(num)
            elif ">" in i:
                cat, num = i.split(">")
                rule_result = part[cat] > int(num)
            else:
                if rule_result:
                    return i
        return i

    def update_rule(self, rule):
        removed_rule = False
        for rule_idx, rule_part in enumerate(rule):
            if not (("<" in rule_part) or (">" in rule_part)):
                # if it's the last rule part and it's A or R
                if (rule_part in "AR") and (rule_idx + 1 == len(rule)):
                    break
                elif rule_part in "AR":
                    rule1 = rule[: rule_idx + 1]
                    rule2 = (
                        rule[: rule_idx - 1]
                        + [self.swap_sign(rule[rule_idx - 1])]
                        + rule[rule_idx + 1 :]
                    )
                    new_rules = [rule1, rule2]
                else:
                    new_rules = self.rule_map(rule[rule_idx], rule[:rule_idx])
                [self.rules.append(r) for r in new_rules]
                removed_rule = True
                break
        return removed_rule

    def rule_map(self, workflow="in", previous_rule=[]):
        workflow = re.split("[{:,]", self.workflows[workflow])
        new_rules = []
        # Append the normal extension
        new_rules.append(previous_rule + [workflow[0], workflow[1]])

        # If the next part is an inequality
        if ("<" in workflow[2]) or (">" in workflow[2]):
            # Add that part with the inequality
            new_rules.append(
                previous_rule + [self.swap_sign(workflow[0])] + workflow[2:4]
            )
            # If part after that is an inequality
            if ("<" in workflow[4]) or (">" in workflow[4]):
                # Add that part with the inequality
                new_rules.append(
                    previous_rule
                    + [self.swap_sign(workflow[0])]
                    + [self.swap_sign(workflow[2])]
                    + workflow[4:6]
                )
                new_rules.append(
                    previous_rule
                    + [self.swap_sign(workflow[0])]
                    + [self.swap_sign(workflow[2])]
                    + [self.swap_sign(workflow[4])]
                    + workflow[6:]
                )
            else:
                # But also add the reverse of that inequality
                new_rules.append(
                    previous_rule
                    + [self.swap_sign(workflow[0])]
                    + [self.swap_sign(workflow[2])]
                    + workflow[4:]
                )
        # Otherwise just the one added rule is fine
        else:
            new_rules.append(
                previous_rule + [self.swap_sign(workflow[0])] + workflow[2:]
            )
        return new_rules

    def process_part(self, part):
        workflow = "in"
        while workflow not in "AR":
            workflow = self.follow_workflow(part, self.workflows[workflow])
        return workflow

    def process_parts(self):
        sum_ratings = 0
        for part in self.parts:
            if self.process_part(part) == "A":
                sum_ratings += sum(list(part.values()))
        return sum_ratings

    def swap_sign(self, rule_str):
        if "<" in rule_str:
            rule_str = rule_str.replace("<", ">=")
        elif ">" in rule_str:
            rule_str = rule_str.replace(">", "<=")
        return rule_str

    def process_rule_list(self, rule):
        limits = {
            "x": [1, 4000],
            "m": [1, 4000],
            "a": [1, 4000],
            "s": [1, 4000],
        }
        for rule_part in rule[:-1]:
            rating = rule_part[0]
            if rule_part[2] == "=":
                fn = rule_part[1:3]
                num = int(rule_part[3:])
            else:
                fn = rule_part[1]
                num = int(rule_part[2:])
            if fn == "<":
                limits[rating][1] = min(limits[rating][1], num - 1)
            elif fn == "<=":
                limits[rating][1] = min(limits[rating][1], num)
            elif fn == ">":
                limits[rating][0] = max(limits[rating][0], num + 1)
            elif fn == ">=":
                limits[rating][0] = max(limits[rating][0], num)
        return limits

    def sum_rules(self):
        rule_sum = 0
        for rule in self.rules:
            if rule[-1] == "A":
                print(rule)
                limits = self.process_rule_list(rule)
                print(limits)
                limit_sums = [x[1] - x[0] + 1 for x in limits.values()]
                print(limit_sums)
                limit_prod = 1
                for i in limit_sums:
                    limit_prod *= i
                rule_sum += limit_prod
                print(limit_prod)
        return rule_sum
