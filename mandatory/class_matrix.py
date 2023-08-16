from utils_colors import Colors
from class_vector import Vector

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

    def transpose(self):
        nb_rows, nb_cols = self.shape()
        all_columns = [[self.rows[row_index][col_index] for row_index in range(nb_rows)] for col_index in range(nb_cols)]
        return Matrix(*all_columns)

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

    def __add__(self, m):
        if isinstance(m, Matrix) and self.shape() == m.shape():
            res = [[x1 + x2 for x1, x2 in zip(rows_self, rows_m)] for rows_self, rows_m in zip(self.rows, m.rows)]
            return Matrix(*res)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrices should have the same dimension to use operator +.")

    def __sub__(self, m):
        if isinstance(m, Matrix) and self.shape() == m.shape():
            res = [[x1 - x2 for x1, x2 in zip(rows_self, rows_m)] for rows_self, rows_m in zip(self.rows, m.rows)]
            return Matrix(*res)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrices should have the same dimension to use operator -.")

    def __mul__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            return self.scl(scalar)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrix multiplication not implemented yet.")

    def __div__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            return self.scl(1 / scalar)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrix multiplication not implemented yet.")

    def shape(self):
        x = len(self.rows)
        y = len(self.rows[0])
        return (x, y)

    def is_square(self):
        x, y = self.shape()
        return x == y
    
    def add(self, m: 'Matrix'):
        if self.shape() != m.shape():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two matrices of different sizes.")
        res = [[c + d for c, d in zip(r, s)] for r, s in zip(self.rows, m.rows)]
        return Matrix(*res)

    def sub(self, m: 'Matrix'):
        if self.shape() != m.shape():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two matrices of different sizes.")
        res = [[c - d for c, d in zip(r, s)] for r, s in zip(self.rows, m.rows)]
        return Matrix(*res)

    def scl(self, scalar):
        res = [[c * float(scalar) for c in row] for row in self.rows]
        return Matrix(*res)

    def mul_vec(self, v):
        dim = v.size()
        if self.shape()[1] != dim:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot perform matrix vector multiplication if the number of matrix columns (dimensions) differs from vector size (dimenssions).")
        new_nb_rows = self.shape()[0]
        res_coords = [0] * new_nb_rows
        for i in range(new_nb_rows):
            for j in range(dim):
                res_coords[i] += self.rows[i][j] * v.coordinates[j]
        return Vector(*res_coords)

    def _concat_mat_vec(m, v):
        pass

    def mul_mat(self, m):
        dim = self.shape()[1]
        if dim != m.shape()[0]:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot perform matrix matrix multiplication if the number of dimensions differs.")
        res_nb_rows = self.shape()[0]
        res_nb_cols = m.shape()[1]
        res_coords = [[0] * res_nb_cols for _ in range(res_nb_rows)]
        for c in range(res_nb_cols):
            for r in range(res_nb_rows):
                for i in range(dim):
                    res_coords[r][c] += self.rows[r][i] * m.rows[i][c]
        return Matrix(*res_coords)

    def trace(self):
        if self.shape()[0] != self.shape()[1]:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot perform matrix trace on non squared matrix.")
        trace = 0.
        for c in range(self.shape()[0]):
            for r in range(self.shape()[1]):
                if (c == r):
                    trace += self.rows[c][r]
        return trace