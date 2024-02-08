from AdventOfCode.support import support
import re


class ClassName:
    def __init__(self, filename):
        self.file_input = support.read_input(filename, flavor=None, split_char=None)
        self.workflows = self.parse_workflows()
        self.parts = self.parse_parts()

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


filename = r"year_2023/tests/test_inputs/19_test_input.txt"
m = ClassName(filename)
m.parse_workflows()
