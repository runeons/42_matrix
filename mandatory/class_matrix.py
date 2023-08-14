from utils_colors import Colors

class Matrix:
    def __init__(self, *rows):
        self.rows = [list(row) for row in rows]
        self.check_validity()

    def check_validity(self):
        # check if args same len
        # check if not empty
        pass
    
    def __str__(self):
        s = f"{Colors.PINK}MATRIX:{Colors.RES}\n"
        if not len(self.rows):
            s += "[]\n"
            return s
        for row in self.rows:
            if not len(row):
                s += "[]\n"
                return s
        max_width = max([max(len(str(coord)) for coord in row) for row in self.rows])
        for row in self.rows:
            s += "[ "
            for i, coord in enumerate(row):
                s += f"{coord:<{max_width}}"
                if i != len(row) - 1:
                    s += ", "
            s += " ]\n"
        return s

    def shape(self):
        x = len(self.rows)
        y = len(self.rows[0])
        return (x, y)