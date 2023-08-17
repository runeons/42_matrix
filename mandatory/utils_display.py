from utils_colors import Colors
from memory_profiler import profile
from utils_constants import SPACE_COMPLEXITY

def print_title(title, color=Colors.YELLOW):
    print(f"{color}{title}{Colors.RES}")

def space_complexity(func):
    if SPACE_COMPLEXITY:
        return profile(func)
    return func
