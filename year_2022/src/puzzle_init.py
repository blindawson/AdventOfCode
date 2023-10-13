import os
import sys
import pathlib

project_dir = pathlib.Path.home() / "GitHub" / "AdventOfCode"
os.chdir(project_dir)
sys.path.append(str(project_dir))

from support import support
