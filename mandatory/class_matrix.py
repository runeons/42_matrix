from utils_colors import Colors
from class_vector import Vector
from utils_display import space_complexity

class LogicError(Exception):
    "Raised when we try to calculate the inverse of a matrix with a 0 determinant"

class Matrix:
    def __init__(self, rows):
        try:
            self.rows = [list(row) for row in rows]
            self.check_validity()
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

    @space_complexity
    def transpose(self):
        nb_rows, nb_cols = self.shape()
        all_columns = [[self.rows[row_index][col_index] for row_index in range(nb_rows)] for col_index in range(nb_cols)]
        return Matrix([*all_columns])

    def __str__(self):
        return(str(self.rows))
        # s = f"{Colors.MATRIX}MATRIX:{Colors.RES}\n"
        # max_width = max([max(len(str(coord)) for coord in row) for row in self.rows])
        # for i, row in enumerate(self.rows):
        #     s += "[ "
        #     for j, coord in enumerate(row):
        #         s += f"{coord:<{max_width}}"
        #         if j != len(row) - 1:
        #             s += ", "
        #     s += " ]"
        #     if i != len(self.rows) - 1:
        #         s += "\n"
        # return s
    
    def summary(self):
        # print(self)
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
        # return s
        print(s)
        print(f"{Colors.MATRIX}shape: {Colors.RES}{self.shape()}")
        print(f"{Colors.MATRIX}square: {Colors.RES}{self.is_square()}")
        print()

    def __eq__(self, v):
        if isinstance(v, Matrix):
            if (self.rows == v.rows):
                return True
            else:
                return False
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}cannot compare Matrix with non-Matrix.")
        
    def __add__(self, m):
        if isinstance(m, Matrix) and self.shape() == m.shape():
            res = [[x1 + x2 for x1, x2 in zip(rows_self, rows_m)] for rows_self, rows_m in zip(self.rows, m.rows)]
            return Matrix([*res])
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrices should have the same dimension to use operator +.")

    def __sub__(self, m):
        if isinstance(m, Matrix) and self.shape() == m.shape():
            res = [[x1 - x2 for x1, x2 in zip(rows_self, rows_m)] for rows_self, rows_m in zip(self.rows, m.rows)]
            return Matrix([*res])
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrices should have the same dimension to use operator -.")

    def __mul__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            return self.scl(scalar)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrix multiplication not implemented.")

    def __div__(self, scalar):
        if (isinstance(scalar, int) or isinstance(scalar, float)):
            return self.scl(1 / scalar)
        else:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Matrix multiplication not implemented.")

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
        return Matrix([*res])

    def sub(self, m: 'Matrix'):
        if self.shape() != m.shape():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot add two matrices of different sizes.")
        res = [[c - d for c, d in zip(r, s)] for r, s in zip(self.rows, m.rows)]
        return Matrix([*res])

    def scl(self, scalar):
        res = [[c * float(scalar) for c in row] for row in self.rows]
        return Matrix([*res])

    @space_complexity
    def mul_vec(self, v):
        dim = v.size()
        if self.shape()[1] != dim:
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot perform matrix vector multiplication if the number of matrix columns (dimensions) differs from vector size (dimenssions).")
        new_nb_rows = self.shape()[0]
        res_coords = [0] * new_nb_rows
        for i in range(new_nb_rows):
            for j in range(dim):
                res_coords[i] += self.rows[i][j] * v.coordinates[j]
        return Vector([*res_coords])

    @space_complexity
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
        return Matrix([*res_coords])

    def trace(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Cannot perform matrix trace on non squared matrix.")
        trace = 0.
        for i in range(self.shape()[0]):
            trace += self.rows[i][i]
        return trace

    def _abs(self, x):
        if x < 0:
            return -x
        return x

    @space_complexity
    def row_echelon_not_so_reduced(self): # pivots not reduced to 1 (to find determinant via multiplication)
        ref = Matrix([*self.rows])
        (nb_rows, nb_cols) = ref.shape()
        pivot_row = 0
        sign = 1
        for pivot_col in range(nb_cols):
            max_val = 0
            k = 0
            for i in range(pivot_row, nb_rows):
                if ref._abs(ref.rows[i][pivot_col]) > max_val:
                    max_val = ref._abs(ref.rows[i][pivot_col])
                    k = i
            if ref.rows[k][pivot_col] == 0: 
                continue;
            else:
                if k != pivot_row:
                    ref.rows[k], ref.rows[pivot_row] = ref.rows[pivot_row], ref.rows[k]
                    sign *= -1
                for i in range(pivot_row + 1, nb_rows): # each row UNDERNEATH will be simplified/normalised (pivot doesn't change, hence 'not so reduced')
                    ratio = ref.rows[i][pivot_col] / ref.rows[pivot_row][pivot_col]
                    for j in range(pivot_col, nb_cols): # each FURTHER value in the row will be simplified/normalised (pivot doesn't change, hence 'not so reduced')
                        ref.rows[i][j] -= ref.rows[pivot_row][j] * ratio
                pivot_row += 1
        return ref, sign

    @space_complexity
    def row_echelon(self): # wiki - pivots reduced to 1 (but not pure reduced - other numbers in pivot column)
        ref = Matrix([*self.rows])
        (nb_rows, nb_cols) = ref.shape()
        r = 0
        for j in range(nb_cols):
            max_val = 0
            k = -1 
            for i in range(r, nb_rows):
                if ref._abs(ref.rows[i][j]) > max_val:
                    max_val = ref._abs(ref.rows[i][j])
                    k = i
            if k == -1:
                continue
            pivot_val = ref.rows[k][j]
            if pivot_val != 0:
                for l in range(j, nb_cols):
                    ref.rows[k][l] /= pivot_val
                if k != r:
                    ref.rows[k], ref.rows[r] = ref.rows[r], ref.rows[k]
                for i in range(nb_rows):
                    if i != r:
                        coef = -ref.rows[i][j]
                        for l in range(j, nb_cols):
                            ref.rows[i][l] += coef * ref.rows[r][l]
                r += 1
        return ref

    @space_complexity
    def determinant(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Non squared matrix don't have determinant.")
        ref, sign = self.row_echelon_not_so_reduced()
        det = 1
        for i in range(ref.shape()[0]):
            det *= ref.rows[i][i]
        return det * sign

    def _identity(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Non squared matrix don't have a corresponding identity matrix.")
        dim = self.shape()[0]
        params = [[1 if i==j else 0 for j in range(dim)] for i in range(dim)]
        return Matrix([*params])

    def _augmented(self, m):
        if self.shape() != m.shape():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Augmented matrix inputs should have the same shape.")
        nb_rows = self.shape()[0]
        nb_cols = self.shape()[1] * 2
        half = self.shape()[1]
        params = [[0 for _ in range(nb_cols)] for _ in range(nb_rows)]
        for i in range(nb_rows):
            for j in range(nb_cols):
                if j < half:
                    params[i][j] = self.rows[i][j]
                else:
                    params[i][j] = m.rows[i][j - half]
        return Matrix([*params])

    @space_complexity
    def inverse(self):
        if not self.is_square():
            raise ValueError(f"{Colors.ERROR}Error: {Colors.RES}Non squared matrix don't have absolute inverse.")
        det = self.determinant()
        if det == 0:
            raise LogicError(f"{Colors.ERROR}Error: {Colors.RES}Cannot compute inverse of a matrix with a nul determinant.")
        m_id = self._identity()
        m_aug = self._augmented(m_id)
        m_aug_rref = m_aug.row_echelon()
        m_inverse = Matrix([*[[0 for _ in range(self.shape()[0])] for _ in range(self.shape()[1])]])
        for i in range(m_inverse.shape()[0]):
            for j in range(m_inverse.shape()[1]):
                m_inverse.rows[i][j] = m_aug_rref.rows[i][j + m_inverse.shape()[1]]
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