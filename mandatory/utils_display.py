from utils_colors import Colors
from memory_profiler import profile
from utils_constants import SPACE_COMPLEXITY

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

def print_OK(title, color=Colors.B_GREEN):
    print(f"{color}OK: {Colors.RES}{title}")

def print_KO(title, color=Colors.B_RED):
    print(f"{color}KO: {Colors.RES}{title}")

def space_complexity(func):
    if SPACE_COMPLEXITY:
        return profile(func)
    return func
