class Matrix:
    def __init__(self, data):
        self.data = data
    def __str__(self):
       return f'\n'.join("\t".join([f'{itm:03}' for itm in line]) for line in self.data)
    def __add__(self, other):
        m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
             for line in range(len(self.data))]
        return Matrix(m)

m_1 = [[5, -30, 1, 6], [4, 40.88, -94, 5], [9, 110, 5, 0]]
m_2 = [[1, 1, 176, 2.8], [2, 2, 299, 2], [3, 3, 3, 1]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
mtrx_3 = mtrx_1 + mtrx_2
print(mtrx_3)

print("Спасибо огромное за Ваше бесценное объяснение!")

class Matrix:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        result_data = ''
        for line in self.data:
            result_line = "\t".join([f'{itm:03}' for itm in line]) + "\n"
            result_data += result_line
        return result_data

    def __add__(self, other):
        result_matrix = []
        for line1, line2 in zip(self.data, other.data):
            result_line = []
            for itm1, itm2 in zip(line1, line2):
                result = itm1 +itm2
                result_line.append(result)
            result_matrix.append(result_line)
        return Matrix(result_matrix)



m_1 = [[5, -30, 1, 6], [4, 40, -94, 5], [9, 110, 5, 0]]

m_2 = [[1, 1, 176, 2.8], [2, 2, 299, 2], [3, 3, 3, 1]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)


#(mtrx_1, mtrx_2)
mtrx_3 = mtrx_1 + mtrx_2
#print(mtrx_1, mtrx_2)
print(mtrx_3)