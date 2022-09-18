import numpy as np


def get_norma1_for_vector(vector):
    x = 0

    for index in range(0, vector.shape[0]):
        x += abs(vector[index])

    return x


def get_infinity_normal_for_matrix(matrix):
    x = 0
    for i in range(matrix.shape[0]):
        x = 0
        for j in range(matrix.shape[1]):
            x += abs(matrix[i][j])
    return x


def get_normal1_for_matrix(matrix):
    x = 0
    for i in range(matrix.shape[0]):
        x = 0
        for j in range(matrix.shape[1]):
            x += abs(matrix[j][i])
    return x


def input_matrix():
    rows = int(input("Input number of rows: "))
    col = int(input("Input numbers of columns: "))

    matrix = []
    print("Input numbers")
    for i in range(rows):
        a = []
        for j in range(col):
            a.append(input())
        matrix.append(a)
    matrix2 = np.array(matrix, dtype=float)
    return matrix2


def input_vector():
    row = int(input("Input length of vector: "))
    vector = []

    print("Input numbers")
    for i in range(row):
        vector.append(input())
    vector2 = np.array(vector, dtype=float)

    return vector2


if __name__ == '__main__':
    #vector1 = np.array([0.1, 2, -5], dtype=float)

    #matrix1 = np.array([[0.1, 2, -5],
                        #[5, 1.2, 7],
                        #[3, 4, 8]], dtype=float)

    vector1 = input_vector()
    matrix1 = input_matrix()

    print(vector1, "\n")
    print(matrix1, "\n")
    print(f"Normal 1 for vector: {get_norma1_for_vector(vector1)}\tInfinity normal for matrix: "
          f"{get_infinity_normal_for_matrix(matrix1)}\t"
          f"Normal 1 for matrix: {get_normal1_for_matrix(matrix1)}")
