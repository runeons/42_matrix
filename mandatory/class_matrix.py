from utils_colors import Colors

class Matrix:
    def __init__(self, *rows):
        try:
            self.rows = [list(row) for row in rows]
            self.check_validity()
            self.columns = self.get_columns()
        except:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}{[*rows]} is not a valid matrix.")

    def check_validity(self):
        if not len(self.rows):
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}{self.rows} is not a valid matrix.")
        prev_row_len = len(self.rows[0])
        for row in self.rows:
            if prev_row_len == 0 or len(row) != prev_row_len:
                raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}{self.rows} is not a valid matrix.")
            prev_row_len = len(row)

    def get_columns(self):
        nb_rows, nb_cols = self.shape()
        all_columns = []
        for col_index in range(nb_cols):
            new_column = []
            for row_index in range(nb_rows):
                new_column.append(self.rows[row_index][col_index])
            all_columns.append(new_column)
        # all_columns = [[self.rows[row_index][col_index] for row_index in range(nb_rows)] for col_index in range(nb_cols)]
        return all_columns

    def __str__(self):
        s = f"{Colors.MATRIX}MATRIX:{Colors.RES}\n"
        max_width = max([max(len(str(coord)) for coord in row) for row in self.rows])
        for i, row in enumerate(self.rows):
            s += "[ "
            for j, coord in enumerate(row):
                s += f"{coord:<{max_width}}"
                if j != len(row) - 1:
                    s += ", "
            s += " ]"
            if i != len(self.rows) - 1:
                s += "\n"
        return s
    
    def summary(self):
        print(self)
        print(f"{Colors.MATRIX}shape: {Colors.RES}{self.shape()}")
        print(f"{Colors.MATRIX}square: {Colors.RES}{self.is_square()}")
        print()

    def shape(self):
        x = len(self.rows)
        y = len(self.rows[0])
        return (x, y)

    def is_square(self):
        x, y = self.shape()
        return x == y
    
    # def add(self, m: 'Matrix'):
    #     if self.shape() != m.shape():
    #         raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two matrices of different sizes.")
    #     res = [ i + j for i, j in zip(self.rows, m.rows) ]
    #     return Matrix(*res)

    # def sub(self, m: 'Matrix'):
    #     return m
    #     if self.shape() != m.shape():
    #         raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two matrices of different sizes.")
    #     res = [ i - j for i, j in zip(self.rows, m.rows) ]
    #     return Matrix(*res)

    # def scl(self, scalar):
    #     return self
    #     res = [ i * scalar for i in self.rows]
    #     return Matrix(*res)
