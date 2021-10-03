class Matrix:
    def __init__(self, matrix_string):
        self.matrix_converted = [[int(value) for value in matrix_row.split()]
                                 for matrix_row in matrix_string.splitlines()]

    def row(self, index):
        return self.matrix_converted[index-1]

    def column(self, index):
        return [matrix_row[index-1] for matrix_row in self.matrix_converted]
