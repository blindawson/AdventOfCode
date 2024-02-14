import numpy as np


class LoopFinder:
    def __init__(self, input_list, target_list_length=0, target_sum=0, match_length=10):
        self.input_list = input_list
        self.target_list_length = target_list_length
        self.target_sum = target_sum
        self.match_length = match_length
        self.loop_start, self.loop_length = self.find_loop()
        self.found_match = bool(self.loop_start)
        if self.found_match:
            self.pre_loop_sum = sum(self.input_list[: self.loop_start])
            self.loop_sum = sum(
                self.input_list[self.loop_start : self.loop_start + self.loop_length]
            )
            if self.target_list_length:
                self.total_loops_to_target = int(
                    (self.target_list_length - self.loop_start) / self.loop_length
                )
                self.post_loop_length = (
                    self.target_list_length - self.loop_start
                ) % self.loop_length
                self.post_loop_sum = sum(
                    self.input_list[
                        self.loop_start : self.loop_start + self.post_loop_length
                    ]
                )
                self.sum_to_target_length = (
                    self.pre_loop_sum
                    + self.loop_sum * self.total_loops_to_target
                    + self.post_loop_sum
                )
            elif self.target_sum:
                self.total_loops_to_target = int(
                    (self.target_sum - self.pre_loop_sum) / self.loop_sum
                )
                for i in range(self.loop_length):
                    self.post_loop_length = i
                    self.post_loop_sum = sum(
                        self.input_list[
                            self.loop_start : self.loop_start + self.post_loop_length
                        ]
                    )
                    self.sum_to_target_length = (
                        self.pre_loop_sum
                        + self.loop_sum * self.total_loops_to_target
                        + self.post_loop_sum
                    )
                    if self.sum_to_target_length >= self.target_sum:
                        break

    def find_loop(self):
        min_loop_size = self.match_length

        for start_index in range(len(self.input_list) - min_loop_size * 2 + 1):
            for end_index in range(start_index + min_loop_size, len(self.input_list)):
                loop_size = end_index - start_index
                found_full_match = True
                for i in range(self.match_length):
                    start_index1 = start_index + i
                    end_index1 = end_index + i
                    found_match = (
                        self.input_list[start_index1] == self.input_list[end_index1]
                    )
                    if not found_match:
                        found_full_match = False
                        break
                if found_full_match:
                    return start_index, loop_size
        return np.nan, np.nan


m = LoopFinder(
    input_list=[1, 2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7],
    target_list_length=20,
    match_length=5,
)
m.sum_to_target_length
