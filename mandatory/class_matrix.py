from utils_colors import Colors
from class_vector import Vector

class LogicError(Exception):
    "Raised when we try to calculate the inverse of a matrix with a 0 determinant"

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
    
    def _abs(self, x):
        if x < 0:
            return -x
        return x

    # 3 elementary operations
    def _swap_rows(self, r1_i, r2_i):
        if (r1_i == r2_i):
            return
        tmp_r1 = self.rows[r1_i]
        self.rows[r1_i] = self.rows[r2_i]
        self.rows[r2_i] = tmp_r1

    def row_echelon(self):
        (nb_rows, nb_cols) = self.shape()
        r = -1
        for j in range(nb_cols):
            max_val = 0
            k = -1
            for i in range(r + 1, nb_rows):
                if self._abs(self.rows[i][j]) > max_val:
                    max_val = self._abs(self.rows[i][j])
                    k = i
            if k == -1:
                continue
            pivot = self.rows[k][j]
            if pivot != 0:
                r += 1
                for l in range(j, nb_cols):
                    self.rows[k][l] /= pivot
                if k != r:
                    self.rows[k], self.rows[r] = self.rows[r], self.rows[k]
                for i in range(nb_rows):
                    if i != r:
                        coeff = self.rows[i][j]
                        for l in range(j, nb_cols):
                            self.rows[i][l] -= coeff * self.rows[r][l]
        return self

    def _det_dim_2(self, m):
        if not m.is_square() or m.shape()[0] != 2:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Determinant of matrix 2x2.")
        det = m.rows[0][0] * m.rows[1][1] - m.rows[0][1] * m.rows[1][0]
        return det

    def _det_dim_3(self, m):
        if not m.is_square() or m.shape()[0] != 3:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Determinant of matrix 3x3.")
        a = m.rows[0][0]
        b = m.rows[0][1]
        c = m.rows[0][2]
        d = m.rows[1][0]
        e = m.rows[1][1]
        f = m.rows[1][2]
        g = m.rows[2][0]
        h = m.rows[2][1]
        i = m.rows[2][2]
        det =   a * self._det_dim_2(Matrix([e, f], [h, i])) - \
                b * self._det_dim_2(Matrix([d, f], [g, i])) + \
                c * self._det_dim_2(Matrix([d, e], [g, h]))
        return det

    def _det_dim_4(self, mat):
            a = mat.rows[0][0]
            b = mat.rows[0][1]
            c = mat.rows[0][2]
            d = mat.rows[0][3]
            e = mat.rows[1][0]
            f = mat.rows[1][1]
            g = mat.rows[1][2]
            h = mat.rows[1][3]
            i = mat.rows[2][0]
            j = mat.rows[2][1]
            k = mat.rows[2][2]
            l = mat.rows[2][3]
            m = mat.rows[3][0]
            n = mat.rows[3][1]
            o = mat.rows[3][2]
            p = mat.rows[3][3]
            det =   a * self._det_dim_3(Matrix([f, g, h], [j, k, l], [n, o, p])) \
                  - b * self._det_dim_3(Matrix([e, g, h], [i, k, l], [m, o, p])) \
                  + c * self._det_dim_3(Matrix([e, f, h], [i, j, l], [m, n, p])) \
                  - d * self._det_dim_3(Matrix([e, f, g], [i, j, k], [m, n, o]))
            return det

    def determinant(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Non squared matrix don't have determinant.")
        dim = self.shape()[0]
        if dim == 1:
            return self.rows[0][0]
        elif dim == 2:
            return self._det_dim_2(self)
        elif dim == 3:
            return self._det_dim_3(self)
        elif dim == 4:
            return self._det_dim_4(self)
        raise LogicError(f"{Colors.ERROR}Error: {Colors.RES}Determinant for matrices of dimensions higher than 4 not implemented.")
    
    def _comatrice(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Non squared matrix don't have comatrix.")
        dim = self.shape()[0]
        if dim == 2:
            a = self.rows[0][0]
            b = self.rows[0][1]
            c = self.rows[1][0]
            d = self.rows[1][1]
            com = Matrix([d, -c], [-b, a])
            return com
        elif dim == 3:
            a = self.rows[0][0]
            b = self.rows[0][1]
            c = self.rows[0][2]
            d = self.rows[1][0]
            e = self.rows[1][1]
            f = self.rows[1][2]
            g = self.rows[2][0]
            h = self.rows[2][1]
            i = self.rows[2][2]
            com = Matrix(
                [+self._det_dim_2(Matrix([e, f], [h, i])), -self._det_dim_2(Matrix([d, f], [g, i])), +self._det_dim_2(Matrix([d, e], [g, h]))], 
                [-self._det_dim_2(Matrix([b, c], [h, i])), +self._det_dim_2(Matrix([a, c], [g, i])), -self._det_dim_2(Matrix([a, b], [g, h]))], 
                [+self._det_dim_2(Matrix([b, c], [e, f])), -self._det_dim_2(Matrix([a, c], [d, f])), +self._det_dim_2(Matrix([a, b], [d, e]))]
            )
            return com
        raise LogicError(f"{Colors.ERROR}Error: {Colors.RES}Comatrix for matrices of dimensions higher than 3 not implemented.")

    def inverse(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Non squared matrix don't have absolute inverse.")
        det = self.determinant()
        if det == 0:
            raise LogicError(f"{Colors.ERROR}Error: {Colors.RES}Cannot compute inverse of a matrix with a nul determinant.")
        dim = self.shape()[0]
        if dim == 1:
            return Matrix([1/self.rows[0][0]])
        m_comatrice = self._comatrice()
        m_complementaire = m_comatrice.transpose()
        m_inverse = m_complementaire * (1 / det)
        return m_inverse
    
    def rank(self):
        m_rre = self.row_echelon()
        rank = 0
        (nb_rows, nb_cols) = m_rre.shape()
        for i in range(nb_rows):
            for j in range(nb_cols):
                if (m_rre.rows[i][j] == 1.0):
                    rank += 1
                    break
        return rank