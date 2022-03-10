class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        mtrx = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for a in range(len(self.list_1)):

            for b in range(len(self.list_2[a])):
                mtrx[a][b] = self.list_1[a][b] + self.list_2[a][b]

        return str('\n'.join(['\t'.join([str(b) for b in a]) for a in mtrx]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(b) for b in a]) for a in mtrx]))

my_matrix = Matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])


print(my_matrix.__add__())