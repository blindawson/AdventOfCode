from AdventOfCode.support import support
import re
import numpy as np


class MonkeyMap:
    def __init__(self, filename: str, version: str = "Part 1"):
        """Coordinates in [y, x]
        y moves from top down
        x moves left right
        coordinates include empty spaces

        Parameters
        ----------
        filename : str
            full path to input file
        version : str
            Part 1
            Part 2 Example
            Part 2
        """
        self.version = version
        self.maplist = support.read_input(filename, flavor="str_grid")[:-2]
        self.pad_rows()
        self.map = np.array(self.maplist)
        if self.version == "Part 2 Example":
            self.block_size = int(self.map.shape[1] / 4)
        else:
            self.block_size = int(self.map.shape[0] / 4)
        instructions = support.read_input(filename)[-1]
        instructions = re.findall(r"(\d+|[A-Za-z])", instructions)
        self.instructions = [
            int(item) if item.isdigit() else item for item in instructions
        ]
        # Current position
        self.y, self.x = [0, np.where(self.map[0] == ".")[0][0]]
        # Current direction
        self.dir = "e"
        self.travel()

    def pad_rows(self) -> None:
        max_row_len = max([len(row) for row in self.maplist])
        for y, row in enumerate(self.maplist):
            if len(row) < max_row_len:
                pad_len = max_row_len - len(row)
                self.maplist[y] += [" "] * pad_len

    def move_forward(self) -> bool:
        stop_moving = False
        dir2coord = {
            "e": [self.y, self.x + 1],
            "w": [self.y, self.x - 1],
            "n": [self.y - 1, self.x],
            "s": [self.y + 1, self.x],
        }
        ny, nx = dir2coord[self.dir]
        ndir = self.dir
        # If next is " " then loop back to the other side
        # Or if next is out of bounds then loop back to the other side
        if support.point_out_of_bounds(ny, nx, self.map) or (self.map[ny, nx] == " "):
            if self.version == "Part 1":
                loop_dict = {
                    "e": self.find_extents_left(self.y),
                    "w": self.find_extents_right(self.y),
                    "n": self.find_extents_down(self.x),
                    "s": self.find_extents_up(self.x),
                }
                idx, _ = loop_dict[self.dir]
                if self.dir in ["e", "w"]:
                    nx = idx
                else:
                    ny = idx
            elif self.version == "Part 2 Example":
                ny, nx, ndir = self.cross_edge_example()
            else:
                ny, nx, ndir = self.cross_edge_real()
        # If next is "#" then don't go next
        if self.map[ny, nx] == "#":
            ny, nx, ndir = [self.y, self.x, self.dir]
            stop_moving = True
        self.x = nx
        self.y = ny
        self.dir = ndir
        return stop_moving

    def find_extents_left(self, y: int) -> list[int]:
        row = self.map[y]
        min_idx_dot = np.where(row == ".")[0][0]
        if "#" in row:
            min_idx_hash = np.where(row == "#")[0][0]
            min_idx_x = min(min_idx_dot, min_idx_hash)
        else:
            min_idx_x = min_idx_dot
        min_val_x = row[min_idx_x]
        return min_idx_x, min_val_x

    def find_extents_right(self, y: int) -> list[int]:
        row = self.map[y]
        max_idx_dot = np.where(row == ".")[0][-1]
        if "#" in row:
            max_idx_hash = np.where(row == "#")[0][-1]
            max_idx_x = max(max_idx_dot, max_idx_hash)
        else:
            max_idx_x = max_idx_dot
        max_val_x = row[max_idx_x]
        return max_idx_x, max_val_x

    def find_extents_up(self, x: int) -> list[int]:
        col = self.map[:, x]
        min_idx_dot = np.where(col == ".")[0][0]
        if "#" in col:
            min_idx_hash = np.where(col == "#")[0][0]
            min_idx_y = min(min_idx_dot, min_idx_hash)
        else:
            min_idx_y = min_idx_dot
        min_val_y = col[min_idx_y]
        return min_idx_y, min_val_y

    def find_extents_down(self, x: int) -> list[int]:
        col = self.map[:, x]
        max_idx_dot = np.where(col == ".")[0][-1]
        if "#" in col:
            max_idx_hash = np.where(col == "#")[0][-1]
            max_idx_y = max(max_idx_dot, max_idx_hash)
        else:
            max_idx_y = max_idx_dot
        max_val_y = col[max_idx_y]
        return max_idx_y, max_val_y

    def turn(self, turn_dir: str) -> None:
        if turn_dir == "R":
            new_dir = {"e": "s", "s": "w", "w": "n", "n": "e"}
        else:
            new_dir = {"e": "n", "s": "e", "w": "s", "n": "w"}
        self.dir = new_dir[self.dir]

    def travel(self) -> None:
        for i in self.instructions:
            if isinstance(i, str):
                self.turn(i)
            else:
                for _ in range(i):
                    stop_moving = self.move_forward()
                    self.print_position()
                    if stop_moving:
                        break

    def print_position(self) -> None:
        print(self.y, self.x, self.dir, self.find_face_real())

    def password(self) -> int:
        facing = {"e": 0, "s": 1, "w": 2, "n": 3}
        return (self.y + 1) * 1000 + (self.x + 1) * 4 + facing[self.dir]

    def cross_edge_example(self) -> tuple[int]:
        """Figure out how to cross from one face of the cube to another."""
        cur_face = self.find_face_example()
        cur_ref = self.reference_point_example(cur_face)
        cur_row_ref = self.y - cur_ref[0]
        cur_col_ref = self.x - cur_ref[1]

        if cur_face == 1:
            if self.dir == "w":
                new_ref = self.reference_point_example(3)
                ny = new_ref[0]
                nx = new_ref[1] + cur_row_ref
                ndir = "s"
            elif self.dir == "e":
                new_ref = self.reference_point_example(6)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
            elif self.dir == "n":
                new_ref = self.reference_point_example(2)
                ny = new_ref[0]
                nx = new_ref[1] + self.block_size - 1 - cur_col_ref
                ndir = "s"
        elif cur_face == 2:
            if self.dir == "w":
                new_ref = self.reference_point_example(6)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + self.block_size - 1 - cur_row_ref
                ndir = "n"
            elif self.dir == "s":
                new_ref = self.reference_point_example(5)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + self.block_size - 1 - cur_col_ref
                ndir = "n"
            elif self.dir == "n":
                new_ref = self.reference_point_example(1)
                ny = new_ref[0]
                nx = new_ref[1] + self.block_size - 1 - cur_col_ref
                ndir = "s"
        elif cur_face == 3:
            if self.dir == "n":
                new_ref = self.reference_point_example(1)
                ny = new_ref[0] + cur_col_ref
                nx = new_ref[1]
                ndir = "e"
            elif self.dir == "s":
                new_ref = self.reference_point_example(5)
                ny = new_ref[0] + self.block_size - 1 - cur_col_ref
                nx = new_ref[1]
                ndir = "e"
        elif cur_face == 4:
            if self.dir == "e":
                new_ref = self.reference_point_example(6)
                ny = new_ref[0]
                nx = new_ref[1] + self.block_size - 1 - cur_row_ref
                ndir = "s"
        elif cur_face == 5:
            if self.dir == "w":
                new_ref = self.reference_point_example(3)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + self.block_size - 1 - cur_row_ref
                ndir = "n"
            elif self.dir == "s":
                new_ref = self.reference_point_example(2)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + self.block_size - 1 - cur_col_ref
                ndir = "n"
        elif cur_face == 6:
            if self.dir == "e":
                new_ref = self.reference_point_example(1)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
            elif self.dir == "s":
                new_ref = self.reference_point_example(2)
                ny = new_ref[0] + self.block_size - 1 - cur_col_ref
                nx = new_ref[1]
                ndir = "e"
            elif self.dir == "n":
                new_ref = self.reference_point_example(4)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
        # return new position and direction
        return (ny, nx, ndir)

    def cross_edge_real(self) -> tuple[int]:
        """Figure out how to cross from one face of the cube to another."""
        cur_face = self.find_face_real()
        cur_ref = self.reference_point_real(cur_face)
        cur_row_ref = self.y - cur_ref[0]
        cur_col_ref = self.x - cur_ref[1]

        if cur_face == 1:
            if self.dir == "w":
                new_ref = self.reference_point_real(4)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1]
                ndir = "e"
            elif self.dir == "n":
                new_ref = self.reference_point_real(6)
                ny = new_ref[0] + cur_col_ref
                nx = new_ref[1]
                ndir = "e"
        elif cur_face == 2:
            if self.dir == "e":
                new_ref = self.reference_point_real(5)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
            elif self.dir == "s":
                new_ref = self.reference_point_real(3)
                ny = new_ref[0] + cur_col_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
            elif self.dir == "n":
                new_ref = self.reference_point_real(6)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + cur_col_ref
                ndir = "n"
        elif cur_face == 3:
            if self.dir == "w":
                new_ref = self.reference_point_real(4)
                ny = new_ref[0]
                nx = new_ref[1] + cur_row_ref
                ndir = "s"
            elif self.dir == "e":
                new_ref = self.reference_point_real(2)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + cur_row_ref
                ndir = "n"
        elif cur_face == 4:
            if self.dir == "w":
                new_ref = self.reference_point_real(1)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1]
                ndir = "e"
            elif self.dir == "n":
                new_ref = self.reference_point_real(3)
                ny = new_ref[0] + cur_col_ref
                nx = new_ref[1]
                ndir = "e"
        elif cur_face == 5:
            if self.dir == "e":
                new_ref = self.reference_point_real(2)
                ny = new_ref[0] + self.block_size - 1 - cur_row_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
            elif self.dir == "s":
                new_ref = self.reference_point_real(6)
                ny = new_ref[0] + cur_col_ref
                nx = new_ref[1] + self.block_size - 1
                ndir = "w"
        elif cur_face == 6:
            if self.dir == "e":
                new_ref = self.reference_point_real(5)
                ny = new_ref[0] + self.block_size - 1
                nx = new_ref[1] + cur_row_ref
                ndir = "n"
            elif self.dir == "s":
                new_ref = self.reference_point_real(2)
                ny = new_ref[0]
                nx = new_ref[1] + cur_col_ref
                ndir = "s"
            elif self.dir == "w":
                new_ref = self.reference_point_real(1)
                ny = new_ref[0]
                nx = new_ref[1] + cur_row_ref
                ndir = "s"
        # return new position and direction
        return (ny, nx, ndir)

    def find_face_example(self) -> int:
        """Find the face of the block for the current position

        Returns
        -------
        int
            The face number.
        """
        y, x = [self.y, self.x]
        if y < self.block_size:
            face = 1
        elif y < self.block_size * 2:
            if x < self.block_size:
                face = 2
            elif x < self.block_size * 2:
                face = 3
            else:
                face = 4
        else:
            if x < self.block_size * 3:
                face = 5
            else:
                face = 6
        return face

    def find_face_real(self) -> int:
        """Find the face of the block for the current position

        Returns
        -------
        int
            The face number.
        """
        y, x = [self.y, self.x]
        bs = self.block_size
        if y < bs:
            if x < bs * 2:
                face = 1
            else:
                face = 2
        elif y < bs * 2:
            face = 3
        elif y < bs * 3:
            if x < bs:
                face = 4
            else:
                face = 5
        else:
            face = 6
        return face

    def reference_point_example(self, face: int) -> tuple[int]:
        """List the position of the top left corner of each face (y, x)

        Parameters
        ----------
        face : int
            Face number we are pulling position of
        """
        bs = self.block_size
        rf_dict = {
            1: (0, bs * 2),
            2: (bs, 0),
            3: (bs, bs),
            4: (bs, bs * 2),
            5: (bs * 2, bs * 2),
            6: (bs * 2, bs * 3),
        }
        return rf_dict[face]

    def reference_point_real(self, face: int) -> tuple[int]:
        """List the position of the top left corner of each face (y, x)

        Parameters
        ----------
        face : int
            Face number we are pulling position of
        """
        bs = self.block_size
        rf_dict = {
            1: (0, bs),
            2: (0, bs * 2),
            3: (bs, bs),
            4: (bs * 2, 0),
            5: (bs * 2, bs),
            6: (bs * 3, 0),
        }
        return rf_dict[face]
