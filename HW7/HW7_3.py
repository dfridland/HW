class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num

    def make_order(self, row):
        rows = self.cell_num // row
        tail = self.cell_num % row
        return '\n'.join(['*' * row] * rows + ['*' * tail])

      # return '\n'.join(["*" * row for i in range(self.cell_num // row)]) + '\n' + "*" * (self.cell_num % row)


    def __str__(self):
        return str(self.cell_num)

    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if self.cell_num > other.cell_num:
            return Cell(self.cell_num - other.cell_num)
        else:
            print("cell_1 must have more cellules than cell_2")

    def __mul__(self, other):
        return Cell(self.cell_num * other.cell_num)

    def __truediv__(self, other):
        return Cell(round(self.cell_num / other.cell_num))


cell_1 =  Cell(11)
cell_2 =  Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(3))


