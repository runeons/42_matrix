class Matrix:

    def error(self, msg):
        print("\033[31;01mError:\033[39;01m", msg ,"\033[0m")
        # quit()

    # constructeur
    def __init__ (self, *arg):
        if (isinstance(arg[0], tuple)):
            if len(arg[0]) != 2:
                raise ValueError("shape should be a 2-length tuple")
            self.rows, self.cols = arg[0]
            for x in (self.rows, self.cols):
                if type(x) is not int or x < 1:
                    raise ValueError("each value should be a positive int")
            self.data = []
            for r in range(self.rows):
                l = []
                for c in range(self.cols):
                    l.append(0)
                self.data.append(l)
            self.shape = (self.rows, self.cols);
        elif (isinstance(arg[0], list)):
            self.rows = 0
            self.cols = 0
            self.data = []
            if (len(set(map(len, arg[0]))) != 1):
                raise ValueError("all rows should have the same length")
            for row in arg[0]:
                self.cols = len(row)
                if (self.cols < 1):
                    raise ValueError("empty list")
                self.rows += 1
                for n in row:
                    if not (type(n) in (int, float)):
                        raise ValueError("all values should be numbers")
                self.data.append(row)
            self.shape = (self.rows, self.cols)
        else:
            raise ValueError("constructor accepts (r, c) or list of lists")

# # add : only matrices of same dimensions.
    def __add__(self, m):
        if isinstance(m, Matrix) and m.shape == self.shape:
            ret = [[x + y for x, y in zip(l1, l2)] for l1, l2 in zip(self.data, m.data)]
            if isinstance(m, Vector) and isinstance(self, Vector):
                return Vector(ret)
            return Matrix(ret)
        else:
            raise ValueError("Can't add two matrices with different dimensions")

    def __radd__(self, m):
        self.__add__(m)

# sub : only matrices of same dimensions.
    def __sub__(self, m):
        if isinstance(m, Matrix) and m.shape == self.shape:
            ret = [[x - y for x, y in zip(l1, l2)] for l1, l2 in zip(self.data, m.data)]
            if isinstance(m, Vector) and isinstance(self, Vector):
                return Vector(ret)
            return Matrix(ret)
        else:
            raise ValueError("Can't sub two matrices with different dimensions")

    def __rsub__(self, m):
        return self.__sub__(m)

# # div : only scalars.
    def __truediv__(self, n):
        if type(n) in (int, float) and n != 0:
            ret = [[x / n for x in row] for row in self.data]
            if isinstance(self, Vector):
                return Vector(ret)
            return Matrix(ret)
        else:
            raise ValueError("non-scalar division not supported")
    def __rtruediv__(self, m):
        return self.__truediv__(n)


# # mul : scalars, vectors and matrices , can have errors with vectors and matrices,
# # returns a Vector if we perform Matrix * Vector mutliplication.
    def mul_matrix(self, m):
        if (self.shape[1] != m.shape[0]):
            raise ValueError("nb cols of first matrix should be equal to nb rows of other matrix")
        if ((isinstance(self, Vector) or isinstance(m, Vector)) and (self.shape[0] == 1 or m.shape[1] == 1)):
            product = Vector((self.shape[0], m.shape[1]))
        else:
            product = Matrix((self.shape[0], m.shape[1]))
        for c in range(product.shape[1]):
            for r in range(product.shape[0]):
                for k in range(self.shape[1]):
                    product.data[r][c] = product.data[r][c] + self.data[r][k] * m.data[k][c]
        return product

    def mul_scalar(self, n):
        ret = [[x * n for x in row] for row in self.data]
        return Matrix(ret)

    def __mul__(self, m):
        if (isinstance(m, Matrix) or isinstance(m, Vector)):
            return self.mul_matrix(m)
        elif type(m) in (int, float):
            return self.mul_scalar(m)

    def __rmul__(self, m):
        return self.__mul__(m)

    def __str__(self):
        f_data = str([[ round(x, 2) for x in elem] for elem in self.data])
        if (isinstance(self, Vector)):
            return "Vector(" + f_data + ")"
        return "Matrix(" + f_data + ")"

    def __repr__(self):
        f_data = str([[ round(x, 2) for x in elem] for elem in self.data])
        return "Matrix(" + f_data + ")"

    def __eq__(self, m):
        if (isinstance(m, Matrix)):
            if (m.data == self.data and m.shape == self.shape):
                return True
        return False

    def T(self):
        ret = Matrix((self.shape[1], self.shape[0]))
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                ret.data[j][i] = self.data[i][j]
        return ret

class Vector(Matrix):
    def __init__(self, *arg):
        super().__init__(*arg)
        if self.shape[0] != 1 and self.shape[1] != 1:
            raise ValueError("a Vector shape must be (1, X) or (X, 1)")
    
    def dot(self, v):
        if (isinstance(v, Vector)):
            if (self.shape != v.shape):
                raise ValueError("Can't dot two vectors with different dimensions")
            n = 0
            if (self.shape[0] >= self.shape[1]):
                for i in range(self.shape[0]):
                    n += self.data[i][0] * v.data[i][0]
            else:
                for i in range(self.shape[1]):
                    n += self.data[0][i] * v.data[0][i]            
            return n
        else:
            raise ValueError("dot operation can only be performed with two vectors")
