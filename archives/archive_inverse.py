class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def augmented(self):
        augmented = Matrix(self.rows, self.cols * 2)
        if self.rows != self.cols:
            print("error: augmented: matrix not square")
            return augmented

        for i in range(self.rows):
            for j in range(self.cols):
                if j < self.cols:
                    augmented.matrix[i][j + self.cols] = 1 if i == j else 0
                augmented.matrix[i][j] = self.matrix[i][j]

        return augmented

    def determinant(self):
        if self.rows != self.cols:
            print("error: determinant: matrix not square")
            return 0

        determinant = 1
        re = self.row_echelon()
        for i in range(self.rows):
            determinant *= re.matrix[i][i]

        return determinant

    def inverse(self):
        if self.rows != self.cols:
            print("error: inverse: matrix not square")
            return self

        left_reduced_to_In = self.augmented().reduced_row_echelon()
        if self.determinant() == 0:
            print("error: inverse: matrix's determinant is zero")
            return left_reduced_to_In

        inverse = Matrix(left_reduced_to_In.rows, left_reduced_to_In.cols)
        for i in range(inverse.rows):
            for j in range(inverse.cols):
                inverse.matrix[i][j] = left_reduced_to_In.matrix[i][j + inverse.cols]

        return inverse
    




#   inverse() {
#     if (!this.isSquare()) {
#       throw new AssertionError({
#         message: 'Matrix must be square.'
#       })
#     }

#     if (this.determinant().isZero()) {
#       throw new AssertionError({
#         message: 'Matrix must not be singular.'
#       })
#     }

#     const identity = Matrix.identityMatrix(this.rows)
#     const augmented = this.augment(identity)
#     const reducedRowEchelonForm = augmented.reducedRowEchelonForm()

#     return new Matrix(
#       reducedRowEchelonForm.matrix.map(vector => new Vector(vector.vector.slice(this.columns))))
#   }